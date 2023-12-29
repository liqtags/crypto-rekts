# Exactly Protocol
![Exactly Protocol](/rektimages/Exactly-Protocol.png)
- Amount Lost: $7,197,240.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2023-8-18

**Quick Summary**

Exactly Protocol suffered a reentrancy attack, resulting in the loss of 4332.92 ETH, valued at approximately 7,197,240 $USD.

  


 **Details of the Exploit**

On August 18, 2023, Exactly Protocol, a lending and borrowing protocol operating on the Optimism chain, was exploited through a reentrancy attack. The attacker bypassed the permit check in the DebtManager contract's leverage function by using a fake market address without validation and changing the msg.sender to the victim's address. They then reentered the crossDeleverage function and stole the collaterals.

  


The stolen funds, a total of 4332.92 ETH, were bridged to the Ethereum mainnet, partly through the Across Protocol and partly via the Optimism Bridge. The value of the loss was approximately 7,197,240 $USD.

  


The Exactly:Deployer sent an on-chain message to the exploiter, expressing willingness to discuss the incident and providing instructions for private communication.

  


 **Block Data Reference**

Optimism:

Attacker Addresses:

1\. https://optimistic.etherscan.io/address/0x3747dbbcb5c07786a4c59883e473a2e38f571af9

2\. https://optimistic.etherscan.io/address/0xE4f34a72d7c18b6f666d6cA53fBC3790bc9da042

  


Malicious Transactions:

1\. https://optimistic.etherscan.io/tx/0xe8999fb57684856d637504f1f0082b69a3f7b34dd4e7597bea376c9466813585

2\. https://optimistic.etherscan.io/tx/0x1526acfb7062090bd5fed1b3821d1691c87f6c4fb294f56b5b921f0edf0cfad6

3\. https://optimistic.etherscan.io/tx/0x3d6367de5c191204b44b8a5cf975f257472087a9aadc59b5d744ffdef33a520e

  


Malicious Contract:

https://optimistic.etherscan.io/address/0x6dd61c69415c8ecab3fefd80d079435ead1a5b4d

  


Bridging Transaction:

https://optimistic.etherscan.io/tx/0x27f0fd9584f1307a1e7aee8671276681b7e5a093a4bdfecf79af2fbe948b8a31

  


Ethereum:

Funds Holder:

https://etherscan.io/address/0xE4f34a72d7c18b6f666d6cA53fBC3790bc9da042

  


Bridging Transaction:

https://etherscan.io/tx/0x77461e8087bdde8f42ced1c6486aca85fdb91769dcee426b3ac1187e9b826849

  


Onchain Message:

https://etherscan.io/tx/0x91dd9c55e1d51f7ada448b2aec4552d9bbf5aa02b33f796d29509e4e0b2fe3d1


Proof Links:
- [https://twitter.com/ExactlyProtocol/status/1692509323690184966](https://twitter.com/ExactlyProtocol/status/1692509323690184966)
- [ https://beincrypto.com/exactly-protocol-hackers-steal-7m/]( https://beincrypto.com/exactly-protocol-hackers-steal-7m/)


