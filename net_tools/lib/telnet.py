import telnetlib


class MyTelnet:
    def __init__(self):
        self.hostname = None
        self.password = None
        self.port = 23
        self.commands_file = None

    def connect(self, host, user, password, port=23):
        print 'starting telnet session'
        try:
            tn = telnetlib.Telnet(host)
            tn.read_until("login: ")
            tn.write(user + "\n")
            tn.read_until("Password: ")
            tn.write(password + "\n")
            tn.write("ls\n")
            tn.write("exit\n")

            print tn.read_all()

        except:
            print "telnet unable to connect to host"

if __name__ == '__main__':
    import sys

    telnet = MyTelnet()
    telnet.connect('baron.local', 'baron', 'voodoo')

    sys.exit()
