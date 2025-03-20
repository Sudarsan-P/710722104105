from flask import Flask, jsonify, request
import requests
import time
from util import is_prime, is_fibonacci, is_even, is_odd

app = Flask(__name__)

WINDOW_SIZE = 10
window = []

BASE_URL = "http://localhost:9876/numbers"

@app.route('/numbers/<number_id>', methods=['GET'])
def get_numbers(number_id):
    global window

    id_map = {"p": is_prime, "f": is_fibonacci, "e": is_even, "o": is_odd}


    if number_id not in id_map:
        return jsonify({'error': 'Invalid ID. Use p, f, e, or o.'}), 400

    try:
        start_time = time.time()
        response = requests.get(f"{BASE_URL}/{number_id}", timeout=10) 
        end_time = time.time()

        response_time = end_time - start_time
        print(f"Response time: {response_time} seconds")

        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch data from server', 'status_code': response.status_code}), 500

        new_numbers = response.json().get("numbers", [])

        window_prev = window.copy()
        window.extend(new_numbers)
        window = window[-WINDOW_SIZE:]  

        avg = sum(window) / len(window) if window else 0

        result = {
            "numbers": new_numbers,
            "windowPrevState": window_prev,
            "windowCurrState": window,
            "avg": avg
        }

        return jsonify(result)

    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection refused. Ensure the server is running on port 5000.'}), 500

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Request timed out. Try increasing the timeout or check server load.'}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
