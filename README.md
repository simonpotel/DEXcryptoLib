# DEXcryptoLib

<img src="https://github.com/simonpotel/DEXcryptoLib/blob/a753d48f7edb8da48bb372cd4daeba60291e2754/logo.jpeg" width="300" height="300">

A Python library for simpler interaction with the blockchain. 
The main purpose of this project is to recreate the functions of smart contracts, notably those of decentralized exchanges like Uniswap or Quickswap, to enable direct interactions with the smart contracts using your code.

Exemple for the ERC 20 Tokens functions: https://vscode.blockscan.com/polygon/0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32
in Lib/Web3/ier20.py

This library uses Python's native Web3 api, which can be installed via the deployment section.

You can calculate the fees you will incur during approval or swapping. You can perform swaps using QuickSwap or Uniswap routers on the Polygon network.

## Deployment
- To install requires:
```python
pip install web3
```

- To include the project as submodule of your project
```
git submodule add https://github.com/simonpotel/DEXcryptoLib
```

- To get latest version of the lib 
```
git submodule update --remote 
```

- Includes in your code:
```python
    from DEXcryptoLib.Lib import *
```

## Importants Advices
> [!NOTE]
> The project is based on the structure I have of web3, so it's possible to have frequent reworkings of the main structure of the project if my perception of how a smart contract or networks works.

> [!CAUTION]
> It's a library, so it doesn't control all transaction security. So if a problem is encountered during your transaction, it may be caused by a number of factors that are not necessarily related to the library and the way the code works.

## Example of usage (snippets)
Watch DEXcryptoLib\snippets\* 
to get examples of usages. 
