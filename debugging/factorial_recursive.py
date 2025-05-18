#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Function Description:
    This function calculates the factorial of a given non-negative integer `n` using an iterative approach.
    Factorial is defined as the product of all positive integers less than or equal to `n`.
    Factorial of 0 is defined as 1.

    Parameters:
    - n (int): A non-negative integer for which the factorial needs to be calculated.

    Returns:
    - int: The factorial of the input integer `n`.

    Raises:
    - ValueError: If a negative integer is passed as input, a ValueError is raised since factorial is not defined for negative numbers.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except IndexError:
        print("Usage: ./script.py <non-negative integer>")
    except ValueError as e:
        print(f"Error: {e}")
