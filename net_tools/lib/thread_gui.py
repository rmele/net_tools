from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, event, the_q):
        Thread.__init__(self)
        self.stopped = event
        self.pulse_time = 0.5
        self.q = the_q

    def run(self):
        i = 0
        while not self.stopped.wait(self.pulse_time):
            time.sleep(5)
            i += 1
            # print "my thread", self.q
            self.q.put(str(i))


if __name__ == "__main__":
    stopFlag = Event()
    thread = MyThread(stopFlag, q)
    thread.start()

    # this will stop the timer
    stopFlag.set()
