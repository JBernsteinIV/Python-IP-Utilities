"""
TODOS:
 -> Check validation of IP addresses so invalid subnets are caught.
    -> Example: .250 is not a valid subnet mask.
 -> Implement IPv6 class
 -> Allow shortened IPv6 addresses to be used in both the IPv6 class's constructor and the IP
    wrapper function.
 -> Make IPv4 and IPv6 child classes of IP class. Possibly make IP into an abstract base class
    but that will require importing abc for Abstract Base Class module.
 -> Possibly remove exceptions and just return -1 on failure?
 -> Separate out functions and classes into distinct modules. Recompose later in final utility build.
 -> Check amount of possible host addresses. Fix bugs here!
"""

"""
DEPENDENCIES:
 -> re for Regex
 -> binascii for binary of IPv6 (possibly remove later)
"""

"""
LICENSE:
This Python utility is licensed under the MIT license.
Copyright 2018 John L. Bernstein IV (github.com/user/JBernsteinIV)
"""

import re #For regex use of removing leading zeros in IPv6 address
from InvalidAddressException import InvalidAddressException

#Converts CIDR suffix to appropriate subnet mask:
#/0  = 0.0.0.0
#/1  = 128.0.0.0
#/8  = 255.0.0.0
#...
#/32 = 255.255.255.255
class IPv4(InvalidAddressException):
    #Variable Length Subnet Mask
    vlsm = {
             '0' : "0.0.0.0",        '1' : "128.0.0.0",      '2' : "192.0.0.0",
             '3' : "224.0.0.0",      '4' : "240.0.0.0",      '5' : "248.0.0.0",
             '6' : "252.0.0.0",      '7' : "254.0.0.0",      '8' : "255.0.0.0",
             '9' : "255.128.0.0",    '10': "255.192.0.0",    '11': "255.224.0.0",
             '12': "255.240.0.0",    '13': "255.248.0.0",    '14': "255.252.0.0",
             '15': "255.254.0.0",    '16': "255.255.0.0",    '17': "255.255.128.0",
             '18': "255.255.192.0",  '19': "255.255.224.0",  '20': "255.255.240.0",
             '21': "255.255.248.0",  '22': "255.255.252.0",  '23': "255.255.254.0",
             '24': "255.255.255.0",  '25': "255.255.255.128",'26': "255.255.255.192",
             '27': "255.255.255.224",'28': "255.255.255.240",'29': "255.255.255.248",
             '30': "255.255.255.252",'31': "255.255.255.254",'32': "255.255.255.255"
            }
    def __init__(self, address):
        self.address = address
        #Check that the IPv4 address has attached with it a subnet mask OR
        #a CIDR suffix to indicate the subnet mask for the IP address.
        if self.address.find("/") != -1:
            self.address, self.delim, self.mask = self.address.partition("/")
            self.mask = self.vlsm[self.mask]
        elif self.address.find(" ") != -1:
            self.address, self.delim, self.mask = self.address.partition(" ")
        else:
            raise InvalidAddressException("IPv4 address must contain an appropriate subnet mask OR CIDR suffix (e.g. /24)")
        #Check that the IP address is valid.
        self.address = self.address.split(".")
        for octet in range(0,4):
            if int(self.address[octet]) < 0 or int(self.address[octet]) > 255:
                raise InvalidAddressException("IPv4 address must be between 0 and 255.")
        #If the IP address is valid, recompose self.address into a string
        self.address = ".".join(self.address)
        #Check that the subnet mask is valid as well.
        self.mask = self.mask.split(".")
        for octet in range(0,4):
            if int(self.mask[octet]) < 0 or int(self.mask[octet]) > 255:
                raise InvalidAddressException("Subnet mask must be between 0 and 255.")
        #Same as before, recompose to string if it is valid
        self.mask = ".".join(self.mask)
