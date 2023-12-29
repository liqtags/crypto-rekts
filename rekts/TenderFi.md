# TenderFi
![TenderFi](/rektimages/TenderFi.png)
- Amount Lost: $1,583,432.00
- Funds Returned: $1,486,726.00
- Category: Borrowing and Lending
- Date: 2023-3-7

**Quick Summary**

TenderFi was exploited by a WhiteHat hacker via the Oracle issue. The hacker was able to borrow 1,583,432 $USD worth of assets and returned almost the full amount.

  


 **Details of the Exploit**

TenderFi is a Lending and Borrowing protocol running on the layer-2 Arbitrum chain. The protocol was exploited via Oracle issue, which allowed the hacker to take 1,583,432 $USD worth of assets for 1 $GMX (~70 $USD). The project's Unitroller contract has oracle misconfiguration, which allowed malicious actions on DistributedBorrowerComp() function. The WhiteHat hacker left an on-chain message, to contact him to return the funds. Within 24 hours after the incident, the TenderFi Team was able to recover the funds, while paying the Bug Bounty for 62.15 $ETH. The received funds were transferred to another EOA address. The TenderFi Team claimed they will compensate the remaining funds, so the protocol's users will not be affected and there will be no bad debt.

  


 **Block Data Reference**

Attacker address:

https://arbiscan.io/address/0x896df3759205c141c97640b2b7345fa479feb1ab

  


Malicious transaction example:

https://arbiscan.io/tx/0x0a637e3260c7b5f23e93e89c5f5cc2c0ca05ebccdfd0403fb8d7d97f8dba4c4a

  


Recovering transaction example:

https://arbiscan.io/tx/0x0281ff6e307cec5a74068824b9e86839c0f14633b7b0926ffca6db11ea806bd1

  


Attacker's on-chain message:

https://arbiscan.io/tx/0x38ae60739af0726831957546d9d16c92ed75164a1581d4e4e6f270917913ab9c

  


Recovering message from the TenderFi:

https://arbiscan.io/tx/0xdeb31360e395dcba28ec360f61c619f5ebd0db170a189b796631b2c6796e0b72

  


Address holding the Bug Bounty:

https://arbiscan.io/address/0xd724a36b813a6e3592e6c03dde906da711203769


Proof Links:
- [https://twitter.com/tender_fi/status/1633170112718188549](https://twitter.com/tender_fi/status/1633170112718188549)
- [ https://twitter.com/lookonchain/status/1633063188735614976]( https://twitter.com/lookonchain/status/1633063188735614976)
- [ https://cointelegraph.com/news/defi-lender-tender-fi-suffers-exploit-white-hat-hacker-suspected]( https://cointelegraph.com/news/defi-lender-tender-fi-suffers-exploit-white-hat-hacker-suspected)


