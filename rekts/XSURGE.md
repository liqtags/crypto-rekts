# XSURGE
![XSURGE](/rektimages/XSURGE.png)
- Amount Lost: $5,570,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-8-16

The transaction behind the attack:  
https://bscscan.com/tx/0x7e2a6ec08464e8e0118368cb933dc64ed9ce36445ecf9c49cacb970ea78531d2  
  
The hacker made a flash loan of 10,000 BNB and purchased 202 trillion SURGEs, next _sell_ () 202 trillion SURGEs within reentrancy to _purchase_ (), where the price is calculated before updating __totalSupply_ to a smaller one, thus gaining more SURGEs.  
  
The hacker exploited five times in five different transactions and gained 13,112 BNBs in total (with ~$5.57M). The funds were transferred to Ethereum via Binance Bridge.


Proof Links:
- [https://twitter.com/peckshield/status/1427504583971155989](https://twitter.com/peckshield/status/1427504583971155989)
- [ https://twitter.com/XSURGEDEFI/status/1427388385853943812]( https://twitter.com/XSURGEDEFI/status/1427388385853943812)


