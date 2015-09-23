# package imports
import GetUpIPv4
import SubnetCalc
import ThreadedPing


class LocalNetworkScan:
    def __init__(self):
        pass

    def main(self):
        all_ips = []
        ips = self.find_local_ipv4()
        for ip in ips:
            ip_list = self.local_ip_to_ips(ip)
            found_ips = self.find_network_ips(ip_list)
            all_ips.append(found_ips)
        return all_ips

    def find_local_ipv4(self):
        ips = GetUpIPv4.get_all_local_ipv4()
        ex_ips = []
        for ip in ips:
            if ip[0] == "127.0.0.1":
                pass
            else:
                ex_ips.append(ip)
        return ex_ips

    def local_ip_to_ips(self, ip):
        ip_list = []
        subnet_mask = SubnetCalc.num_to_dotted_decimal(SubnetCalc.hex_to_num(ip[1]))
        net, wild, bcast, m_bits, p_hosts = SubnetCalc.subnet_calc(ip[0], subnet_mask)
        x = SubnetCalc.dotted_decimal_to_num(net)
        for i in range(p_hosts + 1):
            z = i + x
            ip_list.append(SubnetCalc.num_to_dotted_decimal(z))

        return ip_list

    def find_network_ips(self, ips):
        x = ThreadedPing.PingHosts()
        x.create_ping_threads(ips)
        return x.get_online_hosts()

if __name__ == '__main__':
    # TODO: modify to return without pretty print to pass to other scripts
    print "\nStarting threaded ping to potential hosts ...\n"
    my_net = LocalNetworkScan()
    print "\nOnline Hosts:"
    print "=" * 50
    ips = my_net.main()
    for interface in ips:
        print "\nTotal IPs in subnet:", len(interface)
        print "=" * 25
        for ip in interface:
            print ip
