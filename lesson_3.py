import collections
import random
from typing import List


def random_array(min: int, max: int, length: int):
    numbers = []
    for i in range(0, length):
        numbers.insert(i, random.randint(min, max))
    return numbers


def task_1(number: int):
    numbers = range(2, 99)
    count = sum(it % number == 0 for it in numbers)
    print(f'There are {count}')


def task_2():
    numbers = random_array(0, 10, 10)
    indexes = [i for i, it in filter(lambda it: it[1] % 2 == 0, enumerate(numbers))]
    print(numbers)
    print(indexes)


def task_3():
    numbers = random_array(0, 10, 10)
    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))
    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
    print(numbers)


def task_4():
    list = [10, 10, 10, 20, 20]
    result = max(collections.Counter(list).most_common(), key=lambda it: it[1])[0]
    print(result)


def task_5(items: List[int]):
    min_number = min(items)
    print(f'min[{min_number}]={items[min_number]}')
    pass
