# MonoX
![MonoX](/rektimages/MonoX.png)
- Amount Lost: $31,400,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-12-1

**Quick Summary**

Monoswap contracts on Polygon and Ethereum were exploited due to a flaw in the swapTokenForExactToken() function, allowing the attackers to inflate the value of the MONO token and drain other tokens from the pool.

  


 **Details of the Exploit**

The attackers exploited a weakness in the swapTokenForExactToken() function in the Monoswap contract, using the same token as tokenIn and tokenOut. This resulted in the price of the MONO token being artificially inflated. The attackers then used this inflated token to swap out almost all of the other tokens in the pool.

  


Stolen funds:

\- 5.7M MATIC ($10.5M)

\- 3.9k WETH ($18.2M)

\- 36.1 WBTC ($2M)

\- 1.2k LINK ($31k)

\- 3.1k GHST ($9.1k)

\- 5.1M DUCK ($257k)

\- 4.1k MIM ($4.1k)

\- 274 IMX ($2k)

  


 **Block Data Reference**

  


The attacker's addresses:

Polygon: https://polygonscan.com/address/0xecbe385f78041895c311070f344b55bfaa953258

Ethereum: https://etherscan.io/address/0xecbe385f78041895c311070f344b55bfaa953258

  


Transactions behind the attack:

Polygon: https://polygonscan.com/tx/0x5a03b9c03eedcb9ec6e70c6841eaa4976a732d050a6218969e39483bb3004d5d

Ethereum: https://etherscan.io/tx/0x9f14d093a2349de08f02fc0fb018dadb449351d0cdb7d0738ff69cc6fef5f299


Proof Links:
- [https://twitter.com/MonoXFinance/status/1465692925791137799](https://twitter.com/MonoXFinance/status/1465692925791137799)
- [ https://rekt.news/monox-rekt/]( https://rekt.news/monox-rekt/)
- [ https://twitter.com/FrankResearcher/status/1465679352448917504]( https://twitter.com/FrankResearcher/status/1465679352448917504)


