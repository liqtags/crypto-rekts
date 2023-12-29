# BRA Token
![BRA Token](/rektimages/BRA-Token.png)
- Amount Lost: $225,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-1-10

**Quick Summary**

On January 10, 2023, BRA token was attacked, and the hacker was able to steal funds worth $225,000 USD.

  


 **Details of the Exploit**

On January 10, 2023, a hack occurred that targeted the BRA token resulting in the theft of funds worth 819 WBNB, which is equivalent to approximately $225,000. The hack was made possible by a logical vulnerability that allowed the attacker to exploit the transfer function, which gave them twice the rewards if the sender and recipient were a pair.

The attacker exploited the vulnerability by obtaining a 1,400 WBNB flash loan before exchanging 1,000 WBNB for 10.5K BRA tokens. They then transferred all the acquired BRA tokens to the Pancakeswap pair. Next, they used the "skim()" function and invoked the BRA contract's transfer function to receive rewards. The "skim()" function acts as a recovery mechanism if the number of tokens supplied to a pair exceeds the two uint112 storage spaces for reserves.

  


In this case, the attacker provided the pair as the recipient address, and BRA reverted to the pair, resulting in the doubling of the BRA amount after a single skim. The attacker repeated this method 100 times, which led to a significant increase in the contract pair's BRA balance.

  


The attacker then returned 1.675K WBNB tokens and repaid the 1.4K WBNB token flash loan, which generated a profit of 675 WBNB that was sent to their address. The attacker carried out the same attack again and took 144 WBNB in profit from the BRA contract.

  


 **Block Data Reference**

Exploit TX:

https://bscscan.com/tx/0x6759db55a4edec4f6bedb5691fc42cf024be3a1a534ddcc7edd471ef205d4047

  


Wallet with funds: 

https://debank.com/profile/0x67a909f2953fb1138beA4B60894B51291D2d0795


Proof Links:
- [https://blog.solidityscan.com/bra-token-hack-analysis-double-the-reward-e82ca060405e](https://blog.solidityscan.com/bra-token-hack-analysis-double-the-reward-e82ca060405e)


