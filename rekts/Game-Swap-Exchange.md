# Game Swap Exchange
![Game Swap Exchange](/rektimages/Game-Swap-Exchange.png)
- Amount Lost: $22,796.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-1-24

**Quick Summary**

The Game Swap Exchange project exploited its investors through minting and dumping the $GAME token for $ETH, netting the scammer $ETH 16 in the process.

  


 **Details of the Exploit**

The Game Swap Exchange project existed for 1 day after launching. The contract deployer added initial liquidity at:  
https://etherscan.io/tx/0x67abd476012f072f521301fc4e55c11006c96001e3c452bcb283d768bb202758  
The contract deployer then used a hidden backdoor mechanism by using the minting functionality under the _approveAndCall_ () function to generate new tokens onto this external address at:  
https://etherscan.io/tx/0x179c0c4146440e71cbf353353c664e7b4730475ddf91b0b02d61a56e31a099c8

At this point it is important to state that investors without technical knowledge could have spotted a massive centralization risk with the external wallet holding +99% of the token supply:

https://etherscan.io/token/0x681b24478e9f7e31ee3b5b7f807c9151e46aa165#balances  
  
The token recipient sold the minted tokens for $ETH 28,4, which meant the end for the project:  
https://etherscan.io/tx/0x2bc2c0d42bb22c36c70123179b2be5da9c4ef2653347183a5a396a431655c56f

  


 **Block Data Reference**

Project Deployer Address (Scammer):

https://etherscan.io/address/0x8c848be2790a535c5770af217f1e1b7739e4897b

  


Scammer Address that received the minted tokens:

https://etherscan.io/address/0x0659f3520590a4d39546975b8e56b2ef164c194d



