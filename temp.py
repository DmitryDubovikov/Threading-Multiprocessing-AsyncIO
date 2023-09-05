import threading
import time

def background_task():
    for i in range(5):
        print("Задача в фоне: ", i)
        time.sleep(1)

if __name__ == "__main__":
    background_thread = threading.Thread(target=background_task)
    background_thread.daemon = True  # Устанавливаем флаг daemon, чтобы поток был потоком заднего плана
    background_thread.start()

    print("Основной поток завершил работу")
