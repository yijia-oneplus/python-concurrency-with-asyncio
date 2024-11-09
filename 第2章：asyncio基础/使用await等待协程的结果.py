import asyncio

async def add_one(n:int)->int:
    return n+1

async def main()->None:
    one_plus_one = await add_one(1) # 暂停，等待 add_one(1) 的结果
    two_plus_one = await add_one(2) # 暂停，等待 add_one(2) 的结果
    print(one_plus_one)
    print(two_plus_one)

if __name__ == '__main__':
    asyncio.run(main())

