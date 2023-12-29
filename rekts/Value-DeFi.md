# Value DeFi
![Value DeFi](/rektimages/Value-DeFi.png)
- Amount Lost: $10,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-5-5

**Quick Summary**

An attacker exploited a vulnerability in the pool of vBSWAP/BUSD LP, re-initialized the pool, took control, and drained the original stake token, resulting in a loss of 10,839.16 vBSWAP/BUSD LP.

  


 **Details of the Exploit**

The attacker re-initialized the pool and set the operator role to himself and _stakeToken to HACKEDMONEY. He then took control of the pool and called the method governanceRecoverUnsupported() to drain the original stake token (vBWAP/BUSD LP). The attacker removed 10,839.16 vBWAP/BUSD LP, then removed liquidity and received 7342.75 vBSWAP and 205,659.22 BUSD. He sold all 7342.75 vBSWAP for 8790.77 BNB at 1inch. The attacker used both BNB and BUSD to buy renBTC and used renBridge to move the funds back to BTC, which was laundered to a specific address.

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/address/0xef63ad578e75d498d0723e5420fa1962b1d28764

The transaction behind the attack:

https://bscscan.com/tx/0xd3382252bc204fdc32a6b3add8c639850882b70a798399d6e00a542cdf769040

The transaction of removing vBWAP/BUSD LP:

https://bscscan.com/tx/0x9ba0454c2301ad5780795ae7477e9fa7e38226be16cc282158624479e66389b6

The laundered BTC address:

https://www.blockchain.com/btc/address/1Cm6WGvXQ9EgvvWX5dRsBxE2NvxFjfbcVF


Proof Links:
- [https://medium.com/valuedefi/vstake-pool-incident-post-mortem-4550407c9714](https://medium.com/valuedefi/vstake-pool-incident-post-mortem-4550407c9714)
- [ https://rekt.news/value-rekt2/]( https://rekt.news/value-rekt2/)


