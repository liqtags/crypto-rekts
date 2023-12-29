# PancakeSwap
![PancakeSwap](/rektimages/PancakeSwap-2.png)
- Amount Lost: $1,800,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-4-12

Since April 12th, 2021 a person who had access to a Binance Smart Chain account 0x35f16a46d3cf19010d28578a8b02dfa3cb4095a1 (PancakeSwap admin account) has stolen from PancakeSwap lottery pool 59,765 Cakes (equivalent of about $1,800,000). He used the exploit a few times. Shortly after the last theft, the lottery game was suspended, and this account was banned by PancakeSwap.  
  
The admin of PancakeSwap used his opportunity to manually call lottery contract methods such as:  
  
\- function drawing(uint256 _externalRandomNumber) external onlyAdmin  
  
\- function enterDrawingPhase() external onlyAdmin  
  
He executed a few calls simultaneously (buy, enter drawing, draw) and put them all into the same block. That created for him an opportunity to predict jackpot numbers, since the random number generator, based on the previous block hash, was no longer random.


Proof Links:
- [https://cryptopwnage.medium.com/1-800-000-was-stolen-from-binance-smart-chain-pancakeswap-lottery-pool-ca2afb415f9](https://cryptopwnage.medium.com/1-800-000-was-stolen-from-binance-smart-chain-pancakeswap-lottery-pool-ca2afb415f9)
- [ https://hacked.slowmist.io/]( https://hacked.slowmist.io/)


