# Themis Protocol
![Themis Protocol](/rektimages/Themis-Protocol.png)
- Amount Lost: $367,748.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2023-6-27

**Quick Summary**

Themis Protocol suffered a flashloan exploit which leads to a $367,748 USD loss in various assets.

  


 **Details of the Exploit**

Themis Protocol, an Arbitrum-based lending protocol, fell victim to a flash loan attack. The attacker deployed a malicious contract with unverified source code which allowed them to exploit multiple pools of the Themis Protocol, including tArbWETH, tArbUSDC, tArbARB, tArbWBTC, tArbDAI, and tArbUSDT. The stolen assets were swapped to ETH, USDT, and USDC within the same transaction. The attacker manipulated prices and gained 94.32 ETH ($178,453), 130,471 USDC, and 58,824 USDT, amassing a total of $367,748. The stolen funds were then bridged to the Ethereum Mainnet and subsequently transferred through TornadoCash.

  


 **Block Data Reference**

Attacker address:

https://arbiscan.io/address/0xdb73eb484e7dea3785520d750eabef50a9b9ab33

  


Malicious contract: 

https://arbiscan.io/address/0x05a1b877330c168451f081bfaf32d690ea964fca

  


Malicious transaction:

https://arbiscan.io/tx/0xff368294ccb3cd6e7e263526b5c820b22dea2b2fd8617119ba5c3ab8417403d8

  


TornadoCash transfer transaction:

https://etherscan.io/tx/0x6555191198bca4df0789772a35bd1112144234f55a870a9add5b5bfcd198ab3a


Proof Links:
- [https://twitter.com/peckshield/status/1673778002373509121?s=20](https://twitter.com/peckshield/status/1673778002373509121?s=20)


