# HoneySwap.Fi
![HoneySwap.Fi](/rektimages/HoneySwap.Fi.png)
- Amount Lost: $3,280,848.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-2-28

The attack description:  
1\. Deploying MasterChef  
2\. Setting MasterChef ownership to the unverified smart contract:  
https://bscscan.com/tx/0xdc7478ace40fdeca8791fb2a85ebc903f6b2d9a881d0b066280cb5a02d7ca13b  
3\. Unverified contract was set as the migrator:  
https://bscscan.com/address/0xf5b2f301d5936a4f72b5a6a159c20432cc9f563f  
4\. Calling migrate function on each pool, even without any tokens already staked, this call still grants an infinite amount of allowance to the current migrator, which is the unverified contract.  
5\. Setting migrator back to 0x0000000 (this covers up their tracks that something fishy already happened)  
6\. Transfering MasterChef ownership to the Timelock contract  
7\. Executing rug pull method in the unverified contract:  
https://bscscan.com/tx/0xaab125fa61d88e9086cdbcde2cc4010eb768fbeab0fd32184bca63b8cda969da


Proof Links:
- [https://goosefinance.medium.com/the-honeytrap-a-story-about-a-migrator-behind-timelock-397b889ab780](https://goosefinance.medium.com/the-honeytrap-a-story-about-a-migrator-behind-timelock-397b889ab780)


