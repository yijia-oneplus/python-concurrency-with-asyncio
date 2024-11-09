import asyncio

async def hello_world_message()->str:
    await asyncio.sleep(1) # 暂停 hello_world_message 1秒
    return 'Hello，世界'

async def main()->None:
    message = await hello_world_message() # 暂停 main，直到 hello_world_message 完成
    print(message)


asyncio.run(main())
