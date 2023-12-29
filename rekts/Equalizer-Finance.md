# Equalizer Finance
![Equalizer Finance](/rektimages/Equalizer-Finance.png)
- Amount Lost: $72,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-6-7

On June 7-th Equalizer Finance suffered from a flash loan attack. The EqualizerFinance has FlashLoanProvider contract that providers flash loans, and the Vault contract used for borrowing funds by calling _flashLoan()  _function.

  


Flash loan attack explanation:

The attacker first borrows 165.3 WBNB from PancakeSwap using flash loan. 

Event 15: https://bscscan.com/tx/0xdc4ea764632bb264bf820e1942c20cda4c9564c1255f78a6b8aa62c31d5035f0#eventlog

The FlashLoanProvider provider first transfers the WBNB liquidity to the attacker in the WBNB storage contract, which is then followed by the flash loan callback.  
The attacker then provides liquidity to the WBNB repository in a second instant callback.  
The attacker then returns the secondary flash loan and removes the liquidity from the WBNB vault.  
By targeting the storage contracts in each chain, the attacker was able to withdraw liquidity from Equalizer Finance.

  


Attack transactions:

ETH - https://etherscan.io/tx/0x9b17f61d2c7fc4463ff94c5edfea6695d131584a6e07fed5b9ed298c16c17f41

BSC - https://bscscan.com/tx/0xdc4ea764632bb264bf820e1942c20cda4c9564c1255f78a6b8aa62c31d5035f0

  


Attacker address: 

BSC - https://bscscan.com/address/0x0000003502aa61a5f1b1fdadff2cf947dfda526e

ETH - https://etherscan.io/address/0x0000003502aa61a5f1b1fdadff2cf947dfda526e

  


Attacker contract address:

ETH - https://etherscan.io/address/0xf667e04a8d5910328ae92750c0459d2e9e29a67f

BSC - https://bscscan.com/address/0xf667e04a8d5910328ae92750c0459d2e9e29a67f


Proof Links:
- [https://twitter.com/EqualizerFlash/status/1534161931547836417](https://twitter.com/EqualizerFlash/status/1534161931547836417)


