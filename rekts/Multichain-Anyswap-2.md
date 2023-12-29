# Multichain
![Multichain](/rektimages/Multichain-Anyswap-2.png)
- Amount Lost: $147,326.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-2-15

**Quick Summary**

Multichain Protocol encountered a front-run attack resulting in the loss of 147,326 $USD worth of $ETH 

  


 **Details of the Exploit**

Multichain is an infrastructure designed to support arbitrary cross-chain interactions. On February 15, 2023, the AnyswapV4Router contract of Multichain encountered a front-run attack, during which the attacker made a profit of 87 $ETH, worth approximately 147,326 $USD at the moment. 

The vulnerability occurred because the attacker used an MEV contract to front-run and invoke a function of the AnySwapV4Router contract to sign and approve the transfer. Due to the lack of signature verification, the attacker was able to transfer the $ETH approved to the victim contract, through the from address parameter directly to the attack contract using the safeTransferFrom() function.

  


This was an old vulnerability that was reported in January 2022 and more than 61% of all affected users had revoked access to the contract containing the underlying vulnerability. The liquidity pool's vulnerability was quickly fixed after it was reported, as the Multichain team upgraded the affected tokens' liquidity to new contracts.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0xfde0d1575ed8e06fbf36256bcdfa1f359281455a

  


Malicious MEV contract:

https://etherscan.io/address/0xd050e0a4838d74769228b49dff97241b4ef3805d

  


Malicious transaction:

https://etherscan.io/tx/0x192e2f19ab497f93ed32b2ed205c4b2ff628c82e2f236b26bec081ac361be47f


Proof Links:
- [https://medium.com/multichainorg/multichain-contract-vulnerability-post-mortem-d37bfab237c8](https://medium.com/multichainorg/multichain-contract-vulnerability-post-mortem-d37bfab237c8)
- [ https://twitter.com/BlockSecTeam/status/1625743126307414017]( https://twitter.com/BlockSecTeam/status/1625743126307414017)


