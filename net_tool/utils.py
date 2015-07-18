import subprocess
import os
import sys


##############################
# User input handlers
##############################
def tab_to_spaces(text):
    pass


def spaces_to_tab(text):
    pass


def get_raw_input():
    string_var = raw_input("Input Text:\n")
    return string_var


def get_integer():
    # TODO: returns None incorrectly
    int_var = raw_input("Input Number:\n")
    if int_var.isdigit():
        return int(int_var)
    else:
        get_integer()


def print_matrix(x=16, y=16):
    spacing = '{0: 4}'
    holder = ""
    for col in range(y):
        for row in range(x):
            holder += spacing.format(row+1)
        holder += "\n"
    if holder:
        print holder


##############################
# Utilities based around actual files
##############################
def read_file(which_file):
    try:
        text = ""
        with open(which_file, 'r') as f:
            for line in f:
                text += line
            f.close()
        return text

    except:
        return None


def write_file(which_file, text):
    try:
        with open(which_file, 'w') as f:
            for line in text:
                f.write(line)
            f.write('\n')
            f.close()

        return

    except:
        return


# TODO: Append currently will only replace text, need to move to end of file and add new content
def append_file(which_file):
    try:
        with open(which_file, 'w') as f:
            f.seek(-1)
            f.write('text added by append_file function')
            f.close()

        return

    except:
        return


##############################
# Utilities based around checking python environment
##############################
def check_py_environ():
    """
    Method to print Python Interpreter values
    """
    for param in os.environ.keys():
        print param, os.environ[param]


def check_path():
    """
    Method to print paths included in PYTHONPATH
    """
    for a_path in sys.path:
        print a_path


def check_version():
    """
    Method to print current VERSION of Python interpreter
    """
    print sys.version


##############################
# Interact with BASH shell
##############################
def py_to_shell(cmd_list):
    """
    :param cmd_list: list containing a Command and Flags for the command
    :return: output of shell command
    """
    p = subprocess.Popen(cmd_list, shell=True, stdout=subprocess.PIPE,)
    return p


def shell_to_shell(cmd_list, prev_output):
    """
    :param cmd_list: list containing Output from Previous shell command
    :return: Output of Instance from current shell command
    """
    p = subprocess.Popen(cmd_list, stdin=prev_output.stdout, stdout=subprocess.PIPE,)
    return p


def handle_shell_output(output):
    """
    :param output: Instance of shell command
    :return: string value of shell command instance
    """
    return output.stdout.read().strip()


def interact_with_shell(case):
    """
    :param case: String containing a shell command
    :return: None
    """
    print handle_shell_output(py_to_shell(case))
