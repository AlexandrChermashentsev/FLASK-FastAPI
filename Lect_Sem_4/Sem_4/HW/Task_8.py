'''
Задание №8
Напишите программу, которая будет скачивать страницы из списка URL-адресов и сохранять их в отдельные файлы на диске.
В списке может быть несколько сотен URL-адресов.
При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
Представьте три варианта решения.
'''

import threading
import time
import requests
import multiprocessing
import asyncio
import aiohttp



urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://www.youtube.com/',
        'https://sportcast.online/timetable/',
        'https://flexboxfroggy.com/#ru',
        'https://codepip.com/games/grid-garden/',
        'https://www.radiorecord.ru/'
        ]

def download(_url, prefix):
    response = requests.get(_url)
    filename = prefix + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        
def threads_my():
    threads = []   
    start_time = time.time()
    prefix = 'threading_'
    for url in urls:
        thread = threading.Thread(target=download, args=(url, prefix))
        threads.append(thread)
        thread.start()
            
    for thread in threads:
        thread.join()
        
    print(f"Threads run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
            

def multiprocessing_my():
    processes = []
    start_time = time.time()
    prefix = 'multiprocessing_'
    for url in urls:
        p = multiprocessing.Process(target=download, args=(url, prefix))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
    
    print(f"Multiprocessing run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
    
    
async def download_async(url, prefix):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = prefix + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
                # print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def async_my():
    tasks = []
    start_time = time.time()
    prefix = 'asyncio_'
    for url in urls:
        tasks.append(asyncio.create_task(download_async(url, prefix)))
    await asyncio.gather(*tasks)
    print(f"Async-func run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
    
    

        
if __name__ == '__main__':
    threads_my()
    multiprocessing_my()
    asyncio.run(async_my())
        
