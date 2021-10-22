# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ast_sharp
   Description :   
   Author :        Yalye
   date：          10/22/21
-------------------------------------------------
"""

import ast

# node = ast.Expression(ast.BinOp(
#     ast.JoinedStr('xy'),
#     ast.Mult(),
#     ast.IntEnum(3)
# ))


source = '6 + 8'
node = ast.parse(source, mode='eval')

print(eval(compile(node, '<string>', mode='eval')))