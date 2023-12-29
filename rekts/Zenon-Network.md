# Zenon Network
![Zenon Network](/rektimages/Zenon-Network.png)
- Amount Lost: $1,209,467.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-11-20

The attacker's address:  
https://bscscan.com/address/0x53d4307d7cc1e1b728c0678618efe10a339c18fd  
  
The transaction behind the attack:  
https://bscscan.com/tx/0xc14ae484b49a346fca9bb414e302c6a9ad0e16fc085c8e197ac7ae85df5727fc  
  
The Zenon Network hack was made possible by an unprotected burn function within the smart contract. Zenon Network left external access to the _burn_ () function:  
https://twitter.com/peckshield/status/1462165620506742784  
  
The attacker deposited tokens in the protocol’s pool for wrapped ZNN (wZNN) tokens and then called the burn function to destroy over 26k wZNN tokens. This decreased the supply of wZNN tokens, increasing their value dramatically.  As a result, when the attacker redeemed his wZNN tokens, the pool believed that he was owed a massive number of WBNB tokens, enabling him to drain the pool. Stolen funds were deposited into the Tornado Cash mixer.


Proof Links:
- [https://twitter.com/Zenon_Network/status/1462092022098059280](https://twitter.com/Zenon_Network/status/1462092022098059280)
- [ https://halborn.com/explained-the-zenon-network-hack-november-2021/]( https://halborn.com/explained-the-zenon-network-hack-november-2021/)


