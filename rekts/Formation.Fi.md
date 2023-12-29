# Formation.Fi
![Formation.Fi](/rektimages/Formation.Fi.png)
- Amount Lost: $100,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-11-20

The attacker:  
https://etherscan.io/address/0x89640eb6c8d72606d6a0fff45415bff0ab0e3ae1  
  
The transaction behind the attack:  
https://etherscan.io/tx/0x5c9ac39ca05e51147d60156f085e650370a1e930f9f615f758fecb31deafb6ab  
  
The attack contract:  
https://etherscan.io/address/0xb5aef637d77648c4b937d1be5f6a036f52b1711e  
  
Affected contracts:  
https://bscscan.com/address/0xe2ee850d72d02b3d827b98847d332add0d3f0012  
  
https://etherscan.io/address/0x62931dece3411ada1038c09cd01baa11db08334b  
  
The farming contract has been using the balance of the pool for price discovery of the FORM token and LP token in order to calculate the USD (stable coin) value of the position and pay rewards accordingly.  
  
The Flash Swap mechanism allows to alter the price of the FORM token — the exploit contract used that in order to excessively increase the value of the reward calculated at the withdrawal transaction.  
  
The attacker:  
\- staked LP tokens.

\- pulled available funds from the pool, unstaked LP token, and sent back funds to the pool.  
  
Further exploitation was prevented by devs by setting the multiplier to 0, which makes the contract send no FORMs for any new staked LP tokens:  
https://etherscan.io/tx/0x9aad3091b1f71b8fdb9587aadfec512809dec0d4118e1f2b8922a5e1a263efc8


Proof Links:
- [https://formation-fi.medium.com/greetings-formation-fi-community-supporters-investors-and-friends-b09d673cda8a](https://formation-fi.medium.com/greetings-formation-fi-community-supporters-investors-and-friends-b09d673cda8a)


