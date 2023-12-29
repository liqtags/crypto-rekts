# Libertify
![Libertify](/rektimages/Libertify.png)
- Amount Lost: $452,114.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-7-11

**Quick Summary**

Libertify, a portfolio manager, was exploited due to a reentrancy flaw, resulting in a loss of 452,114 $USD across Ethereum and Polygon chains.

  


 **Details of the Exploit**

The exploit of the Libertify portfolio manager project was due to the absence of reentrancy protection. This allowed the attacker to exploit the deposit() routine, minting more shares and draining funds from both the Ethereum and Polygon chains. 

Approximately $162,527 worth of USDT and WETH was drained from the Ethereum chain, and about $289,587 worth of USDT and WETH was drained from the Polygon chain. The funds stolen from the Polygon chain were then bridged to Ethereum using Celer Bridge. Notably, about 56,234 USDT from the stolen funds on the Polygon chain remains at the malicious contract.

  


 **Block Data Reference**

Attacker Address: 

https://etherscan.io/address/0xfd2d3ffb05ad00e61e3c8d8701cb9036b7a16d02

https://polygonscan.com/address/0xfd2d3ffb05ad00e61e3c8d8701cb9036b7a16d02

  


Malicious Transactions: https://etherscan.io/tx/0xcb0ad9da33ecabf75df0a24aabf8a4517e4a7c5b1b2f11fee3b6a1ad9299a282

https://polygonscan.com/tx/0x7320accea0ef1d7abca8100c82223533b624c82d3e8d445954731495d4388483

  


Malicious Contract Address: https://etherscan.io/address/0xdfcdb5a86b167b3a418f3909d6f7a2f2873f2969

  


Bridging Transaction: https://etherscan.io/tx/0x23eb7c6b76b86a6ee7cd89c5c21b7335d6ece6a389522e6bde128b67c105e10e

  


Malicious Contract Address:

https://etherscan.io/address/0xdfcdb5a86b167b3a418f3909d6f7a2f2873f2969 https://polygonscan.com/address/0xdfcdb5a86b167b3a418f3909d6f7a2f2873f2969


Proof Links:
- [https://twitter.com/peckshield/status/1678688731908411393](https://twitter.com/peckshield/status/1678688731908411393)
- [ https://twitter.com/Phalcon_xyz/status/1678694679767031809]( https://twitter.com/Phalcon_xyz/status/1678694679767031809)


