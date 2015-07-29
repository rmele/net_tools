import Queue
import constants
import mem_dict as mem
import utils as ut


class EventLoop:
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
        print "Starting Event Loop:\n"
        self.create_mem()

        while True:
            handled = self.handle_keyboard_input()
            if not handled:
                break
            else:
                pass

    def handle_keyboard_input(self):
        status = True
        action = ut.get_raw_input()
        # TODO: replace control c with action break character
        if action == "quit" or action == "control c":
            print "exiting!"
            status = False
        elif action in constants.ACTION_LIST:
            print "Action is in ACTION_LIST\n"
        else:
            print "Unknown action [{0}]\n".format(action)
            self.print_actions()

        return status

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
    EventLoop()

