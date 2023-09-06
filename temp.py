import asyncio


async def task1():
    await asyncio.sleep(1)
    print("Task 1 is done")


async def task2():
    await asyncio.sleep(2)
    print("Task 2 is done")


async def main():
    await asyncio.gather(task1(), task2())


if __name__ == "__main__":
    asyncio.run(main())
