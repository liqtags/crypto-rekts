# DarkPool
![DarkPool](/rektimages/DarkPool.png)
- Amount Lost: $103,859.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-9-10

**Quick Summary**

Dark Pool token was hacked and 103,859 $USD was stolen from the liquidity pool. The hacker used the vulnerability of the token's smart contract.

  


 **Details of the Exploit**

Dark Pool is the BEP20 standard token trading on PancakeSwap. The smart contract of the $DPC token has a vulnerability, which allows users to accumulate a huge amount of rewards after staking LP tokens. The claimStakeLP() function was called multiple times by the attacker's malicious contracts and granted the attacker the opportunity to withdraw more than 20,000 $DPC tokens. Consequently, the attacker swapped $DPC tokens for $USDT and made a profit of 103,859 $USD. All stolen funds remain in the attacker's address at the moment of writing.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0xf211Fa86CBc60d693D687075B03dFF3c225b25C9

Attacker contract:

https://bscscan.com/address/0x2109bbecb0a563e204985524dd3db2f6254ab419

Draining transaction:

https://bscscan.com/tx/0x92cab23d536d2e13ecb7c473350121165de0ae6c6c81be94ba502ac7db72e86f

Liquidity Pool:

https://bscscan.com/address/0x79cd24ed4524373af6e047556018b1440cf04be3

  



Proof Links:
- [https://en.0xzx.com/beosin-analysis-of-dpc-token-contracts-on-bnbchain-hacked-by-hackers/](https://en.0xzx.com/beosin-analysis-of-dpc-token-contracts-on-bnbchain-hacked-by-hackers/)
- [ https://twitter.com/BeosinAlert/status/1568429367306616832]( https://twitter.com/BeosinAlert/status/1568429367306616832)


