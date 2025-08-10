def fibonacci(n):
    """
    Generate a list of Fibonacci numbers up to n elements.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

def factorial(num):
    """
    Calculate the factorial of a number recursively.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def is_prime(number):
    """
    Check if a number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def list_primes(limit):
    """
    Generate a list of prime numbers up to a given limit.
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    print("Fibonacci sequence (10 elements):", fibonacci(10))
    print("Factorial of 5:", factorial(5))
    print("Prime numbers up to 20:", list_primes(20))

if __name__ == "__main__":
    main()
