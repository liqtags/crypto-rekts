# Nimbus DAO
![Nimbus DAO](/rektimages/Nimbus-DAO.png)
- Amount Lost: $76,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-12-14

**Quick Summary**

Nimbus DAO protocol was exploited via FlashLoan attack. The attacker stole worth around $76,000 USD. 

  


 **Details of the Exploit**

The flashloan was used for the price oracle manipulation and the NIMB/NBU_WBNB pool was affected. Exploit led to the unfair reward distribution in getReward() function.

In case, of computation of the token reward is proportional to the ratio of $NIMB and $GNIMB in the pool, the ratio of Nimbus Utility tokens to Nimbus Governance tokens was broken. To repay the flash loan, the exploiter exchanged $GNIMB for $BNB.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0x86aa1c46f2ae35ba1b228dc69fb726813d95b597

  


Malicious transactions:

https://bscscan.com/tx/0x42f56d3e86fb47e1edffa59222b33b73e7407d4b5bb05e23b83cb1771790f6c1

https://phalcon.blocksec.com/tx/bsc/0x42f56d3e86fb47e1edffa59222b33b73e7407d4b5bb05e23b83cb1771790f6c1

  



Proof Links:
- [https://twitter.com/BeosinAlert/status/1602907558532231169](https://twitter.com/BeosinAlert/status/1602907558532231169)


