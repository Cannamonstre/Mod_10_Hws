import queue
from threading import Thread
import random
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_waiting = random.randint(3, 10)
        time.sleep(time_waiting)


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None

            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table:
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} took table number {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} is in the queue')

    def guest_discuss(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} finished eating and left")
                    print(f"Table number {table.number} is free")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    print(f"{next_guest.name} left the queue and took table number {table.number}")
                    table.guest = next_guest
                    next_guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.guest_discuss()
