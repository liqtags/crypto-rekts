# New Free DAO
![New Free DAO](/rektimages/New-Free-DAO.png)
- Amount Lost: $1,250,372.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-9-8

**Quick Summary**

The New Free DAO project was subjected to a flash loan attack, suffering losses of $1.25M.

  


 **Details of the Exploit**

New Free DAO is a DAO project that give participants the opportunity to coordinate activities and manage resources in accordance with a pre-agreed and formalized set of rules.

The attackers took 250 $WBNB via flash loan and swapped the loaned funds for $NFD tokens via the $WBNB -> $USDT -> $NFD path. 

The attackers contract then created multiple contracts to claim airdrop rewards from the targeted victim contracts. 

The attacker returned the flash loan and swapped all the $NFD for $WBNB. Then the malicious actor swapped 2k $BNB for $USDT.

Step by step the transaction occurred as follows:  
\- The scammer took a flash loan for $250 $BNB  
\- The $BNB tokens were then exchanged for the $NFD tokens  
\- The scammer contract had the ability to create malicious contracts that also created contracts and transferred them all tokens received from airdrop.  
\- In the end, the last contract exchanges the entire balance of $NFD tokens for $BNB, transfers them to the main contract, restores the flash loan, and then the main contract transfers the funds to the scammer.  
  
All the stolen funds have been transferred through tornado.cash.

  


 **Block Data Reference**

Attacker address: https://bscscan.com/address/0x22c9736d4fc73a8fa0eb436d2ce919f5849d6fd2

Attacker contract address: https://bscscan.com/address/0xa35ef9fa2f5e0527cb9fbb6f9d3a24cfed948863

Flash Loan attack transactions:

1) https://bscscan.com/tx/0xb6f9b5ef1feeadb379a2de8f79bb04dd6920bfb214136d057eed4ce23a0003f8

2) https://bscscan.com/tx/0x8b77d75efa185295b09bdf2edcb509541fdde40ed5484212331ceac41b2f4ac0

Swap NFD to BNB transactions:

1) https://bscscan.com/tx/0x8c035fc9c3d944b3dd4a0ea721c119240cb624e79b7625a16173ad6682410599

2) https://bscscan.com/tx/0xda4b4de6ecacfe9b8b60167a2010630aeec103ab51920eb2e1b94ba1fef6c95b

  


Pair address: https://bscscan.com/address/0x26c0623847637095655b2868c3182b2285bdaeaf


Proof Links:
- [https://beincrypto.com/new-free-dao-crashes-99-reported-flash-loan-attack/](https://beincrypto.com/new-free-dao-crashes-99-reported-flash-loan-attack/)


