# Zapper
![Zapper](/rektimages/Zapper.png)
- Amount Lost: $2,500,000.00
- Funds Returned: $2,500,000.00
- Category: Other
- Date: 2021-6-14

The team of whitehat hackers (AndreiKei and VV) identified a loophole in the old Polygon bridge smart contract, which could lead to the possible exploit and lost of the users funds.  
  
The vulnerability allows possible attacker to transfer tokens from users’ accounts, for which they had previously granted unlimited approval, via the Zap. This was possible due to a function, which executes external swaps and Zaps (via 0x, Paraswap, etc), accepting non-validated _calldata_ :  
(bool success, ) = swapTarget.call.value(valueToSend)(swapCallData)  
  
The Zap lacked an appropriate pause function which meant that the Zapper team was unable to prevent the vulnerability from being exploited.  
  
Zapper team together with the team of whitehat hackers (AndreiKei and VV) executed whitehat hack to withdraw funds from the old contract to the safe distribution contract, where users could successfully reclaim their funds.  
  
Deprecated Polygon bridge:  
https://etherscan.io/address/0x1f0d1927498fbd4f9e8558704ce5b658929527ec  
  
Smart contract used for the exploit:  
https://etherscan.io/address/0x7284e5cd49f47da42d355bcb5ab64fbb45d7eff6  
  
Received funds were transferred to the safe smart contract for further distribution to the affected users:  
https://etherscan.io/address/0x63cd1f35063e1bdd01355fb2bee4ecee05d94b84


Proof Links:
- [https://twitter.com/zapper_fi/status/1404429179794362369?s=21](https://twitter.com/zapper_fi/status/1404429179794362369?s=21)
- [ https://medium.com/zapper-protocol/post-mortem-polygon-bridge-vulnerability-cb8029275622]( https://medium.com/zapper-protocol/post-mortem-polygon-bridge-vulnerability-cb8029275622)


