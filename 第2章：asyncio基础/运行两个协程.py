import asyncio
from util import delay

async def add_one(n:int)->int:
    return n + 1

async def hello_world_message()->str:
    await delay(1)
    return 'Hello, 世界'

async def main()->None:
    msg = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(msg)


if __name__ == '__main__':
    asyncio.run(main())

