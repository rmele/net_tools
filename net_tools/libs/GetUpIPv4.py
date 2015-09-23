import subprocess
import re


def get_all_local_ipv4():
    """
    Returns IP address(es) of current machine.
    :return: List of IP and Subnet tuples
    """
    # TODO: subprocess needs to handle resource busy or offline
    p = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
    ifc_resp = p.communicate()
    patt = re.compile(r'inet\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*netmask\s*(\w*)')
    resp = patt.findall(ifc_resp[0])
    return resp

if __name__ == '__main__':
    local_ips = get_all_local_ipv4()
    for host in local_ips:
        if host[0] == "127.0.0.1":
            pass
        else:
            print host


