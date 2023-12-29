# BiSwap
![BiSwap](/rektimages/BiSwap.png)
- Amount Lost: $865,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-6-30

**Quick Summary**

BiSwap, a DEX on Binance Smart Chain, was exploited, resulting in the loss of 865,000 $USD.

  


 **Details of the Exploit**

BiSwap is a DEX, running on BSC. The protocol was exploited via a parameter validation issue. In an intricate exploit, BiSwap's system failed to verify the validity of tokens and their pair parameters, which was taken advantage of by an attacker. By forging token0, token1, and a pair, the attacker was able to manipulate the migration function of the migration contract, leading to a loss of users' burned assets.

In the first step, using a valid pair and fake tokens, the attacker called the migration function and added the users' burned assets into the contract, subsequently adding two fake tokens to the LP pool. In the second step, using real tokens and a fake LP, they called the migration function again, adding the assets left in the contract to their own LP. As a result, users' assets were replaced with fake LP assets, while real LP assets were added to the attacker's LP.  
The stolen funds of 865,000 $USD were transferred through TornadoCash.

 **  
**

 **Block Data Reference**

Attacker Addresses:

https://bscscan.com/address/0xe3aeede563bc6a72dc881755cc98dc57fadf30f6

https://bscscan.com/address/0xA1E31B29f94296FC85FAC8739511360f279B1976

  


Malicious Contracts:

https://bscscan.com/address/0x2a825a174c3125923881d33e922c7a5e56c9b833

https://bscscan.com/address/0x839b0afd0a0528ea184448e890cbaaffd99c1dbf

  


Malicious Transaction Example:

https://bscscan.com/tx/0xa6cc4b18dea57fae6e1d63d493d2bfb4fd07e86a1ab7f545f9c7980d897d7a6c


Proof Links:
- [https://twitter.com/FairyproofT/status/1675114227617652736](https://twitter.com/FairyproofT/status/1675114227617652736)
- [ https://blog.biswap.org/article/migrator-contract-report]( https://blog.biswap.org/article/migrator-contract-report)


