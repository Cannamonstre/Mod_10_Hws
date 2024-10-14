import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f'Deposit: {amount} $. Balance: {self.balance} $')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)

    def withdraw(self):
        for i in range(100):
            amount = random.randint(50, 500)
            print(f'A new request for {amount} $')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Withdrawing {amount} $ in progress.. '
                          f'Actual balance: {self.balance} $')
                else:
                    print(f'Request rejected: insufficient funds')
                    self.lock.acquire()


my_bank = Bank()

deposit_thread = threading.Thread(target=Bank.deposit, args=(my_bank, ))
withdraw_thread = threading.Thread(target=Bank.withdraw, args=(my_bank, ))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(f'Final balance: {my_bank.balance}')
