from InvalidAddressException import InvalidAddressException
from IPv4 import IPv4
from IPv6 import IPv6
#Wrapper for IPv4 and IPv6 objects.
def IP(address):
    try:
        if address.find(".") != -1:
            return IPv4(address)
        if address.find(":") != -1:
            return IPv6(address)
    except InvalidAddressException:
        raise InvalidAddressException("Invalid IP address")

#Finds the network address of the provided host address.
def network(address):
    try:
        if isinstance(address,IPv4):
            addr = address.address.split(".")
            mask = address.mask.split(".")
            netAddr = []
            #Bitwise AND each octet together to get the network address.
            for octet in range(0,4):
                netAddr.append(str(int(addr[octet]) & int(mask[octet])))
            netAddr = ".".join(netAddr)
            return netAddr
            
    except InvalidAddressException:
        raise InvalidAddressException("Invalid IP address")

#Find the broadcast address of the provided host address.
def broadcast(address):
    try:
        if isinstance(address,IPv4):
            addr = address.address.split(".")
            mask = address.mask.split(".")
            netAddr = []
            #Bitwise AND each octet together to get the network address.
            for octet in range(0,4):
                if int(mask[octet]) == 255:
                    netAddr.append(addr[octet])
                elif int(mask[octet]) == 0:
                    netAddr.append(str(255))
                else:
                    netAddr.append(str(256 - (int(mask[octet]) + 1)))
            netAddr = ".".join(netAddr)
            return netAddr
        
    except InvalidAddressException:
        raise InvalidAddressException("Invalid IP address")


def hostRange(address):
    first = network(address)
    last  = broadcast(address)
    #Parse the string from the network address, add one for the first host.
    first = first.split(".")
    first[3] = int(first[3]) + 1
    first[3] = str(first[3])
    first = ".".join(first)
    #Parse the string from the broadcast address, subtract one for the last host.
    last = last.split(".")
    last[3] = int(last[3]) - 1
    last[3] = str(last[3])
    last = ".".join(last)
    return first + " - " + last

#TODO: Currently incorrect - Does not go above 254 available hosts. FIX.
def hostsAvailable(address):
    netAddr = network(address)
    broadcastAddr = broadcast(address)
    netAddr = netAddr.split(".")
    broadcastAddr = broadcastAddr.split(".")
    ctr = 0
    for octet in range(0,4):
        if str(int(netAddr[octet]) & int(broadcastAddr[octet])) == netAddr[octet]:
            ctr = int(broadcastAddr[octet]) - int(netAddr[octet]) - 1
    return ctr
