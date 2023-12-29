# Harvest Finance
![Harvest Finance](/rektimages/Harvest-Finance.png)
- Amount Lost: $33,800,000.00
- Funds Returned: $2,500,000.00
- Category: Yield Aggregator
- Date: 2020-10-26

**Quick Summary**

An attacker exploited a vulnerability in the FARM_USDT and FARM_USDC pools, stealing $33.8 million through a series of flash loans and price manipulation.

 **  
**

 **Details of the Exploit**

The attacker initiated the exploit by swapping 11.4 million USDC for USDT, causing the price of USDT to rise. They then deposited 60.6 million USDT into the Vault. Following this, they exchanged 11.4 million USDT back to USDC, causing the USDT price to drop. The attacker then withdrew 61.1 million USDT from the Vault, making a profit of 0.5 million. This process was repeated 32 times. The stolen funds were then converted to renBTC and exited to BTC / ETH via Tornado Cash.

  


Stolen funds:

\- $33.8M USDT

  


 **Block Data Reference**

The attacker's address:

https://app.zerion.io/0x3811765a53c3188c24d412daec3f60faad5f119b/history

The transaction behind the attack:

https://etherscan.io/tx/0x9d093325272701d63fdafb0af2d89c7e23eaf18be1a51c580d9bce89987a2dc1/advanced

Detailed transaction analysis:

https://ethtx.info/mainnet/0x9d093325272701d63fdafb0af2d89c7e23eaf18be1a51c580d9bce89987a2dc1


Proof Links:
- [https://rekt.news/harvest-finance-rekt/](https://rekt.news/harvest-finance-rekt/)
- [ https://medium.com/harvest-finance/harvest-flashloan-economic-attack-post-mortem-3cf900d65217?source=collection_archive---------0-----------------------]( https://medium.com/harvest-finance/harvest-flashloan-economic-attack-post-mortem-3cf900d65217?source=collection_archive---------0-----------------------)


