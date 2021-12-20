# -*- coding: utf-8 -*-
# @Time : 2021/12/20 11:53
# @Author : nobody
# @File : test_tqdm.py
# @Software: PyCharm

from tqdm import tqdm

for i in tqdm(range(10000)):
    ...


#seq 9999999 | tqdm --bytes | wc -l
#https://tqdm.github.io/