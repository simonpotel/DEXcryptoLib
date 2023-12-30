from ..Misc.logs import *  # Importing logs from the Misc directory.
from web3 import Web3  # Importing the Web3 library.

class Network(object):
    def __init__(self, network):
        """
        Initializes a new Network object.

        Parameters:
        - network (str): The URL of the node for the desired network.

        """
        self.web3 = Web3(Web3.HTTPProvider(network))
        log("web3", "Network object has been created : " + str(self) + " connected: " + str(self.web3.is_connected()))

    def getStateWeb3(self):
        """
        Function to check the connection state of the Web3 instance.

        Returns:
        - True if Web3 is connected, False otherwise.
        """
        return self.web3.is_connected() == True
