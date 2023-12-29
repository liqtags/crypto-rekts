# CS
![CS](/rektimages/CS.png)
- Amount Lost: $714,285.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-5-23

**Quick Summary**

CS token's pool was exploited via a flash loan attack. The attacker used 80,000,000 $USD to manipulate the token price and made a profit of 714,285 $USD.

  


 **Details of the Exploit**

CS is a BEP20 token trading on PancakeSwap. The token's CS/USD pool was drained via a flash loan attack. The attack started from the malicious contract deployment by the exploiter, which took 80,000,000 $USD as a flash loan from the BSC-USD pool. Consequently, multiple swaps with a small amount of 5,000 $USD was continuously repeated to manipulate the pool's price. After reaching some conditions, the attacker could swap the $CS tokens back with an unfairly high price and the total amount gained back went to 80,954,285 $USD. 240,000 $USD were paid back to the BSC-USD pool as a flash loan fee after the base amount was returned. The exploiter's profit reached 714,285 $USD, which was transferred to the initial EOA, and then distributed between several addresses. All the malicious actions were performed in a single transaction.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0x2cdeee9698ffc9fcabc116b820c24e89184027ba 

  


Malicious transaction:

https://bscscan.com/tx/0x906394b2ee093720955a7d55bff1666f6cf6239e46bea8af99d6352b9687baa4 

  


Malicious contract:

https://bscscan.com/address/0x90fa57d23b85cdd52c46b85636f44c47926ee2e3 


Proof Links:
- [https://twitter.com/DeDotFiSecurity/status/1661092709392629783](https://twitter.com/DeDotFiSecurity/status/1661092709392629783)


