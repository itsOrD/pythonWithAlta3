#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt
import time

def sundial():
    time.sleep(1)
    print(f'''Sundial: {dt.now()}''')

# for advanced use cases when you can't turn your
# blocking code into async code

async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.run_in_executor(None, sundial)
    task2 = loop.run_in_executor(None, sundial)
    tasks = [await task for task in [task1, task2]]


if __name__ == "__main__":
    asyncio.run(main())
