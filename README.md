# Python-Parcels
Assortment of Python files

This is an assortment of small IP utility classes I created. The IP utilities allow a string to be read in that will check for IPv4 or IPv6 syntax. If an incorrect string is read in, currently an error handling class is used but in future installments this will likely be taken out (the error handler was mostly to ensure each of the utility functions like network() and broadcast() worked appropriately).

# IP.py - Wrapper class

The IP.py file specifies a wrapper class called IP that will take in a string and check if it's a valid IPv4 or IPv6 address. If it is not, it will throw an error. If a valid IPv4 or IPv6 address is read in from the string, the IP class will pass the string into the appropriate IPv4 or IPv6 constructor.

# IPv4.py - IPv4 class and utility functions

The IPv4.py file defines the IPv4 class and works for both CIDR notation (e.g. 192.168.1.1/24) and for subnet specifications (e.g. 192.168.1.1 255.255.255.0). The IPv4.py file also contains some utility functions for the class, such as a utility function to return the range of available host addresses, the network address of the appropriate subnet, and the broadcast address of the appropriate subnet.

# IPv6.py - IPv6 class and utility functions

The IPv6.py file defines the IPv6 class and allows for both lengthened and shortened IPv6 addresses to be used (e.g. 2001:db8:1::ab9:C0A8:102/64 [shortened] vs. 2001:0db8:0001:0000:0000:0ab9:C0A8:0102/64 [lengthened]). Currently some work needs to be done to ensure the network bit (/XX) is working appropriately. Also some work still needs to be done to check for IPv6 dual address channels (IPv6 addresses that can be converted into IPv4 addresses and vice versa). 

# InvalidAddressException.py - Basic error handler

The InvalidAddressException.py file is just a small exception handler. This was just for some testing purposes and should be removed.

# Test_IP.py - Driver 

Test_IP.py is a simple test program to verify the IP wrapper class , IPv4, IPv6, and the utility functions were all working appropriately.
