# Arbix Finance
![Arbix Finance](/rektimages/Arbix-Finance.png)
- Amount Lost: $10,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-1-4

**Quick Summary**

Arbitrum (ARBX) contract exploited due to onlyOwner function, leading to the minting and dumping of 10M ARBX tokens.

  


 **Details of the Exploit**

The ARBX contract contained a mint() function with onlyOwner, which was exploited to mint 10M ARBX tokens to 8 different addresses. Approximately 4.5M ARBX were minted in a single transaction and subsequently dumped by the recipient. The users' assets were drained from several pools, with the stolen funds being bridged to Ethereum.

 **  
**

 **Block Data Reference**

  


The addresses involved in the exploit:

https://bscscan.com/address/0x4714a26e4e2e1334c80575332ec9eb043b61a2c4

https://bscscan.com/address/0x161262d172699cf0a5e09b6cdfa5fee7f32c183d

  


The transaction of 4.5M ARBX minting:

https://bscscan.com/tx/0x4707d30a8d8152eebad1cdcae1d93af24cb9a344b447412ee1d65638b5c3db6f

  


The transaction of asset draining:

https://bscscan.com/tx/0xfbba507c8e90a264d5e77e5db854f5697572da1681f3647d4fa4381f7ef825b9

  


The Ethereum address where stolen funds were bridged:

https://etherscan.io/address/0xdc85c1eb22b0ece7be559a83fd788fe57f5a7a9f


Proof Links:
- [https://rekt.news/arbix-rekt/](https://rekt.news/arbix-rekt/)
- [ https://twitter.com/certikorg/status/1478243729244839938]( https://twitter.com/certikorg/status/1478243729244839938)


