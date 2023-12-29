# GDS Chain
![GDS Chain](/rektimages/GDS-Chain.png)
- Amount Lost: $187,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-1-3

**Quick Summary**

On January 3, 2023, a flash loan attack occurred on the GDS chain, resulting in a total loss of $187,000 and an 84% decline in the price of GDS currency.

  


 **Details of the Exploit**

The attacker, identified by their address as 0xcf2362, used a flash loan to borrow 2.38 million $USDT and traded 0.6 million $USDT for 3.4 million $GDS tokens using a pancake swap. The attacker then obtained a large amount of LP tokens using the remaining $1.7 million in USDT from the liquidity pool. There was a flaw in the "_lpRewardAmount" calculation function that the attacker misused to collect the profits from the $GDS token contract and then transfer the LP tokens to another contract 70 times to earn higher rewards until the flash loan was repaid.

  


 **Block Data Reference**

Attacker’s address: https://bscscan.com/address/0xcf2362b46669e04b16d0780cf9b6e61c82de36a7

Attacker’s transaction: https://bscscan.com/tx/0x2bb704e0d158594f7373ec6e53dc9da6c6639f269207da8dab883fc3b5bf6694

Attacker’s remaining balance: https://bscscan.com/tokenholdings?a=0xcf2362b46669e04b16d0780cf9b6e61c82de36a7

GDS Pool closed after the attack: https://bscscan.com/tx/0x06d23624bd1edeb63665f41c4d3dd098d4c913a715c7b6fd9894575dcb0f43dc

10.3M $GDS tokens reward: 0x43b487c


Proof Links:
- [https://blog.solidityscan.com/gds-chain-hack-analysis-flash-loan-exploit-c175772dec74](https://blog.solidityscan.com/gds-chain-hack-analysis-flash-loan-exploit-c175772dec74)


