"""
Basic tools to calculate IP ranges based on Subnet Masking
"""


def is_valid_ipv6(ip):
    pass


def is_valid_ipv4(ip):
    """
    Check if ip meets basic validity criteria
    :param ip: string of dotted decimal ip address, eq '123.456.789.0'
    :return: Return True is ip is valid else False
    """
    try:
        octets = ip.split('.')
        if len(octets) == 4 and \
                1 <= int(octets[0]) <= 223 and \
                int(octets[0]) != 127 and \
                (int(octets[0]) != 169 or int(octets[1]) != 254) and \
                0 <= int(octets[1]) <= 255 and \
                0 <= int(octets[2]) <= 255 and \
                0 <= int(octets[3]) <= 255:
            return True
        
        else:
            return False
            
    except:
        return False
        

def is_valid_subnet(subnet):
    """
    Check if subnet mask meets basic validity criteria
    :param subnet:  string of dotted decimal ip address, eq '255.255.255.0'
    :return: Return True if subnet is valid else False
    """
    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
    try:
        octets = subnet.split('.')
        if len(octets) == 4 and \
                int(octets[0]) == 255 and \
                int(octets[1]) in masks and \
                int(octets[2]) in masks and \
                int(octets[3]) in masks and \
                (int(octets[0]) >= int(octets[1]) >= int(octets[2]) >= int(octets[3])):
            return True
        else:
            return False

    except:
        return False


def hex_to_num(val):
    return int(val, 16)


def dotted_decimal_to_num(dd):
    """
    Convert dotted decimal IP to integer number
    :param dd:
    :return:
    """
    val = 0
    octets = dd.split('.')
    for num in octets:
        val = (val << 8) + int(num)
    return val


def num_to_dotted_decimal(val):
    dd = ''
    for i in range(4):
        x = val & 255
        val >>= 8
        if i > 0:
            dd = "." + dd
        dd = str(x) + dd
    return dd


def count_bits(val, t):
    cnt = 0
    for i in range(32):
        x = val & 1
        val >>= 1
        if x == t:
            cnt += 1
    return cnt


def subnet_calc(ip, subnet):
    """

    :param ip: dotted decimal formatted IPv4 Address
    :param subnet: dotted decimal formatted subnet mask
    :return: network_address, wildcard_mask, broadcast_address, host_bits, possible_hosts
    """
    network_address = num_to_dotted_decimal(dotted_decimal_to_num(ip) & dotted_decimal_to_num(subnet))
    wildcard_mask = num_to_dotted_decimal(~ dotted_decimal_to_num(subnet))
    broadcast_address = num_to_dotted_decimal(dotted_decimal_to_num(network_address) | dotted_decimal_to_num(wildcard_mask))
    # TODO host bits should not return value of -1 if subnet is all 255.255.255.255
    host_bits = count_bits(dotted_decimal_to_num(subnet), 0)
    possible_hosts = (2 ** host_bits) - 2
    return network_address, wildcard_mask, broadcast_address, host_bits, possible_hosts

if __name__ == '__main__':
    import sys
    my_ip = '192.168.5.5'
    my_subnet = '255.255.255.224'

    if is_valid_ipv4(my_ip) and is_valid_subnet(my_subnet):
        the_network_address, the_possible_hosts, the_broadcast_address, the_wildcard_mask, the_host_bits = subnet_calc(my_ip, my_subnet)

        # print statements
        padding = 40
        print "\n" + "=" * padding
        print "{0:20}{1}".format("User IP:", my_ip)
        print "{0:20}{1}".format("Subnet Mask:", my_subnet)
        print "{0:20}{1}".format("Network Address:", the_network_address)
        print "{0:20}{1}".format("Possible Hosts:", the_possible_hosts)
        print "{0:20}{1}".format("Broadcast Address:", the_broadcast_address)
        print "{0:20}{1}".format("Wildcard Mask:", the_wildcard_mask)
        print "{0:20}{1}".format("Mask Bits:", the_host_bits)
        print "=" * padding + "\n"
    else:
        print "Invalid parameters: [{0}] [{1}]".format(my_ip, my_subnet)

    sys.exit()

