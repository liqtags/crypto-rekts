# Saddle Finance
![Saddle Finance](/rektimages/Saddle-Finance.png)
- Amount Lost: $11,000,000.00
- Funds Returned: $2,500,000.00
- Category: Exchange (DEX)
- Date: 2022-4-30

**Quick Summary**

Saddle Finance, an automated market maker (AMM) on Ethereum, suffered an attack on April 30, 2022, which exploited smart contracts and resulted in roughly $11m of crypto being stolen

  


 **Details of the Exploit**

Saddle Finance, an automated market maker (AMM) on Ethereum, experienced a series of transactions on April 30, 2022, which resulted in the loss of roughly $11 million worth of cryptocurrency. The attack was carried out in three transactions, with one of them being a whitehat who managed to rescue approximately 25% of the total amount taken. The exploit was made possible due to a previously known bug that had not been properly patched. Saddle Finance is an AMM that focuses on stable swaps of assets that are pegged or similar in nature. It uses concepts from Curve, which has two distinct swap pools: Standard and Meta. The Meta pool allows liquidity in one pool to be used in additional pools. The root cause of the attack on Saddle Finance was the inconsistent price calculations of assets within its Meta pool. The mispricing was caused by the omission of math that calculates the value of tokens given, based upon the base virtual price of the LP token. The bug was present within the library called MetaSwapUtils, which is used for calculating swaps, deposits, and withdrawals. Despite the protocol's quick reaction to the exploit and the migration to a supposedly fixed MetaSwapUtils library, the incorrect swap calculation present in the original code was still present in live pools.

  


 **Block Data Reference**

Exploit TXs:

https://etherscan.io/tx/0x2b023d65485c4bb68d781960c2196588d03b871dc9eb1c054f596b7ca6f7da56

https://etherscan.io/tx/0xe7e0474793aad11875c131ebd7582c8b73499dd3c5a473b59e6762d4e373d7b8

  


Exploiter:

https://etherscan.io/address/0x63341ba917de90498f3903b199df5699b4a55ac0


Proof Links:
- [https://twitter.com/peckshield/status/1520330006710616064?s=20](https://twitter.com/peckshield/status/1520330006710616064?s=20)
- [ https://medium.com/immunefi/hack-analysis-saddle-finance-april-2022-f2bcb119f38]( https://medium.com/immunefi/hack-analysis-saddle-finance-april-2022-f2bcb119f38)


