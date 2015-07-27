import sys
import getopt

# package imports
import net_tool
import event_loop


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    """
    :param argv: CLI options for script startup
    :return: Program Exit
    """
    if argv is None:
        argv = sys.argv
    try:
        try:
            options, remainder = getopt.getopt(argv[1:], 'ghl:i:v', ['gui', 'help', 'log=', 'input=', 'verbose'])
        except getopt.error, msg:
            raise Usage(msg)

        # Custom behavior starts here
        verbosity = False
        input_command = None
        output_filename = None
        gui = False

        for opt, arg in options:
            if opt in ('-i', '--input'):
                input_command = arg
            elif opt in ('-l', '--log'):
                output_filename = arg
            elif opt in ('-v', '--verbose'):
                verbosity = True
            elif opt in ('g', '--gui'):
                gui = True
            elif opt in ('-h', '--help'):
                print_menu()

        # print args from main(*args) execution
        if verbosity:
            spacing = '{0:16}'
            print ''
            print spacing.format('Options:'), options
            print spacing.format('Remainder:'), remainder

            if input_command:
                print spacing.format('Input Command:'), input_command
            else:
                print spacing.format('Input Command:'), "None"

            if output_filename:
                print spacing.format('Log File:'), output_filename
            else:
                print spacing.format('Log File:'), 'None'
            print ''

        # initial gui main page
        if not gui:
            try:
                event_loop.EventLoop()

            except Usage, err:
                print >> sys.stderr, err.msg

        else:
            # startup up GUI
            pass

    except Usage, err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"
        return 2


# def create_mem():
#     mem_struct = mem.MemDict()
#     actions = mem_struct.new()
#     mem_struct.set('actions', 0, 'quit')
#     mem_struct.set('actions', 1, 'menu')
#     return mem





if __name__ == "__main__":
    # used for basic command line usage
    sys.exit(main())

    # used for pycharm run usage
    # sys.exit(main(['', '--gui']))
    # sys.exit(main(['',  '-v']))
    # sys.exit(main(['', '-h', '--verbose', '-i foo', '-l file', '--gui']))



