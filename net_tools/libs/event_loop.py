from Queue import Queue
import constants
import mem_dict as mem
import thread_cli
import thread_gui
from threading import Event


class ClientEventLoop:
    def __init__(self):
        self.hashmap = None
        self.actions = None
        self.programs = None
        self.event_loop()

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

        # for i in range(5):
        #     g.put(i)

        print "Starting Event Loop:\n"
        self.print_actions()
        while True:
            cmd = ""
            if not k.empty():
                cmd = k.get()

            if not g.empty():
                cmd = g.get()

            if cmd:
                if cmd == "quit" or cmd == "0":
                    print "exiting threads!"

                    # this will stop the timer
                    stop_cli.set()
                    stop_gui.set()
                    break

                elif cmd in constants.ACTION_LIST:
                    print cmd, "is in action list"

                elif cmd in constants.PROGRAM_LIST:
                    print cmd, "is in program list"

                else:
                    print "Unknown action [{0}]\n".format(cmd)
                    self.print_actions()

    def format_menu_header(self, text):
        return "{0}  {1}  {2}".format("#" * 10, text, "#" * 10)

    def fill_mem_dict(self):
        for index, action in enumerate(constants.ACTION_LIST):
            self.hashmap.set(self.actions, index, action)

        for index, program in enumerate(constants.PROGRAM_LIST):
            self.hashmap.set(self.programs, index, program)

    def print_programs(self):
        print self.format_menu_header("Programs")

        for program in self.hashmap.list(self.programs):
            print "{0}. {1}".format(program[0], program[1])

        print "\n"

    def print_actions(self):
        print self.format_menu_header("Actions")

        for action in self.hashmap.list(self.actions):
            print "{0}. {1}".format(action[0], action[1])

        print "\n"

if __name__ == "__main__":
    ClientEventLoop()

