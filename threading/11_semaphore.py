import threading

semaphore = threading.Semaphore(2)  # Разрешение для двух потоков


def worker():
    with semaphore:
        print("Работник вошел")


for _ in range(4):
    threading.Thread(target=worker).start()
