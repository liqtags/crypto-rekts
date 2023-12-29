# Rari Capital
![Rari Capital](/rektimages/Rari-Capital.png)
- Amount Lost: $15,723,948.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-5-8

**Quick Summary**

Rari Capital Ethereum Pool exploited through manipulation of ibETH.totalETH() value, resulting in the withdrawal of more ETH than deposited by the attacker.

  


 **Details of the Exploit**

The attacker initiated the exploit by flash loaning ETH from dYdX and depositing it into the Rari Capital Ethereum Pool. They then manipulated the value of ibETH.totalETH() to artificially inflate it. This allowed them to withdraw more ETH from the Rari Capital Ethereum Pool than they had initially deposited. The value of ibETH.totalETH() returned to its true value at the end of ibETH.work, leaving the Rari Capital Ethereum Pool’s balances lower than before the attack due to the attacker's inflated withdrawal.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0xcb36b1ee0af68dce5578a487ff2da81282512233

The transactions behind the attack:

https://bloxy.info/txs/calls_from/0xcb36b1ee0af68dce5578a487ff2da81282512233?signature_id=1286331&smart_contract_address_bin=0x67b66c99d3eb37fa76aa3ed1ff33e8e39f0b9c7a

The transactions of stolen funds deposited into the Tornado Cash mixer:

https://bloxy.info/txs/calls_from/0xcb36b1ee0af68dce5578a487ff2da81282512233?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://medium.com/rari-capital/5-8-2021-rari-ethereum-pool-post-mortem-60aab6a6f8f9](https://medium.com/rari-capital/5-8-2021-rari-ethereum-pool-post-mortem-60aab6a6f8f9)
- [ https://www.rekt.news/rari-capital-rekt/]( https://www.rekt.news/rari-capital-rekt/)


