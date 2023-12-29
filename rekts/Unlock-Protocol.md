# Unlock Protocol
![Unlock Protocol](/rektimages/Unlock-Protocol.png)
- Amount Lost: $38,300.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2023-4-21

**Quick Summary**

On the 21th of April we has detected a security breach aimed at UnlockProtocol that resulted in a significant loss of more than 20 ETH. 

  


 **Details of the Exploit**

The root cause of this breach is related to the "postLockUpgrade()" function in the implementation contract 0xdcb2f7d1fb126a166e7168e1d84e415b3ffd6b93, which failed to verify the caller.

  


During the preparation phase of the attack, the attacker called the "postLockUpgrade()" function in transaction 0x4ac413c3c6edd445d1f09cd770d6aafab19b0b58fde7d0cefc74e17265033ef6. The purpose of this function call was to set the "locks[<0xac08>].deployed" parameter to True, allowing the attacker to pass the "onlyFromDeployedLock()" check on the "recordKeyPurchase()" function in the subsequent transaction.

  


It should be noted that an accomplice address, 0x3a6833329fc1bd0b867413045c5f6da3cb0e3c0e, was used to deposit 16 ETH into Tornado. The attacker used this address to obfuscate their tracks and make it more difficult to track the flow of funds.

  


 **Block Data Reference**

Exploiter contract:

https://etherscan.io/address/0xac08f1af4131480cc41ae89c80a63e578a152e84

Exploiter:

https://etherscan.io/address/0x43ee4169d9ff5e5b10ca42923b1e5d07a157bb71


Proof Links:
- [https://twitter.com/AnciliaInc/status/1649270348716867586](https://twitter.com/AnciliaInc/status/1649270348716867586)


