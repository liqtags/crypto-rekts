# Elephant Money
![Elephant Money](/rektimages/Elephant-Money.png)
- Amount Lost: $22,200,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-4-12

**Quick Summary**

The $TRUNK token's redemption mechanism was exploited by an attacker who manipulated the price oracle to enable token return, resulting in the theft of ELEPHANT from the unverified Treasury contract.

  


 **Details of the Exploit**

The attacker initially borrowed 131,162 WBNB and 91,035,000 BUSD via a flash loan. They then exchanged the 131,162 WBNB for 34,244 ELEPHANT Tokens. The attacker then manipulated the minting contract to swap BUSD for WBNB, which was used to buy back ELEPHANT tokens at an increased market value. The ELEPHANT tokens were then swapped back to WBNB, resulting in 34,244 ELEPHANT exchanged on 163,782.82 WBNB. The attacker then redeemed TRUNK for 36,987.33 WBNB and 66,884,140.12 BUSD. After repaying the flash loans, the attacker made a profit of $4M.

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/tx/0xf678370cf3ee8d5df5ae319577b46bf3834ec6ffb44f2c1ebe86ed702b0b22a2

The transaction behind the attack:

https://bscscan.com/tx/0xec317deb2f3efdc1dbf7ed5d3902cdf2c33ae512151646383a8cf8cbcd3d4577


Proof Links:
- [https://medium.com/elephant-money/reserve-exploit-52fd36ccc7e8](https://medium.com/elephant-money/reserve-exploit-52fd36ccc7e8)
- [ https://twitter.com/CertiKAlert/status/1514345918564286482]( https://twitter.com/CertiKAlert/status/1514345918564286482)
- [ https://twitter.com/peckshield/status/1514023036596330496]( https://twitter.com/peckshield/status/1514023036596330496)
- []()


