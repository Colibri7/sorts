from random import randint, shuffle

from past.builtins import xrange


def create_area(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


def is_sorted(a):
    for i in xrange(1, len(a)):
        if a[i] < a[i - 1]: return False
    return True


def bogo_sort(a):
    ct = 0
    while not is_sorted(a):
        shuffle(a)
        ct += 1
    return ct, a


a = create_area(10, 5)
mas = [11, 1, 3, 5, 6, 8, 345, 346, 346, 456]
print(f'Unsorted: ', mas)
ct, s = bogo_sort(mas)
print(f'Sorted: ', s)
print(f'Number of iterations: {ct}')
