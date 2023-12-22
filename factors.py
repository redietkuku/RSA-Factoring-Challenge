#!/usr/bin/env python3
import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return 1, n  # Fallback for prime numbers

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readlines()

    for number in numbers:
        n = int(number.strip())
        p, q = factorize(n)
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main(sys.argv[1])

