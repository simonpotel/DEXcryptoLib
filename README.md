# DEXcryptoLib

<img src="https://github.com/simonpotel/DEXcryptoLib/blob/00055673f01d94ee65bb20b0c82928aaa058a3a4/logo.jpeg" width="300" height="300">

A Python library for simpler interaction with the blockchain. This library uses Python's native Web3 api, which can be installed via the deployment section.
Functions for interacting with contracts and different network tokens in the blockchain.

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
