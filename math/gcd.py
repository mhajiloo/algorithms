"""
https://en.wikipedia.org/wiki/Greatest_common_divisor
"""


def gcd(a: int, b: int) -> int:
    while True:
        if b == 0:
            return a

        a, b = b, a % b


a = int(input())
b = int(input())

print(gcd(a, b))
