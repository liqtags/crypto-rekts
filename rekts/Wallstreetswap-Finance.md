# Wallstreetswap Finance
![Wallstreetswap Finance](/rektimages/Wallstreetswap-Finance.png)
- Amount Lost: $2,905,021.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-2-15

**Quick Summary**

Wallstreetswap Finance rug pulled its investors by introducing a backdoor into its smart contracts, granting the project deployer to transfer of all LP positions at will. The exploit cost investors approx. $2,9 million in damages.

  


 **Details of the Exploit**

Wallstreetswap Finance was a DEX on the Binance Smart Chain that offered the typical DEX services such as staking, farming, and swapping. The factory contract contains a line that approves both tokens' balances to the malicious actor in every created LP inside initialize() function. This means that the malicious actor can perform liquidity withdrawal from the pools anytime. 

  


 **Block Data Reference**

LP creation contract WallStreetSwapFactory:  
https://bscscan.com/address/0xd395ce2bbc62eeb612bd4c41d51ef4b6bf611d6c#code

Contract deployer (scammer) address:

https://bscscan.com/address/0xa7524ec326d81dd26765f1bb17ad976d04778304

Some example of token draining:  
https://bscscan.com/tx/0xb8fb142aa94092de2ccf4749a70400f6a91f8365e9ee53ed4d38512e2ec0a5a3

https://bscscan.com/tx/0xb05480336ed4c099f42fde746abb74a370c2ffb4ea1a7850f5be9ee335ca6d26

In this last transaction the contract deployer transferred  all stolen $BNB to a third seemingly unrelated address:

https://bscscan.com/tx/0x92d301e06107cf524101a12ea3540bae85c87b154dcb470f19a88bbf5952d7e7


Proof Links:
- [https://y-pakorn.medium.com/defi-scams-rug-pull-analysis-wallstreetswap-finance-ca657280b85a](https://y-pakorn.medium.com/defi-scams-rug-pull-analysis-wallstreetswap-finance-ca657280b85a)


