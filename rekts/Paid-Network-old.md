# Paid Network
![Paid Network](/rektimages/Paid-Network-old.png)
- Amount Lost: $27,418,034.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-3-5

**Quick Summary**

External wallet exploited ProxyAdmin contract to mint new tokens and sell them off.

  


 **Details of the Exploit**

The contract deployer transferred the ownership to an external address through the ProxyAdmin contract by calling the newOwner() function. The external wallet then invoked the mint() function to generate new tokens in his wallet. These tokens were then sold off in a series of transactions.

 **  
**

 **Block Data Reference**

The transaction of ownership transfer:

https://etherscan.io/tx/0x733dd279b3d24f3415f3850b8eceafc651c1998163dcd0352b9e83c46e2b33d9

  


The transaction of minting new tokens:

https://etherscan.io/tx/0x4bb10927ea7afc2336033574b74ebd6f73ef35ac0db1bb96229627c9d77555a0

  


The transactions of selling off the tokens:

https://etherscan.io/address/0x18738290af1aaf96f0acfa945c9c31ab21cd65be#tokentxns

  


The deposit of stolen funds to the Tornado Cash mixer:

https://bloxy.info/txs/calls_from/0x18738290af1aaf96f0acfa945c9c31ab21cd65be?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://www.rekt.news/paid-rekt/](https://www.rekt.news/paid-rekt/)


