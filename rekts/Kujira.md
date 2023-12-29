# Kujira
![Kujira](/rektimages/Kujira.png)
- Amount Lost: $260,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2023-2-21

**Quick Summary**

Kujira Network was exploited, resulting in more than 236,000 $USD worth of $USK being created. 

  


 **Details of the Exploit**

Kujira Network is a layer-1 ecosystem. $USK is the stablecoin of the ecosystem. The attacker exploited a previously unknown vulnerability and minted $USK to buy their own $ETH back from themselves at an unusually expensive rate. This exploit caused $230,000 of bad debt to be accrued by this contract. 

  


In the USK Margin contract instead of providing collateral and minting $USK, users provide $USK, and the contract is permitted to mint $USK and then swap the total amount for the collateral asset.

A bug in the USK Margin contract meant it considered $ETH to be worth significantly more than the market rate when opening a new position, allowing the exploiter to place limit orders for their own $ETH at a little less than 10,000 $USK each. They then opened large margin positions, which minted $USK, and bought their own $ETH back from themselves, at nearly 6x the market rate. 

This $USK was then sold for $USDC and extracted from the network. The attacker sold a total of 58 $ETH, and the USK Margin contract has a total debt of 335,000 $USK, equating to roughly $236,000 $USD. 

  


In order to guarantee that $USK is fully collateralized - the Kujira Team has placed a single limit order on the USDC-USK pair for 245,000 $USDC at a price of 1.01. This meant absorbing any excess supply from the market, offsetting the effects of the attack.

  


 **Block Data Reference**

USK Margin contract:

https://finder.kujira.app/kaiyo-1/contract/kujira1m4ves3ymz5hyrj3war3t7uxu9ewt8rwpunja87960n0gre3a5pzspgry4g


Proof Links:
- [https://twitter.com/teamkujira/status/1628008910312407040?s=46&t=E8wgajeu3hb1yrjKdowRVQ](https://twitter.com/teamkujira/status/1628008910312407040?s=46&t=E8wgajeu3hb1yrjKdowRVQ)


