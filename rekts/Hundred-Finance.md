# Hundred Finance
![Hundred Finance](/rektimages/Hundred-Finance.png)
- Amount Lost: $6,200,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-3-15

**Quick Summary**

Exploitation of reentrancy vulnerability in xDAI token's architecture allows attackers to borrow assets significantly more valuable than the provided collateral.

  


 **Details of the Exploit**

The attacker exploited the xDAI token's architecture which includes the function callAfterTransfer(), creating a reentrancy vulnerability. By using flash loans as collateral, they were able to layer multiple borrow functions within one another to increase the borrowed amount before the protocol could update the debt balance. This approach was repeated and resulted in the borrowing of assets that were significantly more valuable than the collateral provided.

 **  
**

 **Block Data Reference**

The attacker's address:

https://blockscout.com/xdai/mainnet/address/0xD041Ad9aaE5Cf96b21c3ffcB303a0Cb80779E358/transactions

The stolen funds were bridged to Ethereum and deposited into Tornado Cash mixer:

https://etherscan.io/txs?a=0xd041ad9aae5cf96b21c3ffcb303a0cb80779e358


Proof Links:
- [https://twitter.com/HundredFinance/status/1503754916300476420](https://twitter.com/HundredFinance/status/1503754916300476420)
- [ https://rekt.news/agave-hundred-rekt/]( https://rekt.news/agave-hundred-rekt/)
- [ https://twitter.com/PeckShieldAlert/status/1503927403584061442]( https://twitter.com/PeckShieldAlert/status/1503927403584061442)


