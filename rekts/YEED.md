# YEED
![YEED](/rektimages/YEED.png)
- Amount Lost: $1,043,069.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-4-21

**Quick Summary**

YEED Token was dumped due to the exploit with a profit of about 1M+ $USD.

  


 **Details of the Exploit**

The hacker has performed transfers to three trading pairs, namely ZEED, HOR, and USDT via YEED. This process has been repeated multiple times. The ZEED tokens are directly added or subtracted from the balance of the trading pair, which creates a vulnerability that the hacker exploits. This vulnerability allows the hacker to increase the balance and receive excess rewards from the pair. The attack leverages the ZEED contract's direct calculation of the balance using the rewardFee but not using the separate calculation of zedreward, horward, usdtreward. This vulnerability is used to generate profits for the hacker. The total amount of funds stolen is estimated at $1,043,070. The hacker has not yet transferred out the funds, as the contract has already self-destructed. 

  


 **Block Data Reference**

Exploit TXs:

https://bscscan.com/tx/0x0507476234193a9a5c7ae2c47e4c4b833a7c3923cefc6fd7667b72f3ca3fa83a

Exploiter address:

https://bscscan.com/address/0xec14207d56e10f72446576779d9b843e476e0fb0

Attacker contract:

https://bscscan.com/address/0x05e55d051ac0a5fb744e71704a8fa4ee3b103374


Proof Links:
- [https://twitter.com/PeckShieldAlert/status/1517062566232879105?s=20](https://twitter.com/PeckShieldAlert/status/1517062566232879105?s=20)
- [ https://mirror.xyz/0xaB265E6124dedE46C85336e720521209d51E403e/6Qi2X7fCVsts6nhlPvuLYi8DSo5RltArCg9Z52L-epo]( https://mirror.xyz/0xaB265E6124dedE46C85336e720521209d51E403e/6Qi2X7fCVsts6nhlPvuLYi8DSo5RltArCg9Z52L-epo)


