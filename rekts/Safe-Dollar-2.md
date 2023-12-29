# Safe Dollar
![Safe Dollar](/rektimages/Safe-Dollar-2.png)
- Amount Lost: $248,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-6-28

The attacker's address:  
https://polygonscan.com/address/0xfedc2487ed4bb740a268c565dacdd39c17be7ebd  
  
The attack transaction:  
https://polygonscan.com/tx/0x1360315a16aec1c7403d369bd139f0fd55a99578d117cb5637b234a0a0ee5c14  
  
The attack took the use of a flaw in Safe Dollar reward structure to alter the _accSdoPerShare_ value, allowing it to claim a big number of SDO for each token deposited token.  
  
In preparation, an initial deposit was placed into one of the protocol's Safe Farms:  
https://polygonscan.com/tx/0x55dad44a7ed31d1637e70879af66e02290d39aea54554f8411e6ec19c03a074b  
  
Transfer fees are charged by PLX, the currency that SafeDollar was incentivizing. These fees are meant to be borne by the user, however, they were taken from the rewarder balance instead during withdrawal transactions.  
  
The hacker used a deposit/withdraw loop to progressively drain the pool's PLX balance over the course of 101 transactions, resulting in a hugely inflated _accSdoPerShare_ of 1,142,913,215,739,484,400 SDO being awarded for each PLX contributed.  
  
Claiming rewards on the initial deposit produced a total of 831,309,277,244,108,000 SDO which were sold by the attacker.


Proof Links:
- [https://safedollar.medium.com/safedollar-post-mortem-analysis-cb2769fe059](https://safedollar.medium.com/safedollar-post-mortem-analysis-cb2769fe059)
- [ https://rekt.news/safedollar-rekt/]( https://rekt.news/safedollar-rekt/)


