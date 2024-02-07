from web3 import Web3  # Importing the Web3 library.
from ..Misc.logs import *  # Importing logs from the Misc directory.

# Extracted Natice functions of ERC20 contract
    #interface IERC20 {
    #    event Approval(address indexed owner, address indexed spender, uint value);
    #    event Transfer(address indexed from, address indexed to, uint value);
    #
    #   function name() external view returns (string memory);
    #   function symbol() external view returns (string memory);
    #   function decimals() external view returns (uint8);
    #   function totalSupply() external view returns (uint);
    #   function balanceOf(address owner) external view returns (uint);
    #   function allowance(address owner, address spender) external view returns (uint);

    #    function approve(address spender, uint value) external returns (bool);
    #    function transfer(address to, uint value) external returns (bool);
    #    function transferFrom(address from, address to, uint value) external returns (bool);
    #}

# VScode Blockscan : https://vscode.blockscan.com/polygon/0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32

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
    def getAllowance(self, owner, spender):
        """
        Function to get the amount allowed to to be use on owner balance by a address (spender)

        Parameters:
        - owner (str): The address of the the balance owner
        - spender (str): The address of the spender (most of the time a Smart Contract)

        Returns:
        - The amount allowed to to be use on owner balance by a address (spender) 
        """
        return self.contract.functions.allowance(owner, spender).call()
    def getBalance(self, address):
        """
        Function to get the balance of the given address from the contract.

        Parameters:
        - address (str): The address to get the balance for.

        Returns:
        - The balance of the given address from the contract.
        """
        return self.contract.functions.balanceOf(address).call()
