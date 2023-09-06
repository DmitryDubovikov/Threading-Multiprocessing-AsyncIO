import asyncio


async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i


async def main():
    # async for используется для итерации по асинхронному итерируемому объекту
    # в асинхронном контексте
    async for item in async_generator():
        print(item)


if __name__ == "__main__":
    asyncio.run(main())
