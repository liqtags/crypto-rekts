# Harvest Keeper
![Harvest Keeper](/rektimages/Harvest-Keeper.png)
- Amount Lost: $929,595.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2023-3-17

**Quick Summary**

Harvest Keeper was rugpulled via privileged function. 929,595 $USD were stolen in total across three chains.

  


 **Details of the Exploit**

Harvest Keeper claimed to be an AI-powered trading platform running on Binance, Ethereum, and Polygon chains. The platform was rugpulled by the contract owner via the privileged function getAmount(). The function allowed the contract owner to drain all remaining $USDT from the project's contract. 710,595 $USDT was siphoned out in a single transaction this way. 219,000 $USD worth of assets were stolen via ice phishing and then exploiting user approvals across Binance, Ethereum, and Polygon chains in addition. All the stolen funds were transferred through multiple EOA addresses.

  


 **Block Data Reference**

Attacker addresses:

https://bscscan.com/address/0x027c83d22ae5390367b34b94dcbf0443e495ade8

https://bscscan.com/address/0x250ce5a8d8a8f0345fb8708e0575c8ede7710c14

  


Malicious transaction:

https://bscscan.com/tx/0x3c9e53a91cde4a366d02692a94128e28e71e86a51d2cb546b70142add4a8809b

  


Approval exploits transaction example:

https://bscscan.com/tx/0x12f1def80ec4593c4e303fd8b3d8a7d95da9e3fdaacb41f2ad5a7a1ac9896f7a


Proof Links:
- [https://beincrypto.com/ai-harvest-keeper-dapp-rugpulls-draining-1m-users-funds/](https://beincrypto.com/ai-harvest-keeper-dapp-rugpulls-draining-1m-users-funds/)
- [ https://twitter.com/CertiKAlert/status/1637470777355165696]( https://twitter.com/CertiKAlert/status/1637470777355165696)


