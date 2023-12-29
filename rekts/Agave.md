# Agave
![Agave](/rektimages/Agave.png)
- Amount Lost: $5,500,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-3-15

The attacker's address:  
https://blockscout.com/xdai/mainnet/address/0xD041Ad9aaE5Cf96b21c3ffcB303a0Cb80779E358/transactions  
  
The attacks were made possible due to the xDAI token's architecture, which includes the function _callAfterTransfer_ (), which creates a reentrancy vulnerability.  
  
Using flash loans as collateral, the attacker(s) layered multiple borrow functions within one another, increasing the amount borrowed before the protocol could update the debt balance. Repeating this approach resulted in borrowing assets that were significantly more valuable than the collateral provided.  
  
Stolen funds were bridged to Ethereum and deposited into Tornado Cash mixer:  
https://etherscan.io/txs?a=0xd041ad9aae5cf96b21c3ffcb303a0cb80779e358


Proof Links:
- [https://twitter.com/Agave_lending/status/1503725275917565954](https://twitter.com/Agave_lending/status/1503725275917565954)
- [ https://rekt.news/agave-hundred-rekt/]( https://rekt.news/agave-hundred-rekt/)
- []()


