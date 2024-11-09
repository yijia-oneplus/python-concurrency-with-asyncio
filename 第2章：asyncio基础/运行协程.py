import asyncio

async def coroutine_add_one(n:int)->int:
    return n+1

'''
asyncio.run 首先创建了一个全新的事件。
一旦成功创建，就会接受传递给它的任何协程，并运行它，直到完成，然后返回结果。
它还将对主协程完成后可能继续运行的任何内容进行清理。
一切完成之后，它会关闭，并结束事件循环
它旨在成为我们创建asyncio应用程序的主入口，它只执行一个协程，并且该协程应该启动应用程序的其他所有组件
'''
result = asyncio.run(coroutine_add_one(1))

print(result)
