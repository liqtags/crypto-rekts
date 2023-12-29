# BurgerSwap
![BurgerSwap](/rektimages/BurgerSwap.png)
- Amount Lost: $7,200,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-5-29

**Quick Summary**

An attacker exploited BurgerSwap using flash loans and a fake token, resulting in a loss of $7.2 million.

 **  
**

 **Details of the Exploit**

The attacker initiated a flash swap of 6k WBNB ($2M) from PancakeSwap, which was then swapped for 92k BURGER on BurgerSwap. The attacker then created a non-standard BEP-20 token and formed a new trading pair with BURGER. Using this pair, the attacker swapped 100 fake tokens for 4.4k WBNB, and then swapped 45k BURGER for another 4.4k WBNB. The attacker then swapped 493 WBNB for 108.7k BURGER on BurgerSwap, before finally repaying the flash swap.

 **  
**

 **Block Data Reference**

The attacker's transaction:

https://bscscan.com/tx/0xf598e092ab82ce08798f9dab7ea6ade64f152aa91db897f3449b23ab591baa1d


Proof Links:
- [https://rekt.news/burgerswap-rekt/](https://rekt.news/burgerswap-rekt/)
- [ https://twitter.com/burger_swap/status/1398161871778115586]( https://twitter.com/burger_swap/status/1398161871778115586)
- [ https://www.coindesk.com/burgerswap-flash-loan-attack]( https://www.coindesk.com/burgerswap-flash-loan-attack)


