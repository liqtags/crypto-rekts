# Raydium
![Raydium](/rektimages/Raydium.png)
- Amount Lost: $4,400,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-16

**Quick Summary**

The private key of the Pool Owner account  was compromised.

The attacker drained nine Raydium’s constant product liquidity pools having stolen crypto worth around 4.4m USD. 

  


 **Details of the Exploit**

The affected pools are ETH-USDC, RAY-SOL, RAY-USDC, RAY-USDT, SOL-USDT, SOL-USDC, stSOL-USDC, UXP-USDC, ZBC-USDC. 

The funds draining was performed through repeatedly calling the  withdrawPNL function that allows to withdraw fees from the pools.  The expected fees to be withdrawn were increased with the SetParams and AmmParams::SyncNeedTake functionality. 

 

  


 **Block Data Reference**

The pool owner account: 

[https://solscan.io/account/HggGrUeg4ReGvpPMLJMFKV69NTXL1r4wQ9Pk9Ljutwyv](https://solscan.io/account/HggGrUeg4ReGvpPMLJMFKV69NTXL1r4wQ9Pk9Ljutwyv) 


Proof Links:
- [https://twitter.com/osec_io/status/1603763023151509505](https://twitter.com/osec_io/status/1603763023151509505)
- [ https://twitter.com/RaydiumProtocol/status/1604251722351710211?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet]( https://twitter.com/RaydiumProtocol/status/1604251722351710211?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Etweet)


