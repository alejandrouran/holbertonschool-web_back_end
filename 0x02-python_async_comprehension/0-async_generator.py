#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments. """


import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """ async_generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
