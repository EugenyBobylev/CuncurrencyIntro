# ch3/example4.py
import logging
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        logging.info('Starting thread %s.' % self.name)
        thread_lock.acquire()
        thread_count_down(self.name, self.delay)
        thread_lock.release()
        logging.info('Finished thread %s.' % self.name)


def thread_count_down(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)
        logging.info('Thread %s counting down: %i...' % (name, counter))
        counter -= 1


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S ")
    thread_lock = threading.Lock()

    logging.info("Start")
    thread1 = MyThread('A', 0.5)
    thread2 = MyThread('B', 0.5)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    logging.info('Finished.')
