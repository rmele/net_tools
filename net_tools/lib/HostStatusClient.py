import sys
import threading
from datetime import datetime
import time

# package imports
import ssh
import ResolveDNS
import ReadFileSelection
import WriteFolderDialog
import ThreadedPing


class HostStatusClient:
    def __init__(self):
        self._count = 0
        self._connection = None
        self._hosts = None
        self._port = 22
        self._user = None
        self._pass = None
        self._cmds = None

    def main(self):
        try:
            hosts = None
            filt_hosts = None
            fp = self.get_file_path()
            if fp is not None:
                hosts = self.file_to_list(fp)

                if hosts:
                    filt_hosts = filter(None, hosts)

                else:
                    print "Unable to parse hosts file [{0}], exiting ...".format(hosts)
                    sys.exit()

            else:
                print "No Hosts file supplied, exiting ..."
                sys.exit()

            if filt_hosts:
                ip_list = [host.split(" ", 1)[0] for host in filt_hosts]
                print "Staring threaded ping to the following hosts: ", ip_list
                potential_hosts = ThreadedPing.PingHosts()
                potential_hosts.create_ping_threads(ip_list)
                checked_hosts = potential_hosts.get_online_hosts()

                # TODO: improve host name resolution
                for host in checked_hosts:
                    print "\n"
                    # print ResolveMdns.getIP(host)
                    # print ResolveMdns.getIPx(host)
                    # print ResolveMdns.getHost(host)
                    print ResolveDNS.getAlias(host)

                # TODO: improve comparison of ip list. Needs to support dd and .local
                if len(checked_hosts) == len(filt_hosts):
                    self._cmds = self.file_to_list(self.get_file_path())
                    if self._cmds:
                        time.sleep(1)
                        self.create_ssh_threads(filt_hosts)
                    else:
                        print "No Commands file supplied, exiting ..."
                        sys.exit()

                else:
                    print "not all host online, recheck connections"

            else:
                "Unable to parse hosts file"

        except KeyboardInterrupt:
            print "\nKeyboard Interrupt!\nexiting..."

    def get_file_path(self):
        try:
            path = ReadFileSelection.SelectReadFileDialog().main()
            return path

        except:
            return None

    def get_folder_path(self):
        return WriteFolderDialog.SelectWriteFolderDialog()

    def write_file(self, which_file, text):
        try:
            with open(which_file, 'w') as f:
                for line in text:
                    f.write(line)
        except TypeError:
            print "unable to write file:\t", which_file

    def file_to_list(self, fp):
        """

        :param fp: File to be split at each new line character '\n'
        :return: list with each item as a line of the file
        """
        try:
            with open(fp, 'r') as f:
                params = [var.replace("\n", "") for var in f]
            return params
        except IOError:
            return None

        except TypeError:
            return None

    def create_ssh_threads(self, hst):
        write_path = self.get_file_path()
        if write_path:
            threads = []
            for host in hst:
                th = threading.Thread(target=self.connect_and_query, args=(host, write_path))
                th.start()
                threads.append(th)

            for th in threads:
                th.join()

        else:
            print "No file write path supplied, exiting ..."
            sys.exit()

    def connect_and_query(self, host, write_path, port=22):
        write_contents = []
        hostname, username, password = host.split(' ')

        connection = ssh.MySSH()
        connection.set_verbosity(False)
        connection.connect(hostname=hostname,
                           username=username,
                           password=password,
                           port=port)

        print "opening SSH to %s ..." % hostname
        if connection.connected() is False:
            print 'ERROR: connection failed.'
            sys.exit(1)
        else:
            for command in self._cmds:
                content = '\n' + '=' * 64
                content += '\ncommand: %s' % command
                status, output = connection.run(command, None)
                content += '\nstatus : %d' % status
                content += '\noutput : %d bytes' % len(output)
                content += '\n' + '=' * 64
                content += '\n%s' % output
                write_contents.append(content)

            path = write_path + '/' + hostname + '_' + str(datetime.now()).split('.')[0].replace(' ', '_') + '.txt'
            print "File written to [{0}]".format(path)
            self.write_file(path, write_contents)

        print "closing SHH to %s ..." % hostname


if __name__ == '__main__':
    HostStatusClient().main()
    sys.exit()
