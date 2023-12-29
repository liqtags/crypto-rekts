# ShadowFi
![ShadowFi](/rektimages/ShadowFi.png)
- Amount Lost: $302,817.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-9-2

**Quick Summary**

The ShadowFi project was exploited by a hacker who took advantage of a vulnerability in the $SDF token, making a profit of 1078 $BNB.

  


 **Details of the Exploit**

ShadowFi is a BEP20 token focused on anonymous payments, NFT, and passive income. The hack proceeds in two parts.

In the first part, the hacker used a scanner to track new token pairs, and stole $WBNB on PancakePair contract. 

In the second part, another attacker used the burn function, which mistakenly allows any user to burn $SDF tokens from any address. The attacker burns almost all $SDF tokens on the liquidity pool, so the token price was unfairly high. He deployed an exploit smart contract to use the situation to swap 9 $SDF tokens for 1078 $WBNB and made a profit of 302,817 $USD. Consequently, he swapped all the stolen funds and transferred them to Tornado Cash.

  


 **Block Data Reference**

Affected address of token pair:

https://www.bscscan.com/address/0xf9e3151e813cd6729d52d9a0c3ee69f22cce650a

Address of attacker:

https://bscscan.com/address/0x6478576716666758401168757460978685492205

Swap transaction:

https://www.bscscan.com/tx/0xe30dc75253eecec3377e03c532aa41bae1c26909bc8618f21fb83d4330a01018

  



Proof Links:
- [https://archive.is/TjFOQ](https://archive.is/TjFOQ)


