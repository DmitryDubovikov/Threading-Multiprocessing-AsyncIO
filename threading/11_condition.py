import threading

data = []
condition = threading.Condition()


def producer():
    with condition:
        data.append(1)
        condition.notify()  # Оповещение других потоков


def consumer():
    with condition:
        while not data:
            condition.wait()  # Ожидание оповещения
        data.pop()


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

print(data)
producer_thread.start()
print(data)
consumer_thread.start()
print(data)
