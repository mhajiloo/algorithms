"""
https://en.wikipedia.org/wiki/Josephus_problem
"""

def josephus(sequence: list, skip: int):
    result = []

    skip = skip - 1
    idx = 0

    while len(sequence) > 0:
        idx = (idx + skip) % len(sequence)
        result.append(sequence.pop(idx))

    return result


t_list = list(input())

result = josephus(t_list, 3)
print(''.join(result[:-1]))
print('survivor: {}'.format(result[-1]))
