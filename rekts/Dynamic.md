# Dynamic
![Dynamic](/rektimages/Dynamic.png)
- Amount Lost: $22,400.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2023-2-22

**Quick Summary**

Dynamic Finance suffered a reentrancy bug attack on February 22, 2023, resulting in a loss of 73 BNB, approximately $22,400.

  


 **Details of the Exploit**

Details of the Exploit: The attacker used a reentrancy bug that tricked the deposit tracking system of the StakingDYNA contract. By taking out a large flash loan to borrow $DYNA and depositing it before redeeming the deposit, the attacker was able to earn rewards and pay back the flash loan, resulting in a profit. After withdrawing funds from one address, the attacker transferred the funds to the next address for the same operation, allowing them to profit multiple times.

  


 **Block Data Reference**

Attacker:

https://bscscan.com/address/0x0c925a25fdaac4460cab0cc7abc90ff71f410094

  


  



Proof Links:
- [https://neptunemutual.com/blog/how-was-dynamic-finance-exploited/](https://neptunemutual.com/blog/how-was-dynamic-finance-exploited/)
- [ https://twitter.com/CertiKAlert/status/1628274049154531329]( https://twitter.com/CertiKAlert/status/1628274049154531329)
- [ https://twitter.com/BeosinAlert/status/1628301635834486784]( https://twitter.com/BeosinAlert/status/1628301635834486784)


