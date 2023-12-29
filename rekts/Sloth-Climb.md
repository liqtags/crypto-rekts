# Sloth Climb
![Sloth Climb](/rektimages/Sloth-Climb.png)
- Amount Lost: $93,531.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-3-18

**Quick Summary**

Sloth Climb project rugpulled by EOA address which removed liquidity worth 93,531 $USD

  


 **Details of the Exploit**

Sloth Climb is a BEP20 token trading on PancakeSwap. The token can't be confused with other tokens with the same symbol or name. Its liquidity pool was drained after an EOA address called removeLiquidityETH() function to withdraw all available funds in the amount of 93,531 $USD. The attacker address took LP tokens from LockService contract, which was deployed by the token deployer. The attacker then transferred stolen funds through Stargate Bridge.

  


 **Block Data Reference**

Scammer Address:

https://bscscan.com/address/0xe9b7dec3815bc27a755724b488a441043388aa52

  


Vault contract:

https://bscscan.com/address/0x624bf9c8c4694c36642ac46b3ac36a91de1e2eef

  


Liquidity Drain Transaction:

https://bscscan.com/tx/0xf4d483a276b7ee6cbdc99b59d78596199a69b03941d6c3de0d29107733454c83


Proof Links:
- [https://twitter.com/CertiKAlert/status/1637187079850414080?s=20](https://twitter.com/CertiKAlert/status/1637187079850414080?s=20)


