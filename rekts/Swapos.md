# Swapos
![Swapos](/rektimages/Swapos.png)
- Amount Lost: $464,026.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-4-16

**Quick Summary**

Swapos DEX was exploited on the same day it launched, with 464,026 $USD worth of assets stolen. The exploit was possible due to a vulnerable 'swap' function that allowed anyone to perform malicious swaps and 

fully drain the pool.

  


 **Details of the Exploit**

Swapos is a DEX running on the Ethereum chain. The project offered decentralized trading with low fees. On the day Swapos V2 Contracts were deployed, a vulnerability was discovered in their 'swap' function which allowed an attacker to execute malicious swaps and fully drain all three pools, including SWP/WETH, USDC/WETH, USDC/WBTC. In total, 464,026 $USD worth of assets were stolen from these pools. Interestingly, the exploiter executed a transaction after a hack with a message reading "safe", suggesting they may be a whitehat hacker attempting to bring attention to this vulnerability rather than committing outright theft. Regardless of intent, funds are currently held within the attacker's contract.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x53fc4a4a638378b9b81393fbe0fa9a6de2323ebd

  


Malicious transactions:

https://etherscan.io/tx/0x78edc292af51a93f89ac201a742bce9fa9c5d9a7007f034aa30535e35082d50a

https://etherscan.io/tx/0x4c55ba0b403e63702a0358e66b5b20b79c3ff1d77804d4a887dc5c0d119f1966

https://etherscan.io/tx/0xbe643ccdcae57181b9fef554d63029e0605b2e860172d442c37eaabffdb44575

  


Attacker message:

https://etherscan.io/tx/0x4c37d83fa16994ce09fcb2425b9dcad36feb5cea48366880be0828b01843f624

  


Malicious contract:

https://etherscan.io/address/0x2df07c054138bf29348f35a12a22550230bd1405


Proof Links:
- [twitter.com/certikalert/status/1647530789947469825](twitter.com/certikalert/status/1647530789947469825)


