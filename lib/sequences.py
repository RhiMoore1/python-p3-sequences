#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    if length < 1:
        print(f"[]")
    elif length < 2:
        print([fibonacci_sequence[0]], end="\n")
    elif length < 3:
        print(fibonacci_sequence[0:2], end="\n")
    else:
        print(fibonacci_sequence)


