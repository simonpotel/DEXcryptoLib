from web3 import Web3
from ...Misc.logs import *  # Importing logs from the Misc directory.

class Matic(object):
    """
    Class Matic permits interaction with the native token of the Polygon chain: MATIC.
    """
    def __init__(self, web3, address=None, privatekey=None):
        """
        Initializes a new Matic object.

        Parameters:
        - web3 (Web3): An instance of the Web3 class for Ethereum blockchain interaction.
        - address (str): The address associated with your wallet.
        - privatekey (str): The private key associated with your wallet.
        """
        self.web3 = web3
        self.address = address
        self.privatekey = privatekey
        log("debug", "Matic object has been created : " + str(self) + " address: " + address + " Privatekey: " + str(privatekey != None))
    def getBalance(self):
        """
        Function to get the MATIC balance of the address set in the class.

        Returns:
            0 - The balance value in ether (type: int/float).
            1 - The balance value in wei (type: int).
        """
        if not self.address: return 0
        amount = self.web3.eth.get_balance(self.address)
        return (self.web3.from_wei(amount, 'ether'), amount)
