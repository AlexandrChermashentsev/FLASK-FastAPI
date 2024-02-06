'''
Задание №7
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
Массив должен быть заполнен случайными целыми числами от 1 до 100.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
В каждом решении нужно вывести время выполнения вычислений.
'''

from threading import Thread
from multiprocessing import Process
import asyncio
import time
from random import randint


COUNT_ARR = 1_000_000
TREADS_MY = 5

def create_arr(count_arr: int) -> list:
    arr = []
    for _ in range(count_arr):
        arr.append(randint(1, 101))
    return arr

def sum_elements_arr(arr: list) -> int:
    _sum = 0
    for i in arr:
        _sum += i
    print(f'Summa: {_sum}')


def my_threads():
    threads = []
    start_time = time.time()
    
    for _ in range(TREADS_MY):
        thread = Thread(target=sum_elements_arr(create_arr(COUNT_ARR)))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Threads run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
    
    
def my_multiprocessing():
    processes = []
    start_time = time.time()
    
    for _ in range(TREADS_MY):
        process = Process(target=sum_elements_arr(create_arr(COUNT_ARR)))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print(f"Multiprocessing run {time.time() - start_time:.3f} seconds")
    print('-' * 50)


async def create_arr_async(count_arr: int) -> list:
    arr = []
    for _ in range(count_arr):
        arr.append(randint(1, 101))
    return arr

async def sum_elements_arr_async(arr: list) -> int:
    _sum = 0
    for i in arr:
        _sum += i
    print(f'Summa: {_sum}')
    
async def async_my():
    tasks_async = []
    start_time = time.time()
    for _ in range(TREADS_MY):
        tasks_async.append(asyncio.create_task(sum_elements_arr_async(await create_arr_async(COUNT_ARR))))
    await asyncio.gather(*tasks_async)
    print(f"Async function run {time.time() - start_time:.3f} seconds")



if __name__ == '__main__':
    my_threads()
    my_multiprocessing()
    asyncio.run(async_my())