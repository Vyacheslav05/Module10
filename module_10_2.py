import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.total_enemies = 100

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.total_enemies > 0:
            time.sleep(1)
            days += 1
            self.total_enemies -= self.power
            if self.total_enemies < 0:
                self.total_enemies = 0
            print(f"{self.name} сражается {days} день(дня)..., осталось {self.total_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")