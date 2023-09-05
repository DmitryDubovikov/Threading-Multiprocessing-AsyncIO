import threading

# Создаем два мьютекса
mutex_a = threading.Lock()
mutex_b = threading.Lock()


def thread_a():
    print("Thread A: Попытка захвата мьютекса A")
    mutex_a.acquire()
    print("Thread A: Мьютекс A захвачен")
    print("Thread A: Попытка захвата мьютекса B")
    mutex_b.acquire()
    print("Thread A: Мьютекс B захвачен")
    mutex_b.release()
    mutex_a.release()


def thread_b():
    print("Thread B: Попытка захвата мьютекса B")
    mutex_b.acquire()
    print("Thread B: Мьютекс B захвачен")
    print("Thread B: Попытка захвата мьютекса A")
    mutex_a.acquire()
    print("Thread B: Мьютекс A захвачен")
    mutex_a.release()
    mutex_b.release()


# Создаем два потока
thread1 = threading.Thread(target=thread_a)
thread2 = threading.Thread(target=thread_b)

# Запускаем потоки
thread1.start()
thread2.start()

# Ждем завершения потоков
thread1.join()
thread2.join()
