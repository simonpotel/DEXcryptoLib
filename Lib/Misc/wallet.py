from ..Misc.logs import *

class Wallet(object):
    """
    Class to declare all your wallets with address and private key.
    """
    def __init__(self, address, privatekey):
        """
        Initialize a new Wallet object with the provided address and private key.

        Parameters:
        - address (str): The wallet address.
        - privatekey (str): The private key associated with the wallet.
        """
        self.address = address
        self.privatekey = privatekey
        log("debug", "Wallet object has been created : " + str(self) + " address: " + address + " Privatekey: " + str(privatekey != None))
