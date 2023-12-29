# Inverse Finance
![Inverse Finance](/rektimages/Inverse-Finance-2.png)
- Amount Lost: $1,260,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-6-16

**Quick Summary**

  


Ethereum-based Inverse Finance was exploited for more than $1.2 million by an attacker utilizing an oracle manipulation through a flash loan attack.

 

  


 **Details of the exploit**

  


1) The attacker flashloaned 27,000 WBTC using it's contract from AAVE. Then WBTC was added as liquidity to the Curve pool.

2) The obtained LP tokens were deposited to the Yearn’s Vault. Yearn’s Vault tokens were deposited to Inverse Finance’s Yearn 3Crypto Vault to serve as collateral on Inverse Finance.

3) The attacker's then uses the remaining 26,775 WBTC of the initial flashloan to swap for 75M USDT on Curve 3Crypto. It manipulates the pricing oracle that let's the attacker is then able to borrow $10M worth of Dola USD StableCoin.

4) Then, the 75M USDT is swapped for 26,626 WBTC.

5) The attacker then uses the borrowed DOLA to provide liquidity to the Curve Metapool. When the liquidity is ~10.1M USDT, it is removed.

6) Then, it converts 10M USDT to 451 WBTC using the 3Crypto pool on Curve. A remaining 99,976.294 USDT was kept in the attacker’s smart contract.

  


Exploit transaction: https://etherscan.io/tx/0x958236266991bc3fe3b77feaacea120f172c0708ad01c7a715b255f218f9313c

Exploiter address: https://etherscan.io/address/0x7b792e49f640676b3706d666075e903b3a4deec6

Exploiter contract: https://etherscan.io/address/0xf508c58ce37ce40a40997c715075172691f92e2d

Withdrawing 100K USDT: https://etherscan.io/tx/0x3d2f86c1c289731f56bed95dce20434eff48e3bd4a50cdc007ef5d0a2177a9f7

Withdrawing 53.24 WBTC: https://etherscan.io/tx/0x9959f8f10f59b3b88a5499066a21237e492f193e5ff2950bcc7e6c1f5e1fa60c


Proof Links:
- [https://rekt.news/inverse-rekt2](https://rekt.news/inverse-rekt2)
- [ https://www.certik.com/resources/blog/6LbL57WA3iMNm8zd7q111R-inverse-finance-incident-analysis]( https://www.certik.com/resources/blog/6LbL57WA3iMNm8zd7q111R-inverse-finance-incident-analysis)
- [ https://hacken.io/industry-news-and-insights/flashloan-attack-on-inverse-finances-frontier/]( https://hacken.io/industry-news-and-insights/flashloan-attack-on-inverse-finances-frontier/)
- [ https://cryptopotato.com/second-time-in-2-months-defi-lender-inverse-finance-drained-for-1-6m/]( https://cryptopotato.com/second-time-in-2-months-defi-lender-inverse-finance-drained-for-1-6m/)


