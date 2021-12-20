# -*- coding: utf-8 -*-
# @Time : 2021/12/7 18:12
# @Author : nobody
# @File : union_types.py
# @Software: PyCharm

import typing

print(isinstance(5, int | str))

print(issubclass(bool, int | str))

print(isinstance(None, int | None))

print(isinstance(42, None | int))

print(type(int))
print(type(int | str))

# print(int | str == typing.Union[int, str])
#
# print(None | int == typing.Optional[int])

class M(type):
    def __or__(self, other):
        return "hello"

class C(metaclass=M):
    pass

print(C | int)
print(int | C)
print(type(C))


