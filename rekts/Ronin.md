# Ronin
![Ronin](/rektimages/Ronin.png)
- Amount Lost: $625,000,000.00
- Funds Returned: $155,800,000.00
- Category: Bridge
- Date: 2022-3-29

**Quick Summary**

The Ronin bridge has been exploited for 173,600 Ethereum and 25.5M USDC.

  


 **Details of the Exploit  **

The Ronin Network, an Ethereum-based sidechain hosts the prominent play-to-earn game Axie Infinity.

The project team discovered that on March 23rd that Sky Mavis’s Ronin validator nodes and Axie DAO validator nodes were compromised resulting in 173,600 Ethereum and 25.5M USDC drained from the Ronin bridge in two transactions:  
https://etherscan.io/tx/0xc28fad5e8d5e0ce6a2eaf67b6687be5d58113e16be590824d6cfa1a94467d0b7  
https://etherscan.io/tx/0xed2c72ef1a552ddaec6dd1f5cddf0b59a8f37f82bdda5257d9c7c37db7bb9b08  
  
The attacker used hacked private keys in order to forge fake withdrawals. The validator key scheme is set up to be decentralized so that it limits an attack vector, but the attacker found a backdoor through a gas-free RPC node, which they abused to get the signature for the Axie DAO validator. Binance managed to identify and recover $5,8 million in funds spread across 86 accounts that had been moved to their exchange. In the aftermath of the Ronin bridge hack a Binance led funding round raised $150 million in order to partially repay users and ensure that operations will be sustained

  


 **Block Data Reference**

The hacker's address on Ethereum:  
https://etherscan.io/address/0x098b716b8aaf21512996dc57eb0615e2383e2f96


Proof Links:
- [https://twitter.com/Ronin_Network/status/1508828719711879168](https://twitter.com/Ronin_Network/status/1508828719711879168)
- [ https://roninblockchain.substack.com/p/community-alert-ronin-validators?s=w]( https://roninblockchain.substack.com/p/community-alert-ronin-validators?s=w)


