# Orion Protocol
![Orion Protocol](/rektimages/Orion-Protocol.png)
- Amount Lost: $3,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-2-2

**Quick Summary**

Orion protocol was exploited via reentrancy vulnerability with a profit of about 3M $USD.

  


 **Details of the Exploit**

Orion Protocol, a decentralized finance (DeFi) protocol that aggregates liquidity from centralized exchanges, recently suffered a reentrancy exploit that resulted in a loss of around $3 million in Ethereum (ETH) on Feb. 2. The attacker used manipulated swaps of flash loaned stablecoins and artificially deposited assets twice before withdrawing the inflated balance. The exploiter also created and used a fake token to double their balance before making off with the stolen loot. Orion CEO Alexey Koloskov said the damage was contained to an internal broker account, and user funds remained safe. Orion has addressed several issues, such as bug fixes and interface changes, and Rekt reported that the $3 million loss has motivated Orion to take a more controlled approach. 

  


After the attack, 1100 ETH were sent through the tornado cash mixer and 657 ETH are still held in the attacker's balance on the Ethereum network. 

  


 **Block Data Reference**

Exploit TX:

https://bscscan.com/tx/0xfb153c572e304093023b4f9694ef39135b6ed5b2515453173e81ec02df2e2104

  


Exploiter addresses:

https://bscscan.com/address/0x837962b686fd5a407fb4e5f92e8be86a230484bd

https://bscscan.com/address/0x3dabf5e36df28f6064a7c5638d0c4e01539e35f1

https://etherscan.io/address/0x3dabf5e36df28f6064a7c5638d0c4e01539e35f1

  


Attacker contract:

https://bscscan.com/address/0x84452042cb7be650be4eb641025ac3c8a0079b67

  


Example of tornado cash TX:

https://etherscan.io/tx/0xa3fd4f4c4dd4d9a2a1fb8e5267c21b35107ca106cc1b6552a287e3acbad845cb

  


  



Proof Links:
- [https://beincrypto.com/orion-protocol-post-mortem-details-3m-defi-exploit/](https://beincrypto.com/orion-protocol-post-mortem-details-3m-defi-exploit/)
- [ https://cryptoslate.com/orion-protocol-suffers-3m-hack-due-to-third-party-vulnerabilities/]( https://cryptoslate.com/orion-protocol-suffers-3m-hack-due-to-third-party-vulnerabilities/)
- [ https://www.coindesk.com/business/2023/02/02/orion-protocol-loses-3m-of-crypto-in-trading-pool-exploit/]( https://www.coindesk.com/business/2023/02/02/orion-protocol-loses-3m-of-crypto-in-trading-pool-exploit/)
- [ https://twitter.com/peckshield/status/1621342889522642944]( https://twitter.com/peckshield/status/1621342889522642944)
- [ https://twitter.com/alexeykoloskov/status/1621269268959477763?s=20&t=oIA8Mv3AkaYDT5-XjHPpUw]( https://twitter.com/alexeykoloskov/status/1621269268959477763?s=20&t=oIA8Mv3AkaYDT5-XjHPpUw)


