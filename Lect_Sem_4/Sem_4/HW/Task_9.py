'''
Задание №9
Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. 
Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
'''

import threading
import time
import requests
import multiprocessing
import asyncio
import aiohttp
import aiofiles

URLS_TEST = ['https://images.wallpaperscraft.ru/image/single/tsvetok_lepestki_zheltyj_1164739_1280x720.jpg',
       'https://images.wallpaperscraft.ru/image/single/paporotnik_rastenie_listia_108470_1280x720.jpg',
       'https://img.wallscloud.net/uploads/thumb/1544489603/macro-1-61202-1024x576-MM-80.webp',
       'https://images.wallpapershq.com/wallpapers/8232/wallpaper_8232_3840x2160.jpg',
       'https://7themes.su/_ph/55/975683577.jpg',
       'https://images.wallpaperscraft.ru/image/single/stvol_derevo_tekstura_119590_1280x720.jpg',
       'https://images.wallpaperscraft.ru/image/single/bmw_k100_mototsikl_bajk_123991_1280x720.jpg',
       'https://images.wallpaperscraft.ru/image/single/stakan_limon_bryzgi_122158_1280x720.jpg',
       'https://images.wallpaperscraft.ru/image/single/derevo_listia_priroda_71206_1280x720.jpg',]

def download_img(_url: str, prefix: str):
    start_time = time.time()
    file_name = prefix + _url.split('/')[-1]
    print(_url)
    p = requests.get(_url)
    out = open(file_name, "wb")
    out.write(p.content)
    out.close()
    print(f"Downloaded {file_name} in {time.time() - start_time:.3f} seconds")

    
def threads_my(urls: list):
    threads = []   
    start_time = time.time()
    prefix = 'threading_'
    for url in urls:
        thread = threading.Thread(target=download_img, args=(url, prefix))
        threads.append(thread)
        thread.start()
            
    for thread in threads:
        thread.join()
        
    print(f"Threads run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
    

def multiprocessing_my(urls: str):
    processes = []
    start_time = time.time()
    prefix = 'multiprocessing_'
    for url in urls:
        p = multiprocessing.Process(target=download_img, args=(url, prefix))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
    
    print(f"Multiprocessing run {time.time() - start_time:.3f} seconds")
    print('-' * 50)
    

async def download_img_async(_url, prefix):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(_url) as response:
            
            file_name = prefix + _url.split('/')[-1]
            f = await aiofiles.open(file_name, mode='wb')
            await f.write(await response.read())
            await f.close()
            print(f"Downloaded {_url} in {time.time() - start_time:.3f} seconds")
            
            
async def async_my(urls: str):
    tasks = []
    start_time = time.time()
    prefix = 'asyncio_'
    for url in urls:
        tasks.append(asyncio.create_task(download_img_async(url, prefix)))
    await asyncio.gather(*tasks)
    print(f"Async-func run {time.time() - start_time:.3f} seconds")
    print('-' * 50)


def validate_link(link: str) -> bool: # Не стал прописывать метод
    return True


def main_my():
    urls = []
    while True:
        print('Введите команду: \n"1" - Добавить изображение в список\n"2" - Добавить тестовые изображения в список\n"3" - Сохранить на диск\n"0" - Выход')
        command = input('-> ')
        
        match command:
            case "1":
                command = input('Введите ссылку на изображение -> ')
                if validate_link(command):
                    urls.append(command)
                    print(f'{"-" * 10} Изображение добавлено {"-" * 10}')
                else: 
                    print('Ссылка не валидна')
            
            case "2":
                for i in URLS_TEST:
                    urls.append(i)
                print(f'{"-" * 10} Базовые изображения добавлены {"-" * 10}')
            
            case "3":
                threads_my(urls)
                multiprocessing_my(urls)
                asyncio.run(async_my(urls))
                
            case "0":
                break


if __name__ == '__main__':
    main_my()