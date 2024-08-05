import requests
import time
import os
from plyer import notification
import ctypes

# URL для получения данных о количестве людей в очереди
regular_queue_url = "https://2b2t.io/api/queue"
priority_queue_url = "https://api.2b2t.dev/prioq"

def get_regular_queue():
    try:
        response = requests.get(regular_queue_url)
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            latest_queue_info = data[0]
            queue_size = latest_queue_info[1]
            return queue_size
        else:
            return None
    except Exception as e:
        print(f"An error occurred while fetching regular queue: {e}")
        return None

def get_priority_queue():
    try:
        response = requests.get(priority_queue_url)
        data = response.json()
        if isinstance(data, list) and len(data) >= 2:
            queue_size = data[1]
            return queue_size
        else:
            return None
    except Exception as e:
        print(f"An error occurred while fetching priority queue: {e}")
        return None

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Задание названия окна консоли
    ctypes.windll.kernel32.SetConsoleTitleW("2b2t queue")

    while True:
        clear_console()

        regular_queue_size = get_regular_queue()
        priority_queue_size = get_priority_queue()

        if regular_queue_size is not None:
            print(f"Regular Queue Size: {regular_queue_size}")
            if regular_queue_size < 40:
                notification.notify(
                    title="Очередь 2b2t",
                    message=f"Regular Queue is now {regular_queue_size} people.",
                    app_name="2b2t Queue Monitor",
                    timeout=10
                )
        else:
            print("Could not retrieve regular queue size")

        if priority_queue_size is not None:
            print(f"Priority Queue Size: {priority_queue_size}")
        else:
            print("Could not retrieve priority queue size")

        time.sleep(60)  # Пауза на 1 минуту перед следующим обновлением данных
