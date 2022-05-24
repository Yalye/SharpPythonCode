# -*- coding: utf-8 -*-
# @Time : 2022/5/24 17:30
# @Author : nobody
# @File : measure_tools.py
# @Software: PyCharm

from pympler.asizeof import asizeof

COUNT = 10_000

def numbers_1_to_10():
    numbers =  [i + 1 for i in range(10)]
    print(numbers)
    return numbers

def measure(name, func_of_fields, count=COUNT):
    blocks = [func_of_fields() for _ in range(count)]
    size = round(asizeof(blocks) / count)
    print(f"size of {name} is {size} bytes")
    return size

baseline = measure("list", numbers_1_to_10)