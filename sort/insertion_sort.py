"""
https://en.wikipedia.org/wiki/Insertion_sort
"""


def insertion_sort(input):
    for i in range(1, len(input)):
        j = i
        while j > 0 and input[j - 1] > input[j]:
            input[j], input[j - 1] = input[j - 1], input[j]
            j -= 1
    return input


input_list = list(input())
print(insertion_sort(input_list))
