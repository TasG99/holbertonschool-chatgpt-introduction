#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <non-negative integer>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        if num < 0:
            raise ValueError
        print(factorial(num))
    except ValueError:
        print("Please provide a valid non-negative integer.")
        sys.exit(1)
