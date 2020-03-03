# ch3/my_thread.py

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f'Starting thread {self.name}.')
        thread_count_down(self.name, self.delay)
        print(f'Finished thread {self.name}.')


def thread_count_down(name, delay):
    counter = 10
    while counter:
        time.sleep(delay)
        print(f'Thread {name} counting down: {counter}...')
        counter -= 1
