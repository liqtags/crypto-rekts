# Tinyman
![Tinyman](/rektimages/Tinyman.png)
- Amount Lost: $3,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-1-1

The attacker's address:  
https://algoexplorer.io/address/RJROFHHDTCMDRCPYSBKN2ATSKZAPOPEV3KWR3IQEOIZMMZCPMMCEUTXGG4  
  
The account’s first attack was this transaction group:  
https://algoexplorer.io/tx/group/KbOlFc02lRAonvc4yfgpI%2FfkNrlP2FDHGX1ESAF2lvs%3D  
  
A weakness in the project's smart contract code permitted the Tinyman hack. When a user invokes the protocol's burn function, they should be rewarded with two different tokens:

https://docs.tinyman.org/design-doc  
  
The value of each token is determined by the quantity contained in the protocol.  
  
The attacker took use of a flaw in the Tinyman pools' contract code, which enabled them to obtain the same token twice after a burn instead of two separate tokens. This worked in their favor since it allowed the attacker to take twice as many gobtc rather than a mixture of gobtc and ALGO tokens. Because gobtc is far more valuable than ALGO, the attacker was able to profit significantly and drain nearly $3 million in gobtc and goeth from the Tinyman pool across numerous transactions. These tokens were then exchanged for stablecoins in pools and withdrawn to various exchanges and wallets.  
  
The original attacker's vulnerability was copied by other wallets that utilized it to attack the protocol. As a result, the Tinyman team advised all users to remove their funds from impacted pools.


Proof Links:
- [https://tinymanorg.medium.com/official-announcement-about-the-incidents-of-01-01-2022-56abb19d8b19](https://tinymanorg.medium.com/official-announcement-about-the-incidents-of-01-01-2022-56abb19d8b19)


