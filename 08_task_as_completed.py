import asyncio
import time
from typing import Literal


async def tick() -> Literal["Tick"]:
    await asyncio.sleep(1)
    return "Tick"


async def tock() -> Literal["Tock"]:
    await asyncio.sleep(2)
    return "Tock"


async def main():
    start = time.perf_counter()

    t1 = asyncio.create_task(tick())
    t2 = asyncio.create_task(tock())

    # чтобы возвращать результаты по мере их готовности
    for i, t in enumerate(asyncio.as_completed((t1, t2)), start=1):
        result: Literal["Tick", "Tock"] = await t
        elapsed_time = time.perf_counter() - start
        print(f"Task {i}: {result} in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
