import asyncio

async def count(i):
    print(f'Start {i}')
    await asyncio.sleep(i)
    print(f'End {i}')

# Not real async, since no task created.
async def main():
    await count(1)
    await count(2)

# Create task to let controller know.
async def main2():
    task1 = asyncio.create_task(count(1))
    task2 = asyncio.create_task(count(2))
    print("Tasks created")
    await task1
    await task2

# Create task in batch.
async def main3():
    coros = []
    for i in range(3):
        coros.append(count(i))
    await asyncio.gather(*coros)


# Register sequence matter, rather than calling order.
async def main4():
    task2 = asyncio.create_task(count(2))
    task1 = asyncio.create_task(count(1))
    print("Tasks created")
    await task1
    await task2

# Register and call are separated
async def main5():
    task2 = asyncio.create_task(count(2))
    task1 = asyncio.create_task(count(1))
    print("Tasks created")
    await count(3)
    # await count(4)
    # await task1
    # await task2

if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(main2())
    # asyncio.run(main3())
    # asyncio.run(main4())
    asyncio.run(main5())