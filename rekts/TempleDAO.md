# TempleDAO
![TempleDAO](/rektimages/TempleDAO.png)
- Amount Lost: $2,376,872.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-10-11

**Quick Summary**

TempleDAO's staking contract was exploited due to a vulnerable migration functionality. The hacker took away FraxLP tokens and swapped them for 1830 $ETH.

  


 **Details of the Exploit**

TempleDAO is a DeFi yield aggregator. The exploit happens due to stake migration functionality on the StaxLPStaking contract. The attacker was able to transfer xFraxTempleLP liquidity tokens to his address and took $TEMPLE and $FRAX tokens from the pool. Consequently, the hacker swapped them for 1830 $ETH and transferred the stolen funds to another EOA address. The total profit of the attacker reached 2,376,872 $USD. An interesting detail is that the attacker's address was linked to Binance's address. TempleDAO is investigating the accident with Binance and Stax said that a white hat bounty will be initialized for the exploiter.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x9c9Fb3100A2a521985F0c47DE3B4598dafD25B01

  


Malicious transaction:

https://etherscan.io/tx/0x8c3f442fc6d640a6ff3ea0b12be64f1d4609ea94edd2966f42c01cd9bdcf04b5

  


Liquidity removal transaction:

https://etherscan.io/tx/0x4b119a4f4ba1ad483e9851973719f310527b43f3fcc827b6d52db9f4c1ddb6a2


Proof Links:
- [https://cointelegraph.com/news/templedao-exploit-results-in-2m-loss](https://cointelegraph.com/news/templedao-exploit-results-in-2m-loss)


