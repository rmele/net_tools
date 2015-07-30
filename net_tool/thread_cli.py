from threading import Thread
import utils as ut


class CliThread(Thread):
    def __init__(self, event, the_q):
        Thread.__init__(self)
        self.stopped = event
        self.pulse_time = 0.5
        self.q = the_q

    def run(self):
        while not self.stopped.wait(self.pulse_time):
            print self.q
            self.q.put(self.handle_keyboard_input())

    def handle_keyboard_input(self):
        return ut.get_raw_input()

