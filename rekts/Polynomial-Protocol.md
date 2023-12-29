# Polynomial Protocol
![Polynomial Protocol](/rektimages/Polynomial-Protocol.png)
- Amount Lost: $7,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-11-18

**Quick Summary**

The attacker could drain USDC balances of user addresses that approved their tokens to be spent by the PolynomialZap contract. 

  


 **Details of the Exploit**

The swapAndDeposit() function of the PolynomialZap contract contains a bug: there are no limitations for two input parameters - swapTarget and swapData. This allows anyone to abuse the function and steal tokens approved to the contact. 

All tokens that are approved to the vulnerable contract are still in danger. 

  


 **Block Data Reference**

 

The vulnerable contract: 

[https://optimistic.etherscan.io/address/0xB162f01C5BDA7a68292410aaA059E7Ce28D77c82#code](https://optimistic.etherscan.io/address/0xB162f01C5BDA7a68292410aaA059E7Ce28D77c82#code) 

  


The attack contract:

[https://optimistic.etherscan.io/address/0xf682e302f16c9509ffa133029ccf6de55f4e29a8#code](https://optimistic.etherscan.io/address/0xf682e302f16c9509ffa133029ccf6de55f4e29a8#code) 


Proof Links:
- [https://twitter.com/0xpoor4ever/status/1602156729105788929?s=46&t=tH0vMbOpNhvuOa-6q-f14g](https://twitter.com/0xpoor4ever/status/1602156729105788929?s=46&t=tH0vMbOpNhvuOa-6q-f14g)
- [  https://mobile.twitter.com/PolynomialFi/status/1602260142870896646?cxt=HHwWjICx2YvHr7wsAAAA](  https://mobile.twitter.com/PolynomialFi/status/1602260142870896646?cxt=HHwWjICx2YvHr7wsAAAA)


