from web3 import Web3  # Importing the Web3 library.
from ..Misc.logs import *  # Importing logs from the Misc directory.

class Contract(object):
    def __init__(self, web3, address, abi):
        """
        Initializes a new Contract object.

        Parameters:
        - web3 (Web3): An instance of the Web3 class for Ethereum blockchain interaction.
        - address (str): The address of the contract.
        - abi: The ABI (Application Binary Interface) of the contract.

        """
        self.contract = web3.eth.contract(
            address=address,
            abi=abi
        )

    def getBalance(self, address):
        """
        Function to get the balance of the given address from the contract.

        Parameters:
        - address (str): The address to get the balance for.

        Returns:
        - The balance of the given address from the contract.
        """
        return self.contract.functions.balanceOf(address).call()
