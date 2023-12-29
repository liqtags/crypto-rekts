# Compound Labs
![Compound Labs](/rektimages/Compound-Labs-2.png)
- Amount Lost: $71,101,556.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2021-9-30

**Quick Summary**

Compound's new proposal caused a loss of 237,000 $COMP tokens due to the smart contract issue

  
 **Details of the Exploit**  
Compound's governance Proposal 62 changed the distribution in the Comptroller contract to liquidity suppliers and borrowers from a previous 50:50 split to new governance proposed ratios:  
https://compound.finance/governance/proposals/62  
  
However, the Comptroller contract contains a bug, causing some users to receive too much COMP. The Comptroller received tokens for distribution from the Reservoir contract at:  
https://etherscan.io/tx/0xe76167796646eb447cf53a72f1b912ad5028e64f8c8129b1a3fb71c1379f2322  
  
84,000,000 in $COMP tokens are at risk  
  
Approximately 237,000 $COMP tokens are already distributed between different addresses and can be calculated as a loss at the current moment.

  


 **Block Data Reference**

The examples of transactions that trigger the bug:  
https://etherscan.io/tx/0xc9244e5349f49f3b74a54a882e71f1ca11ba14ed74f73bf2cd091ed8be2b0001  
https://etherscan.io/tx/0xbc246c878326f2c128462d08a0b74048b1dbee733adde8863f569c949c06422a  
https://etherscan.io/tx/0xd77300cd5f10d835d60aa7560ab6a140887e6f84cc76b7911e83a46293492f94  
https://etherscan.io/tx/0xc9244e5349f49f3b74a54a882e71f1ca11ba14ed74f73bf2cd091ed8be2b0001  
https://etherscan.io/tx/0x0fefe4a123e9137e7725e07166ddd0e29e8e4a2e3f71d788c6edec6bf13b45c1  
https://etherscan.io/tx/0xf3731f0e45a2a14fa93345453f10c793b29b707a92cb50d05a7ec5a4d280a973  
https://etherscan.io/tx/0xb6d5122afe04a9905adc5de7f708cabc5821e65fb7d6f0bfd571d35b1ddab7f2  
https://etherscan.io/tx/0xf4bfef1655f2092cf062c008153a5be66069b2b1fedcacbf4037c1f3cc8a9f45  
https://etherscan.io/tx/0xee318650ae8bcf83517e77e8654d40201990080fcb888087f737aea28e70bdb1

  


Comptroller contract:  
https://etherscan.io/address/0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b  
  
Reservoir contract:  
https://etherscan.io/address/0x2775b1c75658be0f640272ccb8c72ac986009e38  
  
List of addresses, which claimed a huge amount of tokens:  
https://twitter.com/0xngmi/status/1443442885618278407

  



Proof Links:
- [https://archive.is/mj73m](https://archive.is/mj73m)
- [ https://twitter.com/rleshner/status/1443380518498848768]( https://twitter.com/rleshner/status/1443380518498848768)
- [ https://beincrypto.com/compound-finance-update-bug-distribution/]( https://beincrypto.com/compound-finance-update-bug-distribution/)
- [ https://www.coindesk.com/tech/2021/09/30/defi-money-market-compound-overpays-15m-in-comp-rewards-in-possible-exploit/]( https://www.coindesk.com/tech/2021/09/30/defi-money-market-compound-overpays-15m-in-comp-rewards-in-possible-exploit/)


