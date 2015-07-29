import subprocess
import os
import sys
import re


##############################
# User input handlers
##############################
def tab_to_spaces(text):
    new_text = re.sub(r"\t+", " ", text)
    if new_text:
        return new_text
    else:
        return None


def spaces_to_columns(text):
    new_line = re.sub(r"\t+", " ", text)
    new_text = new_line.split("\n")
    for line in new_text:
        print re.sub(r"\s+", "", "{0:>20}".format(line))
    #     new_line = re.sub(r"\t+", " ", line)
    #     newer_line = new_line.split("\s")
    #     # for col in newer_line:
    #     print "{0:20} :)".format(newer_line)


def format_line(one_line):
    return one_line

def get_raw_input():
    string_var = raw_input("Input Text:\n")
    if string_var:
        return string_var
    else:
        return get_raw_input()


def get_integer():
    int_var = raw_input("Input Number:\n")
    if int_var.isdigit():
        return int(int_var)
    else:
        return get_integer()


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
def read_file_to_list(which_file):
    try:
        with open(which_file, 'r') as f:
            my_file = [words for words in f]
        f.close()
        return my_file
    except:
        return None


def write_file(which_file, text):
    try:
        with open(which_file, 'w') as f:
            for line in text:
                f.write(line)
            f.close()
    except:
        print "unable to write file"


def append_file(which_file, text):
    try:
        with open(which_file, 'a') as f:
            for line in text:
                f.write(line)
            f.close()
    except:
        print "unable to append file"


##############################
# Utilities based around checking python environment
##############################
def check_py_environ():
    """
    Method to print Python Interpreter values
    """
    print "\n" + "#" * 10 + " Python Environment " + "#" * 10 + "\n"
    print "\n".join([param + ":\n\t" + os.environ[param] + "\n" for param in os.environ])


def check_path():
    """
    Method to print paths included in PYTHONPATH
    """
    print "'\n".join([a_path for a_path in sys.path])


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


if __name__ == "__main__":
    # write_file('test', ['this\nis some\ntext\n\nyep'])
    # append_file('test', ['here\nare my\nbig words'])
    # print "".join(read_file_to_list('test'))

    # check_py_environ()
    # check_version()

    # print tab_to_spaces("\n\t\t\t\t\twords\tare\n\tmy\t\t\tfavorite\n")
    spaces_to_columns(("words\tare\nmy\t\t\tfavorite\n"))

    # print get_raw_input()

    # print get_integer()

    # print print_matrix(5, 4)
