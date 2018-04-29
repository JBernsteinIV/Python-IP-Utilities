#Exception handler for invalid IP addresses and/or subnet masks.
#Possibly create a better exception handler in the future.
class InvalidAddressException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
