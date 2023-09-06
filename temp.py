import asyncio


async def foo():
    print("Начало foo")
    await asyncio.sleep(1)
    print("Завершение foo")


async def bar():
    print("Начало bar")
    await asyncio.sleep(0.5)
    print("Завершение bar")


async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())
    await task1
    await task2


asyncio.run(main())
