# Pump Farm
![Pump Farm](/rektimages/Pump-Farm.png)
- Amount Lost: $477,544.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2020-11-12

The contract deployer interacted with the 3rd party malicious unverified smart contract that received infinite approval for spending the user's approved tokens. He invoked the _setMigrator_ () function at the following transaction:  
https://etherscan.io/tx/0xcacef01fb0b75344864a2666dcd94ffacb0e70ec241811af962f85328ab30864  
  
This contract called _migrate_ () function multiple times. Example transaction:  
https://etherscan.io/tx/0x88e788afd3e0efb5d4cc7e49c977075b6c25fed6ad270e8c664d26404142c164  
  
Migrated LP tokens were removed from the liquidity pool at:  
https://etherscan.io/tx/0xeb99cfe73e3d61d9e8e07cb74d4efa87db4a695f03760de7c9c992be3a5d3bfe  
  


In addition, the contract deployer has minted 10q PPF tokens onto his wallet:  
https://etherscan.Io/tx/0xa7ca31dbb91f19d57e5797c6ab6970be3414c63563d3e16c1e8fcc8304699d77  
  
After, 1 billion PPF tokens were exchanged for 220.60 WETH:  
https://etherscan.io/tx/0x6d455a00f300c75152b0d6ecc1b2825c4be3b71df50f613adbb3ba6e1802c483

  
Stolen funds were deposited to the Tornado Cash at these 8 transactions to cover up the tracks:  
https://etherscan.io/address/0x0ef1a03cfdbcfbe0ddcff99bc663c9842efe1eaa


Proof Links:
- [https://archive.ph/5LVnC](https://archive.ph/5LVnC)
- [ https://archive.ph/iAAAi]( https://archive.ph/iAAAi)


