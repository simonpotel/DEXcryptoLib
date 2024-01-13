#This file is importing all composants of the Library

#
from .Misc.logs import *  # Importing the file that manages logs (debug/chain)
from .Misc.json import *  # Importing functionality to retrieve JSON configurations (logs/wallets)
from .Misc.wallet import *  # Importing the class for creating wallet objects and facilitating multi-wallet management
from .Misc.database import *  

#
from .Networks.constants import *  # Importing all Constants related to Networks
#
from .Networks.Polygon.constants import *  # Importing all constants related to tokens on the Polygon Network
from .Networks.Polygon.matic import *  # Importing the Native token class for interacting with MATIC on the Polygon Network
#
from .Routers.constants import *  # Importing addresses and ABIs of all configured routers
from .Routers.quickswap import *  # Importing the class for interacting with the Quickswap router 
from .Routers.uniswap import *  # Importing the class for interacting with the Uniswap router 
#
from .Web3.contract import *  # Importing functionality related to contracts in Web3
from .Web3.network import *  # Importing functionality related to networks in Web3

#**********DIRECTORY TREE
# Lib/
# |-- __init__.py #Actual file

# Networks/
# |-- constants.py
# |-- Bitcoin/
# |   |-- .py
# |-- Ethereum/
# |   |-- .py
# |-- Polygon/
# |   |-- constants.py
# |   |-- matic.py

# Misc/
# |-- jsonconfig.py
# |-- logs.py
# |-- wallet.py

# Routers/
# |-- constants.py
# |-- quickswap.py

# Web3/
# |-- contract.py
# |-- network.py

