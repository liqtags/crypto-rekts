# MetaMoonMars
![MetaMoonMars](/rektimages/MetaMoonMars.png)
- Amount Lost: $866.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-11-30

**Quick Summary**

MetaMoonMars token was exit scammed via Withdrawal Fee issue. The token deployer used a privileged function to set a huge fee multiplier

  


 **Details of the Exploit**

MetaMoonMars is a BEP20 token trading on PancakeSwap. The contract of the token contained privileged function aprove() which sets a fee multiplier. At first, the fee was 8 percent, and after some period the function was called again, setting a fee of 99 percent. Users were not able to buy a fair amount of tokens, and their funds were transferred into the pool. Cause of the huge fee, users couldn't sell the little amount of $M3 token they receive. The scammer profited for 866 $USD.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0xda7e1666ab637609fc2d5833dae1056976a17c96

  


Malicious transactions:

https://bscscan.com/tx/0x93a828726c00f117915ab10489c512b0c39e1ed2dd4c2282c13bddd2b26fdcc0

https://bscscan.com/tx/0xe4095741fdbe2452f5f2ce416fbf012a4ea2549d6b0155ac4871dcbebfdc78d7

  


Tokens transfer transaction:

https://bscscan.com/tx/0x77c2be9454da2b720939254736f941370532d34d8bff4322033c1888f13ce378


Proof Links:
- [https://research.checkpoint.com/2022/scammers-are-creating-new-fraudulent-crypto-tokens-and-misconfiguring-smart-contracts-to-steal-funds/](https://research.checkpoint.com/2022/scammers-are-creating-new-fraudulent-crypto-tokens-and-misconfiguring-smart-contracts-to-steal-funds/)


