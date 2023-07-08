#!/usr/bin/env python3


# def print_fibonacci(length):
#     fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     if length < 1:
#         print(f"[]")
#     elif length < 2:
#         print([fibonacci_sequence[0]], end="\n")
#     elif length < 3:
#         print(fibonacci_sequence[0:2], end="\n")
#     else:
#         print(fibonacci_sequence)


# Recurrenct relation, each term of the sequence (beyond 0 and 1) is a 
# function of the preceding terms
# F(0) = 0
# F(1) = 1
# F(n) = F(n -1) + F(n -2)


def print_fibonacci(length):
    start_sequence = [0, 1]
    if length < 1:
        print(f"[]")
    elif length < 2:
        print([start_sequence[0]])
    elif length < 3:
        print(start_sequence[0:2])
    else:
        for i in range(2, length):
            start_sequence.append(
                start_sequence[i - 1] + start_sequence[i - 2]
            )
        print(start_sequence)

print(print_fibonacci(10))


