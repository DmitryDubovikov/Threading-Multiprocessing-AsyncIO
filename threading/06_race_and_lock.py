import threading
import time
from concurrent import futures

####################################################################################
### так будет получаться разный баланс в зависимости от результатов гонки
# class BankAccount:
#     def __init__(self):
#         self.balance = 1

#     def update(self, reason, amount):
#         print(f"transaction {reason} started")
#         tmp_amount = self.balance
#         tmp_amount += amount
#         time.sleep(0.1)
#         self.balance = amount
#         print(f"transaction {reason} completed")

### так будет получаться разный баланс в зависимости от результатов гонки
####################################################################################


class BankAccount:
    def __init__(self):
        self.balance = 1
        # добавим Lock, чтобы избежать проблем гонки и переключения контекста
        self.lock = threading.Lock()

    def update(self, reason, amount):
        print(f"transaction {reason} started")

        with self.lock:
            # сюда может зайти и захватить lock только один поток, а второй будет ждать освобождения
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(0.1)
            self.balance = tmp_amount
        print(f"transaction {reason} completed, balance={acc.balance}")


if __name__ == "__main__":
    acc = BankAccount()
    print(f"main starting, balance={acc.balance}")

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ("refill", "withdraw"), (1, -2))

    print(f"main completed, balance={acc.balance}")
