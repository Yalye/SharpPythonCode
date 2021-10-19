# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     hello_world
   Description :   
   Author :        Yalye
   date：          10/19/21
-------------------------------------------------
"""


def print_hw():
    print("Hello World!")

if __name__ == "__main__":
    print_hw()

""" python3.9 -m dis hello_world.py
  2           0 LOAD_CONST               0 ('\n-------------------------------------------------\n   File Name：     hello_world\n   Description :   \n   Author :        Yalye\n   date：          10/19/21\n-------------------------------------------------\n')
              2 STORE_NAME               0 (__doc__)

 12           4 LOAD_CONST               1 (<code object print_hw at 0x10fb75660, file "hello_world.py", line 12>)
              6 LOAD_CONST               2 ('print_hw')
              8 MAKE_FUNCTION            0
             10 STORE_NAME               1 (print_hw)

 15          12 LOAD_NAME                2 (__name__)
             14 LOAD_CONST               3 ('__main__')
             16 COMPARE_OP               2 (==)
             18 POP_JUMP_IF_FALSE       26

 16          20 LOAD_NAME                1 (print_hw)
             22 CALL_FUNCTION            0
             24 POP_TOP
        >>   26 LOAD_CONST               4 (None)
             28 RETURN_VALUE

Disassembly of <code object print_hw at 0x10fb75660, file "hello_world.py", line 12>:
 13           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello World!')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""
