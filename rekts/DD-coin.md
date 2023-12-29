# DD coin
![DD coin](/rektimages/DD-coin.png)
- Amount Lost: $306,597.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-6-1

**Quick Summary**

DD coin's Marketplace contract was exploited. The attacker increased their allowances and profited for 306,597 $USD.

  


 **Details of the Exploit**

DD coin is a BEP20 token trading on PancakeSwap. DD coin's Marketplace smart contract had a vulnerability that allowed an attacker to increase their allowances by simulating multiple buy/sell actions from their newly deployed smart contracts and the main malicious smart contract. This gave them enough access to withdraw 306,597 $USD worth of tokens from the Marketplace contract. Over 80 fake buyer contracts were deployed during this process which resulted in two similar transactions where all these actions occurred. The stolen funds were transferred to another EOA address.

  


 **Block Data Reference**

Attacker address: 

https://bscscan.com/address/0x0a3fee894eb8fcb6f84460d5828d71be50612762

  


Malicious transactions:

https://bscscan.com/tx/0xd92bf51b9bf464420e1261cfcd8b291ee05d5fbffbfbb316ec95131779f80809

https://bscscan.com/tx/0x9ba6723c2f529f3e5c1d7673da7258f24713330f6f51a6493d64a0f13e7ee75a

  


Funds holder address:

https://bscscan.com/address/0xa100c4b1962dcdb44201ce123833bf275e5f8847

  


Malicious contracts addresses:

https://bscscan.com/address/0x105e9b0266ae0ae670b7fe9af08cf32049f0dd21

https://bscscan.com/address/0x2d9cb2b02870c6afcf457c14e38fbf8b74ead8d0


Proof Links:
- [https://twitter.com/CertiKAlert/status/1664176774262013957](https://twitter.com/CertiKAlert/status/1664176774262013957)


