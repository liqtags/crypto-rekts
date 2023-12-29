# Sentiment
![Sentiment](/rektimages/Sentiment.png)
- Amount Lost: $968,279.00
- Funds Returned: $862,569.00
- Category: Borrowing and Lending
- Date: 2023-4-4

**Quick Summary**

Sentiment was exploited through a view re-entrancy Balancer bug, resulting in the loss of 968,279 $USD.

  


 **Details of the Exploit**

Sentiment is a Borrowing and Lending protocol running on the Arbitrum chain. The attacker used a view re-entrancy Balancer bug to execute malicious code before pool balances were updated and steal money using overpriced collateral. The attack involved several steps:

1\. Attacker took a flashloan.

2\. Attacker significantly changed rates.

3\. Attacker called "exitPool" function and executed hack when balancer sent assets to its contract.

4\. Sentiment contracts were called before PoolBalancesChanged emitted by balancer smart contract.

5\. Hacker could manipulate these values to overprice their collateral and then borrow and withdraw sentiment pool assets.

  


The exact amount lost due to this exploit reached 968,279 $USD in total, including 538,399 $USDC, 360,000 $USDT, 0.51 $WBTC and 29.97 $WETH.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0xdd0cDb4c3b887bc533957BC32463977E432e49C3

  


Malicious transaction:

https://etherscan.io/tx/0xa9ff2b587e2741575daf893864710a5cbb44bb64ccdc487a100fa20741e0f74d


Proof Links:
- [https://twitter.com/spreekaway/status/1643313592559706113](https://twitter.com/spreekaway/status/1643313592559706113)
- [ https://twitter.com/0xmikko_eth/status/1643345158451208192]( https://twitter.com/0xmikko_eth/status/1643345158451208192)
- [ https://twitter.com/sentimentxyz/status/1643779654141251584?cxt=HHwWgMDU4dy48M8tAAAA]( https://twitter.com/sentimentxyz/status/1643779654141251584?cxt=HHwWgMDU4dy48M8tAAAA)


