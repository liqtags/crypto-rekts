# Solend
![Solend](/rektimages/Solend.png)
- Amount Lost: $16,000.00
- Funds Returned: $16,000.00
- Category: Borrowing and Lending
- Date: 2021-8-19

An attacker attempted to exploit the Solend smart contract. They subverted an insecure auth check on the _UpdateReserveConfig()_ function to make accounts with borrows liquidatable and set the borrow APY to 250% for all markets. The attempt to steal funds was detected and stopped by the Solend team in time such that no funds were stolen. A handful of users (5) were liquidated by Solend's liquidator, but those users were refunded out of the liquidator's undue earnings (~16K USD).  
  
The attacker's address:  
https://explorer.solana.com/address/5ELHytHM4cvKUPCWX8HPwkwtw3J866Wtexdpo8PPxp2u  
  
The attacker submitted a total of 10 txs: 9 of them to So1endDq2YkqhipRh3WViPa8hdiSpxWy6z3Z6tMCpAo (the Solend program address) and one of them to Port7uDYB3wk6GJAw4KT1WpTeMtSu9bTcChBHkX2LfR (the Port program address).  
  
The attacker's wallet was funded by 2ojv9BAiHUrvsm9gxDe7fJSzbNZSJcxZvf8dqmWGHG8S which appears to be an exchange wallet.


Proof Links:
- [https://twitter.com/solendprotocol/status/1428611597941891082](https://twitter.com/solendprotocol/status/1428611597941891082)
- []()


