import time

def my_func_1():
    print("1. fonksiyon başlıyor")
    time.sleep(5)
    print("1. fonksiyon bitti")
    return 5

def my_func_2():
    print("2. fonksiyon başlıyor")
    time.sleep(5)
    print("2. fonksiyon bitti")
    return 10

if __name__=='__main__':
    x=my_func_1()
    y=my_func_2()

print(x)
print(y)

# Asenkron yukarıdan aşağıya sırayla oluşur biri bitmeden diğeri başlamaz.
# Bu örnekte 1. fonskiyon bitmeden 2. fonksiyon çalışmaya başlamıyor web geliştirme yaparken bu yüzden senkron işlemlere ihtiyacımız olur

import asyncio

async def birinci_fonk():
    print("birinci fonksiyon başladı")
    await asyncio.sleep(5) #non blocking
    print("birinci fonksiyon bitti")
    return 5

async def ikinci_fonk():
    print("ikinci fonksiyon başladı")
    await asyncio.sleep(5)
    print("ikinci fonksiyon bitti")
    return 10

async def main():

    task1= asyncio.create_task(birinci_fonk())
    task2= asyncio.create_task(ikinci_fonk())

    x=await task1
    y=await task2

    print(x)
    print(y)

if __name__=='__main__':
    asyncio.run(main())
