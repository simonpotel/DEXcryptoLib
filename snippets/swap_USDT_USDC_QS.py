#This short code is swapping USDT Token to USDC Token using the 
#Smart Contract: QuickSwap

from Lib import *

wallet_address = ""
wallet_key = ""

polygonNet = Network(pol_RPC)  # Creating a Network object for the Polygon network using the specified RPC URL.
qsContract = Contract(polygonNet.web3, aQuickswap, abiQuickswap)  # Creating a Contract object for the Quickswap router with the specified address and ABI.
wallet_qs = Quickswap(polygonNet.web3, qsContract.contract, wallet_address, wallet_key)  # Creating a Quickswap object for interaction with the Quickswap router.

USDTContract = Contract(polygonNet.web3, pol_aUSDT, pol_abiTokens)  # Creating a Contract object for the USDT token with the specified address and ABI.
amount_token = 0.2*(10**6) # 6 decimals so 1*(10**6) for 1USDT (REF: https://polygonscan.com/token/0xc2132d05d31c914a87c6611c10748aeb04b58e8f - "TOKEN CONTRACT (WITH 6 DECIMALS)")

#wallet_qs.Approve(USDTContract.contract, amount_token) # Approve QuickSwap contract to take my USDT on USDT'contract 

#BUILD of the SWAP:
route = [pol_aUSDT, pol_aUSDC] #We are exchanging USDT to USDC, refer to pairs of the tokens.
swap = wallet_qs.SwapExactTokensForTokens(amount=amount_token, path=route, receiver_address=wallet_address, amountOutMin=wallet_qs.getAmountMin(amount=amount_token, path=route))
