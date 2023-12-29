# XCarnival
![XCarnival](/rektimages/XCarnival.png)
- Amount Lost: $3,837,110.00
- Funds Returned: $1,746,801.00
- Category: Borrowing and Lending,NFT
- Date: 2022-6-26

**Quick Summary**

XCarnival was attacked by a hacker for 3,087 $ETH of which 1,467 $ETH was returned to the creator address of the vulnerable contract.

  


 **Details of the Exploit**

The attacker created a contract, with the help of which it was just the same that managed to carry out the attack and pump out 3k $ETH from the victim's contract.

Contract creation transaction: https://etherscan.io/tx/0xe4f99b2fb86a317eb16f7f288fda74ab07f0ffcbf645fb3b1a6490ca23206d09

The attacker called the pledgeAndBorrow() function, which creates an orderID and calls xToken.borrow. The function marks that the order has been borrowed. However, an attacker can control xToken, so an attacker can transfer an NFT with a fake xToken, and then borrow all the assets. When the attacker received $ETH, 2,967 was sent to another address where some of the tokens were withdrawn via Tornado.cash.  
Transfer transaction to another address: https://etherscan.io/tx/0x7687857bbb7501741bbe00ddabd6ee3f0a3a61fbc4260608a984e7f2862a2f49

Half of the tokens were returned to the creator of the XCarnival contract in this transaction: https://etherscan.io/tx/0xcc3fda1e5540486de15f707ccc82a6f9c8c78e0ef3ef02e4318b3bea24ace701

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Attack transaction where $3,087 $ETH was withdrawn: https://etherscan.io/tx/0x51cbfd46f21afb44da4fa971f220bd28a14530e1d5da5009cfbdfee012e57e35

XCarnival Exploiter address: https://etherscan.io/address/0xb7cbb4d43f1e08327a90b32a8417688c9d0b800a

Exploiter contract address: https://etherscan.io/address/0xf70f691d30ce23786cfb3a1522cfd76d159aca8d

Victim address: https://etherscan.io/address/0x39360ac1239a0b98cb8076d4135d0f72b7fd9909

  


Example transactions of funds withdrawal via Tornado.cash:

1) https://etherscan.io/tx/0xf8eb760b44ab8fff8fd385ed0fe013b776c10b47271335b754dbbdf5aab21eb0

2) https://etherscan.io/tx/0xf6ffbc99369865d703b8b949b668123fef9ca3fcdb43919a6b524b39d401ca87

3) https://etherscan.io/tx/0xd6be8d7fead1a0901e70697ffbffa96ab687208f5eef986bc6e9e29415668a0d

  


The transaction of the return of 1,467 $ETH to the XCarnival creator: https://etherscan.io/tx/0xcc3fda1e5540486de15f707ccc82a6f9c8c78e0ef3ef02e4318b3bea24ace701


Proof Links:
- [https://xcarnival-lab.medium.com/xcarnival-has-got-1-467-eth-back-the-security-agencies-have-tentatively-determined-the-hackers-3ea05ad134ae](https://xcarnival-lab.medium.com/xcarnival-has-got-1-467-eth-back-the-security-agencies-have-tentatively-determined-the-hackers-3ea05ad134ae)
- [ https://cryptopotato.com/hacked-lending-protocol-xcarnival-receives-1-9m-worth-of-stolen-eth-back/]( https://cryptopotato.com/hacked-lending-protocol-xcarnival-receives-1-9m-worth-of-stolen-eth-back/)


