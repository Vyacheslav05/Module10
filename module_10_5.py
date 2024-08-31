import time
import multiprocessing

def read_info(name):
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break

filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'Линейный вызов: {linear_time}')

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f'Многопроцессный вызов: {multiprocess_time}')