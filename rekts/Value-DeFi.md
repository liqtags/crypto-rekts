# Value DeFi
![Value DeFi](/rektimages/Value-DeFi.png)
- Amount Lost: $7,000,000.00
- Funds Returned: $2,000,000.00
- Category: Exchange (DEX)
- Date: 2020-11-14

**Quick Summary**

A Flash loan attack on ValueMultiVaultBank resulted in a loss of 5.4M DAI.

  


 **Details of the Exploit**

The attacker initiated the exploit by flash loaning 80k ETH from Aave and flash swapping 166M DAI from Uniswap. They then swapped 80k for 31M USDT on Uniswap, deposited 25M DAI on ValueMultiVaultBank, and swapped 91M DAI to 90.2M USDC on Curve. The attacker then withdrew 33M 3CRV from ValueMultiVaultBank, swapped 17.3M USDC to 30.9M USDT on Curve, and removed liquidity with 33M 3CRV for 33.1M DAI on Curve. They then repaid the flash swap and flash loan, transferred 2M DAI to Value Deployer, and finally transferred 5.4M DAI to their EOA.

  


 **Block Data Reference**

The attacker's transaction:

https://etherscan.io/tx/0x46a03488247425f845e444b9c10b52ba3c14927c687d38287c0faddc7471150a


Proof Links:
- [https://rekt.news/value-defi-rekt/](https://rekt.news/value-defi-rekt/)
- [ https://twitter.com/FrankResearcher/status/1327649421492957184?s=20]( https://twitter.com/FrankResearcher/status/1327649421492957184?s=20)


