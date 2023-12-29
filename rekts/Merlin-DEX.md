# Merlin DEX
![Merlin DEX](/rektimages/Merlin-DEX.png)
- Amount Lost: $1,800,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-4-26

**Quick Summary**

Merlin DEX on zkSync was exploited, with one exploiter stealing almost 850,000 USDC and transferring them to Ethereum. The amount drained from a liquidity pool on the DEX reached $1.82 million, and hackers transferred nearly 165,000 USDC to Binance and MEXC centralized exchanges. The Merlin team has released a post-mortem report stating that several members of the back-end team had drained all of their contracts, carried out on-chain transactions to drain all of Merlin's pools and manipulate front-end contracts.

  


 **Details of the Exploit**

Merlin DEX on zkSync was recently exploited, with one exploiter stealing almost 850,000 USDC and transferring them to Ethereum. Further reports by PeckShield revealed that hackers transferred nearly 165,000 USDC to Binance and MEXC centralized exchanges. The Merlin team has released a post-mortem report stating that several members of the back-end team had drained all of their contracts, carried out on-chain transactions to drain all of Merlin's pools and manipulate front-end contracts.

  


According to the report, the back-end team implemented a function that allowed a call action to all Merlin pairs alongside hidden front-end contracts, draining all of Merlin's pools and the public sale. Merlin had submitted all intended contracts to be used on their platform to Certik for a full audit, but there was a clear oversight on the overarching power that the owner had of the pools. Furthermore, the back-end team, who also had access to Merlin's web-host, unknowingly manipulated the code to achieve their goal.

  


Merlin's priority is to return all funds to affected parties and participants on their platform at the earliest opportunity. They are working alongside on-chain analysts to monitor the movement of the stolen funds and have notified relevant authorities in Serbia (region of the back-end team).

  


 **Block Data Reference**

Wallet addresses of the contract owner/deployer: https://explorer.zksync.io/address/0xc0D6987d10430292A3ca994dd7A31E461eb28182, https://explorer.zksync.io/address/0xc7fD785f81Fe6bBb499009746a2BCbbdd895f5b0


Proof Links:
- [https://twitter.com/TheMerlinDEX/status/1651281814395187200](https://twitter.com/TheMerlinDEX/status/1651281814395187200)
- [ https://www.investing.com/news/cryptocurrency-news/certikaudited-merlin-dex-loses-182m-to-liquidity-pool-exploit-3064794]( https://www.investing.com/news/cryptocurrency-news/certikaudited-merlin-dex-loses-182m-to-liquidity-pool-exploit-3064794)
- [ https://www.coindesk.com/tech/2023/04/26/zksync-based-dex-merlin-drained-of-1m-during-public-token-sale-despite-audit/]( https://www.coindesk.com/tech/2023/04/26/zksync-based-dex-merlin-drained-of-1m-during-public-token-sale-despite-audit/)
- [ https://twitter.com/wasgiventhatday/status/1651043902647078913]( https://twitter.com/wasgiventhatday/status/1651043902647078913)


