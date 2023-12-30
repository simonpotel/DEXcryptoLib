from .constants import *  # Importing constants from the same directory.
from ..Misc.logs import *  # Importing logs from the Misc directory.
import time  # Importing the time module.

class Quickswap(object):
    """
    Class to interact with the Quickswap router.
    """
    def __init__(self, web3, contract, address, privatekey):
        """
        Initializes a new Quickswap object.

        Parameters:
        - web3 (Web3): An instance of the Web3 class for blockchain interaction.
        - contract: The Quickswap contract from the Web3 network.
        - address (str): The address associated with the wallet.
        - privatekey (str): The private key associated with the wallet.

        """
        self.web3 = web3  # Web3 from Web3.network
        self.contract = contract  # Contract of Quickswap from Web3.network
        self.address = address  # Address of your wallet
        self.privatekey = privatekey  # Private key of your wallet
        log("routers", "Quickswap object has been created : " + str(self) + " wallet_address: " + address + " wallet_privatekey: " + str(privatekey != None) + " contract: " + str(contract))
    def Approve(self, tokenContract, amount):
        """
        Function to approve Quickswap to spend a specific amount of tokens from the given contract.

        Parameters:
        - tokenContract: The contract of the token to be approved.
        - amount (int): The amount of tokens to approve.

        Returns:
        - Tuple containing the transaction hash and status.
        """
        log("routers", "Quickswap Approve(" + str(tokenContract) + ", " + str(amount) + ")")

        gas = 600000  # Gas fees
        nonce = self.web3.eth.get_transaction_count(self.address, 'pending')  # Taking Pending instead of classic
        # Several transactions can be sent at the same time without error.
        tx_approve = tokenContract.functions.approve(
            spender=aQuickswap,  # Enable Quickswap router to take x amount of my wallet
            amount=int(amount)  # Amount in wei (1 USDT = 10**6 = 1000000) (with decimals)
        ).build_transaction({
            'nonce': nonce,  # Number of transactions (current amount + pending + 1)
            'gas': gas,  # Gas to use
            'gasPrice': self.web3.eth.gas_price  # Public API function to determine gas price
        })
        log("routers", "Quickswap tx_approve: " + str(tx_approve))
        signed_approve_tx = self.web3.eth.account.sign_transaction(tx_approve, self.privatekey)  # Sign the approve using private_key
        tx_approve_transaction = self.web3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)  # Send transaction on blockchain
        receipt_approve = self.web3.eth.wait_for_transaction_receipt(tx_approve_transaction)  # Function to wait until nonce gets +1
        log("routers", "Quickswap transactionHash: " + receipt_approve["transactionHash"].hex() + " receipt_approve : " + str(receipt_approve))
        return tx_approve_transaction, receipt_approve["status"]  # Return (hash, status) of the transaction
    def getAmountMin(self, amount, path):
        """
        Function to get the minimum amount required for a swap.

        Parameters:
        - amount: The amount to be swapped.
        - path: The path of the tokens in the swap.

        Returns:
        - The minimum amount needed for the swap.
        """
        result = int(amount)
        for i in range(len(path)-1):
            result = self.contract.functions.getAmountsOut(result, [path[i]] + [path[i+1]]).call()[1]
        return result
    def SwapExactTokensForTokens(self, amount, path, receiver_address, amountOutMin):
        """
        Function to swap a specific amount of tokens for another using Quickswap.

        Parameters:
        - amount: The amount of tokens to be swapped.
        - path: The path of the tokens in the swap.
        - receiver_address: The address to receive the swapped tokens.
        - amountOutMin: The minimum amount of tokens expected in return.

        Returns:
        - Tuple containing the transaction hash and status.
        """
        log("routers", "Quickswap SwapExactTokensForTokens(" + str(amount) + ", " + str(path) + ", " + str(receiver_address) + ", " + str(amountOutMin) + ")")

        nonce = self.web3.eth.get_transaction_count(self.address, 'pending')
        swap_transaction_tx = self.contract.functions.swapExactTokensForTokens(
            int(amount),
            int(amountOutMin),
            path,
            receiver_address,
            int(time.time()) + 60 * 10  # uint deadline (10 mins)
        ).build_transaction({
            'chainId': 137,
            'nonce': nonce,
            'gas': 600000,
            'gasPrice': self.web3.eth.gas_price
            # 'value': self.web3.to_wei(1, "ether")
        })
        log("routers", "Quickswap swap_transaction_tx: " + str(swap_transaction_tx))
        sign_transaction = self.web3.eth.account.sign_transaction(swap_transaction_tx, self.privatekey)
        send_transaction = self.web3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        receipt_swap = self.web3.eth.wait_for_transaction_receipt(send_transaction)
        log("routers", "Quickswap transactionHash: " + receipt_swap["transactionHash"].hex() + " receipt_swap : " + str(receipt_swap))
        time.sleep(10)
        return send_transaction, receipt_swap["status"]
