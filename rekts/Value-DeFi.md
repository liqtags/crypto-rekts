# Value DeFi
![Value DeFi](/rektimages/Value-DeFi.png)
- Amount Lost: $11,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-5-7

**Quick Summary**

Exploit in Bancor formula allows an attacker to drain multiple tokens from pair contracts.

  


 **Details of the Exploit**

The attacker initiated the exploit by sending a small amount of a second token to pair addresses. They then made a swap, intending to withdraw a small amount of the first token and a large amount of the second token. Due to an incorrect implementation of the Bancor formula, the pair contracts deemed the swap successful. The attacker then swapped the first tokens for the second in the same pool and repeated this operation until the exploit was exhausted. The stolen funds included 15k BNB, 2.7k FARM, 1.7k BASv2, 8.5M BDO, 68.3k BUSD, 41.4k MDG, 945k VBOND, 1.2M BAC, and 11k FIRO.

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/address/0x2b528a28451e9853f51616f3b0f6d82af8bea6ae#tokentxns

The transaction behind the attack:

https://bscscan.com/tx/0x2fd0aaf0bad8e81d28d0ee6e4f4b5cbba693d7d0d063d1662653cdd2a135c2de


Proof Links:
- [https://twitter.com/FrankResearcher/status/1390905494844313602?s=20](https://twitter.com/FrankResearcher/status/1390905494844313602?s=20)
- [ https://twitter.com/CryptoBethany/status/1390880003261288448?s=19]( https://twitter.com/CryptoBethany/status/1390880003261288448?s=19)
- [ https://rekt.news/value-rekt3/]( https://rekt.news/value-rekt3/)
- [ https://peckshield.medium.com/valuedefi-incident-incorrect-weighted-constant-product-invariant-calculation-1bbaa220a02b]( https://peckshield.medium.com/valuedefi-incident-incorrect-weighted-constant-product-invariant-calculation-1bbaa220a02b)


