async def coroutine_add_one(n:int)->int:
    return n+1

def add_one(n:int)->int:
    return n+1

fn_result = add_one(1)
coroutine_result = coroutine_add_one(1)

print(f'函数的结果是：{fn_result}，它的类型是：{type(fn_result)}')
print(f'协程的结果是：{coroutine_result}，它的类型是：{type(coroutine_result)}')
