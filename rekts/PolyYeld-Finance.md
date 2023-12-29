# PolyYeld Finance
![PolyYeld Finance](/rektimages/PolyYeld-Finance.png)
- Amount Lost: $250,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-7-28

**Quick Summary**

PolyYeld finance introduced a transfer fee, which was inconsistent with its masterchef contract. The resulting vulnerability was exploited by an attacker for $250k.

  


 **Details of the Exploit**

PolyYeld Finance is a yield aggregator protocol on the Polygon network. PolyYield introduced the $xYELD token, a deflationary token in order to support its yield aggregator services. A fee was applied on the transfers of the $xYELD token. The PolyYeld Masterchef contract was not designed to support this token type, which created an exploit opportunity. After a series of deposits and withdraws, the $xYELD balance of the Masterchef became 1 WEI. The calculation of the $YELD rewards were based on the xYELD balance of the pool. This referral mechanism generated  $YELD 49B tokens to the attackers address. The attacker dumped a part of his balance in order to receive $ETH 123. The funds were then bridged and transferred through Tornado.cash.

  


 **Block Data Reference**

The attacker's address:  
https://polygonscan.com/address/0xa4bc39ff54e1b682b366b57d1f6b114a829f5c01

  


The transaction behind the hack:  
https://polygonscan.com/tx/0x3c143d2a211f7448c4de6236e666792e90b2edc8f5035c3aa992fd7d7daca974  
  
  



Proof Links:
- [https://polyyeldfinance.medium.com/moving-forward-yeld-compensation-plan-17be27fab944](https://polyyeldfinance.medium.com/moving-forward-yeld-compensation-plan-17be27fab944)
- [ https://twitter.com/peckshield/status/1420272942030594048]( https://twitter.com/peckshield/status/1420272942030594048)
- [ https://twitter.com/0xPaladinSec/status/1420223729901076489]( https://twitter.com/0xPaladinSec/status/1420223729901076489)


