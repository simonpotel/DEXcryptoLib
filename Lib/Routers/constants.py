#Address and ABI of all routers used in Polygon
from ..Misc.jsonconfig import *  # Importing logs from the Misc directory.

aQuickswap = "0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff" #_factory (address): 0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32
abiQuickswap = GetJSONConfig('DEXcryptoLib/Lib/Routers/quickswap_abi.json')

aUniswap = '0xE592427A0AEce92De3Edee1F18E0157C05861564'
abiUniswap = GetJSONConfig('DEXcryptoLib/Lib/Routers/uniswap_abi.json')