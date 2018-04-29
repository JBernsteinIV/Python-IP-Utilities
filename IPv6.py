 #For regex use of removing leading zeros in IPv6 address
import re
from InvalidAddressException import InvalidAddressException

class IPv6(InvalidAddressException):
    def __init__(self, address):
        self.address = address
        if self.address.find(":") == -1:
            raise InvalidAddressException("Invalid IPv6 Address.")
        else:
            if self.address.find("/") == -1:
                raise InvalidAddressException("Network bit specifier missing. Please include /num to address.")
            

    # Returns a shortened version of the IPv6 address.
    def shorten(self):
        if self.address.find(":0") != -1 or self.address.find("0:") != -1:
            self.shortened = re.sub('[^A-Z,a-z,^1-9,0]0+',":", self.address)
            #This statement literally exists to stop three colons in a row from appearing
            #Occurs in cases of IPv6 addresses with :0000:0000: interspersed inside.
            self.shortened = re.sub('(:::)', '::', self.shortened)
            return self.shortened
        else:
            return self.address
    # TODO: Convert IPv6 w/o padded zeros into IPv6 w/ padded zeros.
    # Returns an IPv6 address with the zeros included in the address.
    def lengthen(self):
        if self.address.find(":0") == -1 or self.address.find("0:") == -1:
            #Split the address into its segments
            self.address, self.delim, self.segments = self.address.partition(" ")
            self.address = self.address.split(":")
            #Pad any zeros into segments less than length of four
            #TODO: Break address into segments of four numbers between each colon
            tmp = ''
            for segment in self.address:
                if len(segment) < 4:
                    tmp = '0'.join(segment)
                    print(tmp)
            print(tmp)
            self.address = tmp
            return self.address
        else:
            return self.address

