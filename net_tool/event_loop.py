from Queue import Queue
import constants
import mem_dict as mem
# import utils as ut
import thread_cli
import thread_gui
from threading import Event

import time


class ClientEventLoop:
    def __init__(self):
        self.event_loop()
        self.hashmap = None
        self.actions = None
        self.programs = None

    def create_mem(self):
        self.hashmap = mem.MemDict()
        self.actions = self.hashmap.new()
        self.programs = self.hashmap.new()
        self.fill_mem_dict()

    def event_loop(self):
        self.create_mem()
        g = Queue()
        k = Queue()

        stop_cli = Event()
        th_cli = thread_cli.CliThread(stop_cli, k)
        th_cli.start()

        stop_gui = Event()
        th_gui = thread_gui.MyThread(stop_gui, g)
        th_gui.start()

        for i in range(5):
            g.put(i)

        time.sleep(5)
        print "Starting Event Loop:\n"
        while True:
            if not k.empty():
                print k.get()

            if not g.empty():
                print g.get()

            else:
                stop_gui.set()

        # this will stop the timer
        stop_cli.set()



    # def handle_keyboard_input(self):
    #     status = True
    #     action = ut.get_raw_input()
    #     # TODO: replace control c with action break character
    #     if action == "quit" or action == "control c":
    #         print "exiting!"
    #         status = False
    #     elif action in constants.ACTION_LIST:
    #         print "Action is in ACTION_LIST\n"
    #     else:
    #         print "Unknown action [{0}]\n".format(action)
    #         self.print_actions()
    #
    #     return status

        # try:
        #     if action.isdigit():
        #         print "num", action
        #     else:
        #         print action.lower()
        #
        # except AttributeError:
        #     print "unable to parse [{0}]".format(action)

    def format_menu_header(self, text):
        return "{0}  {1}  {2}".format("#" * 10, text, "#" * 10)

    def fill_mem_dict(self):
        for index, action in enumerate(constants.ACTION_LIST):
            self.hashmap.set(self.actions, index, action)

        for index, program in enumerate(constants.PROGRAM_LIST):
            self.hashmap.set(self.programs, index, program)

    def print_actions(self):
        print self.format_menu_header("Actions")

        for action in self.hashmap.list(self.actions):
            print "{0}. {1}".format(action[0], action[1])

        print "\n"

if __name__ == "__main__":
    ClientEventLoop()

