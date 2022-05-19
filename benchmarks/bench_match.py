# -*- coding: utf-8 -*-
# @Time : 2022/5/17 11:25
# @Author : nobody
# @File : match_and_if.py
# @Software: PyCharm

from typing import Mapping, Sequence

def sequence_match_logical():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐸", "🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        if isinstance(seq, Sequence) and len(seq) > 0 and seq[0] == "🐸":
            frogs += 1

    assert frogs == 100_000


def sequence_match_statement():
    """ Test matching the first element of a sequence is a frog. """
    seq = ["🐸", "🐛", "🦋", "🪲"]
    frogs = 0
    for _ in range(100_000):
        match seq:
            case ["🐸", *_]: frogs += 1

    assert frogs == 100_000

__benchmarks__ = [
    (sequence_match_logical, sequence_match_statement, "Match statements (sequence)")
]











