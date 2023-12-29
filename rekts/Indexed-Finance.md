# Indexed Finance
![Indexed Finance](/rektimages/Indexed-Finance.png)
- Amount Lost: $16,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-10-14

**Quick Summary**

The DEFI5 and CC10 index tokens were exploited using flash loans, resulting in a loss of approximately $156 million.

  


 **Details of the Exploit**

The attacker targeted the DEFI5 and CC10 index tokens using flash loans of other assets in the pool to buy out UNI, which decreased the extrapolated value due to the delay in updating UNI’s weight decrease. The pool was valued at 29,851 SUSHI ($300k) after executing the updateMinimumBalance function with the gamed pool value. The attacker then deposited small amounts of SUSHI into the pool, resulting in a massively inflated amount of DEFI5 tokens. Approximately $156m worth of flash swaps in UNI, AAVE, COMP, CRV, MKR, SNX were used for dumping tokens in the pool, minting new DEFI5 tokens, and then burning the DEFI5 for all of the underlying assets. The same scenario was used for the CC10 index pool.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0xba5ed1488be60ba2facc6b66c6d6f0befba22ebe

  


The exploiter contract:

https://etherscan.io/address/0xfbc2e6b188013fc5eacd9944e6b8ced2c467464a

  


The attack targeted the DEFI5 index token at:

https://etherscan.io/tx/0x44aad3b853866468161735496a5d9cc961ce5aa872924c5d78673076b1cd95aa

  


and CC10 index token at:

https://etherscan.io/tx/0xbde4521c5ac08d0033019993b0e7e1d29b1457e80e7743d318a3c27649ca4417


Proof Links:
- [https://ndxfi.medium.com/indexed-attack-post-mortem-b006094f0bdc](https://ndxfi.medium.com/indexed-attack-post-mortem-b006094f0bdc)
- [ https://rekt.news/indexed-finance-rekt/]( https://rekt.news/indexed-finance-rekt/)


