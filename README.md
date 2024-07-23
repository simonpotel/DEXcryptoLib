# DEXcryptoLib

<img src="https://github.com/simonpotel/DEXcryptoLib/blob/a753d48f7edb8da48bb372cd4daeba60291e2754/logo.jpeg" width="300" height="300">

DEXcryptoLib is a Python library designed to streamline interactions with the blockchain. The primary objective of this project is to replicate the functionalities of smart contracts, particularly those found in decentralized exchanges like Uniswap or Quickswap, facilitating direct interaction with smart contracts using your code.

For example, for ERC 20 Tokens functions, refer to: [ier20.py](https://vscode.blockscan.com/polygon/0x5757371414417b8C6CAad45bAeF941aBc7d3Ab32) in Lib/Web3/ier20.py.

> [!IMPORTANT]  
> The project structure is based on my understanding of web3, hence expect periodic updates to the main structure of the project to align with changes in smart contracts or networks.

> [!CAUTION]  
> This is a library, and it does not govern all transaction security. If you encounter any issues during your transactions, they may be caused by factors unrelated to the library or its code.

This library leverages Python's native Web3 API, which can be installed using the following command:

```bash
pip install web3
```

## Deployment

### Installation
To include the project as a submodule of your project, run:

```bash
git submodule add https://github.com/simonpotel/DEXcryptoLib
```

To get the latest version of the library:

```bash
git submodule update --remote
```

### Usage
Include the library in your code as follows:

```python
from DEXcryptoLib.Lib import *
```

## Usage Examples (Snippets)

For usage examples, refer to the snippets provided in DEXcryptoLib\snippets\*.
