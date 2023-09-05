import threading

from count_three_sum import count_three_sums, read_ints

if __name__ == "__main__":
    print("starting main")

    ints = read_ints("1Kints.txt")

    print(ints)

    # ВАРИАНТ 1: мэйн луп полностью заблокирован
    # count_three_sums(ints)

    # ВАРИАНТ 2: освобождаем мэйн луп
    # # foreground thread: не завершается даже когда основной поток main завершился
    # new_thread = threading.Thread(target=count_three_sums, args=(ints,))
    # new_thread.start()

    # ВАРИАНТ 3: освобождаем мэйн луп
    # background thread: нужно добавить new_thread.join()
    new_thread = threading.Thread(target=count_three_sums, args=(ints,), daemon=True)
    new_thread.start()

    print("--- inside main --")

    new_thread.join()

    print("ending main")
