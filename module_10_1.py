from threading import Thread
from datetime import datetime
from time import sleep

time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}\n"
            file.write(word)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

write_words(10, 'example.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков: {time_res}')

time_start = datetime.now()

write_words5 = Thread(target=write_words, args=(10, 'example5.txt'))
write_words6 = Thread(target=write_words, args=(30, 'example6.txt'))
write_words7 = Thread(target=write_words, args=(200, 'example7.txt'))
write_words8 = Thread(target=write_words, args=(100, 'example8.txt'))

write_words5.start()
write_words6.start()
write_words7.start()
write_words8.start()

write_words5.join()
write_words6.join()
write_words7.join()
write_words8.join()

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков: {time_res}')


