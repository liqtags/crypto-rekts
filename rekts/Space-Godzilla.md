# Space Godzilla
![Space Godzilla](/rektimages/Space-Godzilla.png)
- Amount Lost: $26,153.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-7-13

**Quick Summary**

The $SpaceGodzilla token has been subjected to a Flash Loan Attack. During this attack, the attacker made a profit of more than $26K.

  


 **Details of the Exploit**

[](https://www.youtube.com/watch?v=U4xMcd_1mKY)

The $SpaceGodzilla token was exposed to the flash loan attack. During the analysis of transactions, the course of the attack was revealed. The attacker borrowed flash loans for $USDT, which he then exchanged for $SpaceGodzilla to raise its value. Then the attacker calls the swapAndLiquifyStepv1() function, which invests both $USDT and $SpaceGodzilla in an unbalanced pool, as a result of which he can exchange the $SpaceGodzilla token for $USDT. Ultimately, the attacker repays the loans and takes a profit of $26k. $25k was transferred to scammer's contract address (https://bscscan.com/tx/0xa74e446aaf0b34a34a4193bda036820944ededbf4d151dcf9757294480c13f4e)

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Exploiter address: https://bscscan.com/address/0x00a62eb08868ec6feb23465f61aa963b89e57e57

Exploiter contract addresses: 

1) https://bscscan.com/address/0x3d817ea746edd02c088c4df47c0ece0bd28dcd72

2) https://bscscan.com/address/0x05ad60d9a2f1aa30ba0cdbaf1e0a0a145fbea16f

Exploit transactions:

1) https://bscscan.com/tx/0x7f183df11f1a0225b5eb5bb2296b5dc51c0f3570e8cc15f0754de8e6f8b4cca4

2) https://bscscan.com/tx/0x67ba949a3fa10bea9ab78b6bb0866bef81370c269debcbae920692bc2081bdeb


Proof Links:
- [https://dexscreener.com/bsc/0x8aff4e8d24f445df313928839ec96c4a618a91c8](https://dexscreener.com/bsc/0x8aff4e8d24f445df313928839ec96c4a618a91c8)


