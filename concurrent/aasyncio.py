# -*- coding: utf-8 -*-
# @Time : 2022/2/11 16:41
# @Author : nobody
# @File : aasyncio.py
# @Software: PyCharm

import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
