from IP import *

if __name__ == "__main__":
    #Example test case with generic IPv4 address and subnet mask specified.
    ipv4 = IP("192.168.1.1 255.255.255.0")
    print(ipv4)
    #IPv4 address using CIDR notation
    cidrNotation = IP("192.168.1.2 /24")
    print(cidrNotation)
    print("Network:", network(cidrNotation))
    print("Broadcast:", broadcast(cidrNotation))
    print("Host range:", hostRange(cidrNotation))
    print("hostsAvailable:", hostsAvailable(cidrNotation))
    #With an IPv6 address
    print("With IPv6")
    ipv6 = IP("2001:0db8:0001:0000:0000:0ab9:C0A8:0102 /64")
    print("Shortened:",ipv6.shorten())
    print("With shortened IPv6")
    shortenedIPv6 = IP("2001:db8:1::ab9:C0A8:102 /64")
    print("Lengthened:",shortenedIPv6.lengthen())
    
