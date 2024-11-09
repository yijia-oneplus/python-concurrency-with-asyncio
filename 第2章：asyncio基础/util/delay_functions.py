import asyncio

async def delay(secs:int)->int:
    print(f'休眠{secs}秒')
    await asyncio.sleep(secs)
    print(f'完成休眠{secs}秒')
    return secs
