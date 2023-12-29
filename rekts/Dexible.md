# Dexible
![Dexible](/rektimages/Dexible.png)
- Amount Lost: $2,047,635.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-2-17

**Quick Summary**

Exchange aggregator Dexible was exploited resulting in the loss of over $2,000,000 worth of $ETH

  


 **Details of the Exploit**

Dexible is a multichain exchange aggregator, that provides a CEX trading experience and tools while being fully decentralized. On February 17th, the Dexible v2 contracts were exploited. The attacker had used the app’s selfSwap() function to move over 2,000,000 $USD worth of crypto from users who had authorized the app to move their tokens. The malicious actor was able to encode the transferFrom() function into the calldata of multiple transactions, getting access to the user's tokens and draining them. The malicious transactions were coming from Dexible, which users had already authorized to spend their tokens, so the token contracts did not block the transactions. 17 users were affected in total, 4 of them were trading on the Ethereum mainnet, and lost 930.6 $ETH which is worth  1,498,266 $USD at the moment. According to some sources, all the lost funds from the Ethereum chain belonged to the BlockTower Capital investment firm. The rest of the affected users are on the Arbitrum layer-2 chain. After receiving the tokens into their own smart contract, the attacker swapped them to $ETH and transfer the funds through Tornado Cash into unknown BNB wallets. Dexible has since paused their contracts and urged users to revoke token authorizations for them.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x684083f312ac50f538cc4b634d85a2feafaab77a

  


Funds transfer example transaction:

https://etherscan.io/tx/0x4393ca721175e8bc97458f97b5118927a026e73b4a6964d16035090b05686a8c


Proof Links:
- [https://cointelegraph.com/news/dexibleapp-aggregator-hacked-for-2m-via-selfswap-function](https://cointelegraph.com/news/dexibleapp-aggregator-hacked-for-2m-via-selfswap-function)
- [ https://twitter.com/DexibleApp/status/1626575966003757056]( https://twitter.com/DexibleApp/status/1626575966003757056)
- [ https://twitter.com/BeosinAlert/status/1626499932265005058]( https://twitter.com/BeosinAlert/status/1626499932265005058)
- [ https://www.coindesk.com/tech/2023/02/17/blocktower-capital-loses-15m-in-defi-market-aggregator-dexible-exploit-blockchain-data/]( https://www.coindesk.com/tech/2023/02/17/blocktower-capital-loses-15m-in-defi-market-aggregator-dexible-exploit-blockchain-data/)


