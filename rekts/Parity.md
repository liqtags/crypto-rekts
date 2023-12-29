# Parity
![Parity](/rektimages/Parity.png)
- Amount Lost: $155,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2017-11-8

**Quick Summary**

513,000 $ETH has been locked and maintained unreachable on Parity contracts after the user accidentally killed it.

  


 **Details of the Exploit**

On November 6th, 2017, Github user devops199 posted the following statement under the Github issues section of the Parity Multi-Sig Library: “I accidentally killed it”:  
https://github.com/openethereum/parity-ethereum/issues/6995  
  
Just moments earlier, devops199 exploited a vulnerability within the smart-contract library code, blocking funds in 587 wallets holding a total of 513,774.16 Ether as well as various other tokens.  
  
On November 6th, the transaction was sent to WalletLibrary, which called the _initWallet_ method:  
https://etherscan.io/tx/0x05f71e1b2cb4f03e547739db15d080fd30c989eda04d37ce6264c5686e0722c9  
  
This transaction ended up making the 0xae7168deb525862f4fee37d987a971b385b96952 the sole owner. The transaction, which called the _kill_ method of _WalletLibrary_ with 0xae7168deb525862f4fee37d987a971b385b96952 as the beneficiary address:  
https://etherscan.io/tx/0x47f7cff7a5e671884629c93b368cb18f58a993f4b19c2a53a8662e3f1482f690  
  
Approximately 30 minutes later, Devops199 created Parity issue #6995 to document what had just occurred:  
https://github.com/openethereum/parity-ethereum/issues/6995  
  
Devops199 posted a link to the issue in the Parity gitter channel, asking “Is this serious issue?” He then followed up by asking “Will I get arrested for this?”. It seemed as though Devops199 failed to understand the consequences of what he had done, by stating “I’m eth newbie..just learning”.

  
About three hours later, Parity released a warning on Twitter:  
https://twitter.com/ParityTech/status/927850992145719296


Proof Links:
- [https://hackernoon.com/parity-wallet-hack-2-electric-boogaloo-e493f2365303](https://hackernoon.com/parity-wallet-hack-2-electric-boogaloo-e493f2365303)
- [ https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7/]( https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7/)
- [ https://twitter.com/ParityTech/status/927850992145719296]( https://twitter.com/ParityTech/status/927850992145719296)


