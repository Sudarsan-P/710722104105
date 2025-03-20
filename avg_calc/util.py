def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True

def fib(n):
    a = 5*(n**2)+4
    b = 5*(n**2)-4
    return int(a**0.5)**2 ==a or int(b**0.5)**2 == b
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    x1 = 5 * (n**2) + 4
    x2 = 5 * (n**2) - 4
    return int(x1**0.5)**2 == x1 or int(x2**0.5)**2 == x2

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def even(n):
    return n%2==0

def odd(n):
    return n%2!=0
