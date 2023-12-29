# AutoSharkFinance
![AutoSharkFinance](/rektimages/AutoSharkFinance-2.png)
- Amount Lost: $2,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-10-29

The attacker's address:  
https://bscscan.com/address/0xfcf6738cabd9ce27f908a480ecaea53219fc08f4  
  
The example of transaction behind the attack:  
https://bscscan.com/tx/0x8769f7ee2c8e010fc8791bd0e42569b7ced9b2f67b721e6f0c6a6435b4d6670f  
  
The hack is made possible due to a profit inflation bug, which was exploited to donate a large amount of $NOVAs so that a huge amount of $JAWS tokens can be minted as a reward.  
  
The attacker (based on the example tx):  
\- flash loaned 2.5K BNB  
  
\- swapped 569 BNB to 186.5K NOVA  
  
\- deposited  186.5K NOVA to Shiba's NOVA/WBNB LP  
  
\- called _getReward()_ to swap 3.69e-06 NOVA to 561 BNB  
  
\- swapped 280 BNB to 3362 JAWS  
  
\- added liquidity with 280 BNB and 3362 JAWS into JAWS/WBNB LP, receiving 955 LP tokens  
  
\- minted 640,050 JAWS as a reward because of the inflated value of 955 JAWS/WBNB LP tokens  
  
\- called _withdrawAll()_ to withdraw 640,050 JAWS  
  
\- swapped received JAWS to 509 BNB  
  
Stolen funds were bridged into Ethereum. The attacker deposited ETH into Tornado Cash mixer:  
https://etherscan.io/address/0xfcf6738cabd9ce27f908a480ecaea53219fc08f4


Proof Links:
- [https://twitter.com/peckshield/status/1454026801869590529](https://twitter.com/peckshield/status/1454026801869590529)
- [ https://twitter.com/AutoSharkFin/status/1454037053159591949]( https://twitter.com/AutoSharkFin/status/1454037053159591949)


