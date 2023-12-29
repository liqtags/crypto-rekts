# PancakeBunny
![PancakeBunny](/rektimages/PancakeBunny.png)
- Amount Lost: $2,395,931.00
- Funds Returned: $2,395,931.00
- Category: Yield Aggregator
- Date: 2021-7-16

**Quick Summary**

PancakeBunny's VaultFlipToFlip vault was exploited using 8 flash loans, leading to a skewed calculation of the BUNNY price and a loss of approximately $1B in BUNNY tokens.

  


 **Details of the Exploit**

The attacker manipulated the price on various PancakeSwap pools using 8 flash loans, which skewed the calculation of the BUNNY price in the VaultFliptoFlip vault. They borrowed WBNB from seven different PancakeSwap pools and USDT from Fortube Bank, deposited a portion of these funds into the WBNB+BUSDT pool, and swapped a large amount of WBNB for BUSDT. This manipulation allowed them to claim a reward of 6.97M BUNNY, valued at about $1B, from VaultFlipToFlip. After the exploit, they returned the flash loans to the PancakeSwap pools and Fortube Bank.

  


Stolen funds:

\- 6.97M BUNNY (~$1B)

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/address/0xa0acc61547f6bd066f7c9663c17a312b6ad7e187

The transaction behind the attack:

https://bscscan.com/tx/0x897c2de73dd55d7701e1b69ffb3a17b0f4801ced88b0c75fe1551c5fcce6a979


Proof Links:
- [https://pancakebunny.medium.com/polybunny-post-mortem-compensation-42b5c35ce957](https://pancakebunny.medium.com/polybunny-post-mortem-compensation-42b5c35ce957)
- [ https://www.reddit.com/r/PancakeBunny/comments/olo4gb/polybunny_hacked/]( https://www.reddit.com/r/PancakeBunny/comments/olo4gb/polybunny_hacked/)
- [ https://www.bsc.news/post/pancakebunny-hit-with-another-flash-loan-exploit-this-time-on-polygon]( https://www.bsc.news/post/pancakebunny-hit-with-another-flash-loan-exploit-this-time-on-polygon)
- [ https://beincrypto.com/polybunny-finance-releases-2-4m-defi-attack-post-mortem-report/]( https://beincrypto.com/polybunny-finance-releases-2-4m-defi-attack-post-mortem-report/)


