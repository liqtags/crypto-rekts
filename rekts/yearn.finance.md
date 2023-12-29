# yearn.finance
![yearn.finance](/rektimages/yearn.finance.png)
- Amount Lost: $11,000,000.00
- Funds Returned: $1,700,000.00
- Category: Yield Aggregator
- Date: 2021-2-5

**Quick Summary**

An attacker exploited dYdX, Aave v2, Compound, and Curve in a complex flash loan attack, resulting in a significant manipulation of funds.

  


 **Details of the Exploit**

The attacker initiated the exploit by flash loaning 116k ETH from dYdX and 99k ETH from Aave v2. They then borrowed 134M USDC and 129M DAI using the loaned ETH as collateral on Compound. The attacker added these funds to the 3crv Curve pool and withdrew 165M USDT. 

  


This process was repeated five times, each time depositing less DAI to the yDAI vault and withdrawing less DAI from it. In the final iteration, the attacker withdrew 39M DAI and 134M USDC instead of USDT. The attacker then repaid the debts on Compound and the flash loans on dYdX and Aave v2.

  


 **Block Data Reference**

The attacker's transactions:

https://etherscan.io/tx/0x59faab5a1911618064f1ffa1e4649d85c99cfd9f0d64dcebbc1af7d7630da98b

https://etherscan.io/tx/0xf6022012b73770e7e2177129e648980a82aab555f9ac88b8a9cda3ec44b30779


Proof Links:
- [https://rekt.news/yearn-rekt/](https://rekt.news/yearn-rekt/)
- [ https://github.com/yearn/yearn-security/blob/master/disclosures/2021-02-04.md#References]( https://github.com/yearn/yearn-security/blob/master/disclosures/2021-02-04.md#References)
- [ https://twitter.com/FrankResearcher/status/1357464851531116544]( https://twitter.com/FrankResearcher/status/1357464851531116544)
- [ https://blog.defiyield.app/yearn-finance-exploit-explained-a10b07c280c8]( https://blog.defiyield.app/yearn-finance-exploit-explained-a10b07c280c8)


