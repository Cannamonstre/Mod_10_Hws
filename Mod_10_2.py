from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, we are under attack')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            sleep(1)  # time import
            days += 1
            print(f'{self.name} is keep fighting for {days} day(s),'
                  f' {enemies} enemies left\n')
        print(f'{self.name} won the battle after {days} day(s) of fighting!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('The battle is over')
