# Feminist Metaverse
![Feminist Metaverse](/rektimages/Feminist-Metaverse.png)
- Amount Lost: $540,000.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2022-5-18

On May 18th, Feminist Metaverse’s FmToken contract was exploited for about 1838 BNB.

  


Attacker transaction: https://bscscan.com/tx/0xfdc90e060004dd902204673831dce466dcf7e8519a79ccf76b90cd6c1c8b320d 

Attacker address: https://bscscan.com/address/0xaaA1634D669dd8aa275BAD6FdF19c7E3B2f1eF50

Attacker contract: https://bscscan.com/address/0x0B8d752252694623766DfB161e1944F233Bca10F

Victim contract: https://bscscan.com/address/0x843528746F073638C9e18253ee6078613C0df0f1

  


Exploit step by step:

1) Attacker directly receives FmToken that is not credited to the liquidity pool using skim function of the SakeSwapPair contract.

2) Attacker transfers 10 FmTokens tokens into an attacking contract to prepare for a subsequent attack.

3) Attacker calls the attack contract, where it cyclically transfer FmToken to the attacker's address, thereby triggering the operation of transferring tokens from the FmToken contract to SakeSwapPair and, finally, transferring them to the attacker's address through the skim function.

4) Multiple transfers of small amounts of FM token to their own address using the created attacker contract 0x0B8d…a10F.

5) Since the FmToken contract balance has reached the standard 150,000 token for transferring to SakeSwapPair, each transfer triggers line 920 to increase the balance of FmToken  to SakeSwapPair. SakeSwapPair thus has a difference between token balance and reserve SakeSwapPair thus has a difference between token balance and reserve.

6) Then attacker calls the skim() function in SakeSwapPair to extract the difference in token balance to his own address.

7) Using PancakeSwap attacker swapped FmToken for BNB


Proof Links:
- [https://twitter.com/FM_Token/status/1526945914061049856?cxt=HHwWgMC-7f_N5rAqAAAA](https://twitter.com/FM_Token/status/1526945914061049856?cxt=HHwWgMC-7f_N5rAqAAAA)


