import threading
import subprocess


class PingHosts:
    def __init__(self):
        self.online_hosts = []

    def create_ping_threads(self, hosts):
        threads = []
        for h in hosts:
            th = threading.Thread(target=self.ping_host, args=(h,))
            th.start()
            threads.append(th)

        for th in threads:
            th.join()

    def ping_host(self, host):
        status = subprocess.call('ping -c 3 -q -n {0} &> /dev/null'.format(host), shell=True)
        if status == 0:
            self.online_hosts.append(host)

    def get_online_hosts(self):
        return self.online_hosts

    def print_online_host(self):
        if self.online_hosts:
            sorted_hosts = sorted(self.online_hosts, key=lambda ip: long(''.join(["%02X" % long(i) for i in ip.split('.')]), 16))
            for online_host in sorted_hosts:
                print online_host
        else:
            print "No online hosts in subnet"

if __name__ == '__main__':
    # base_ip = "10.0.10."
    # base_ip = "172.24.11."
    base_ip = "192.168.71."
    ip_list = [base_ip + str(oc) for oc in range(1, 255)]

    x = PingHosts()
    x.create_ping_threads(ip_list)
    # print x.get_online_hosts()
    x.print_online_host()
