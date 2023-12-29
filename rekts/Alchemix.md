# Alchemix
![Alchemix](/rektimages/Alchemix.png)
- Amount Lost: $6,500,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-6-18

**Quick Summary**

Alchemix's alETH contracts experienced a bug that allowed users to withdraw their ETH collateral with their alETH loans still outstanding, leading to a community rugpull of $6.5 million.

  


 **Details of the Exploit**

An issue with the deployment script of the alETH vault accidentally created additional vaults, which were used to incorrectly calculate outstanding debts. This led to protocol funds being used to pay off user debts. As a result, users were able to withdraw their ETH collateral with their alETH loans still outstanding. The exploit was discovered and the mint contract for alETH was paused two and a half hours later. No users lost funds as a result of the exploit and Yearn.Finance, whose yield vaults automatically repay Alchemix’s synthetic loans, suffered no loss as well.

  



Proof Links:
- [https://twitter.com/intocryptoast/status/1405252688791498753](https://twitter.com/intocryptoast/status/1405252688791498753)
- [ https://twitter.com/AlchemixFi/status/1405187348678148101]( https://twitter.com/AlchemixFi/status/1405187348678148101)
- [ https://cointelegraph.com/news/alchemix-patches-reverse-rug-exploit-address-6-5-million-shortfall]( https://cointelegraph.com/news/alchemix-patches-reverse-rug-exploit-address-6-5-million-shortfall)


