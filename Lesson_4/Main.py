import requests
import os
from urllib.parse import urlparse
import threading
from multiprocessing import Process
import asyncio
import aiohttp
import time

list_url = [
    "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg",
    "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg",
]

def download_image(url):
    start_time = time.time()
    a = urlparse(url)
    img_data = requests.get(url).content
    with open(os.path.basename(a.path), 'wb') as handler:
        handler.write(img_data)
    end_time = time.time()
    print("Время выполнения загрузки изображений в потоках:", end_time - start_time, "секунд")

def proc_download_image_process(url):
    start_time = time.time()
    a = urlparse(url)
    img_data = requests.get(url).content
    with open(os.path.basename(a.path), 'wb') as handler:
        handler.write(img_data)
    end_time = time.time()
    print("Время выполнения загрузки изображений в процессах:", end_time - start_time, "секунд")

async def a_download_image(url):
    start_time = time.time()
    a = urlparse(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_data = await response.read()
            with open(os.path.basename(a.path), 'wb') as handler:
                handler.write(img_data)
    end_time = time.time()
    print("Время выполнения загрузки изображений в асинхронном режиме:", end_time - start_time, "секунд")


async def a_main():
    tasks = []
    for url in list_url:
        task = asyncio.create_task(a_download_image(url))
        tasks.append(task)
    
    await asyncio.gather(*tasks)



def main():
    print("1- потоки")
    print("2- процессор")
    print("3- асинх")
    print("4- Добавить ссылку")
    while True:
        selection = input("Введите метод: ")
        if(selection == "1"):
            start_time = time.time()
            threads = []
            for url in list_url:
                thread = threading.Thread(target=download_image, args=(url,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
            end_time = time.time()
            print("Время выполнения с использованием потоков:", end_time - start_time, "секунд")
        elif (selection == "2"):
            start_time = time.time()
            processes = []
            for url in list_url:
                process = Process(target=proc_download_image_process, args=(url,))
                process.start()
                processes.append(process)
            
            for process in processes:
                process.join()
            end_time = time.time()
            print("Время выполнения с использованием процессов:", end_time - start_time, "секунд")
        elif (selection == '3'):
            start_time = time.time()
            asyncio.run(a_main())
            end_time = time.time()
            print("Время выполнения с использованием асинхронного программирования:", end_time - start_time, "секунд")
        elif (selection == "4"):
            list_url.append(input("Введите ссылку: "))
        else:    
            print(list_url,sep="\n")

if __name__ == '__main__':
    main()