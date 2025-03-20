from flask import Flask, jsonify
import random

app = Flask(__name__)

# Mock numbers for different IDs
number_map = {
    "p": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    "f": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
    "e": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    "o": [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
}

# Route to serve random numbers based on ID
@app.route('/numbers/<number_id>', methods=['GET'])
def mock_numbers(number_id):
    if number_id not in number_map:
        return jsonify({"error": "Invalid ID. Use 'p', 'f', 'e', or 'o'."}), 400

    # Randomly select up to 4 numbers
    numbers = random.sample(number_map[number_id], min(8, len(number_map[number_id])))

    response = {
        "numbers": numbers
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=9876)
