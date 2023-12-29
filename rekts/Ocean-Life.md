# Ocean Life
![Ocean Life](/rektimages/Ocean-Life.png)
- Amount Lost: $11,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-4-19

**Quick Summary**

On April 19, 2023, an attacker hacked the Ocean Life token on Binance Smart Chain (BSC), using a flawed mechanism to lower the token supply and manipulate the price. The attacker earned 32 WBNB in return for their actions.

  


 **Details of the Exploit**

The attacker used a flash loan of 969 WBNB from DPPOracle and converted it to OLIFE tokens using PancakeSwap. By internally calling the '_reflectFee' function through the transfer function, the attacker decreased the total value of _tTotal. However, the balance of the pool was much higher after accumulation, as computed using balanceOf(), and the hacker used a direct call to swap to withdraw $WBNB from the pool. The attacker then returned the 969 WBNB flashloan and transferred the 32 WBNB profit to another address.

  


 **Block Data Reference**

Attacker's transaction: 

https://bscscan.com/tx/0xa21692ffb561767a74a4cbd1b78ad48151d710efab723b1efa5f1e0147caab0a

Attacker address: 

https://bscscan.com/address/0xfb8ef8de849079559801bff8848178640cdd41b7

Stolen funds address: 

https://bscscan.com/address/0x662D2dC484D65a3Ba4Da80E36EAa9a400AF0726B


Proof Links:
- [https://www.binance.com/en/feed/post/437385](https://www.binance.com/en/feed/post/437385)
- [ https://blog.solidityscan.com/ocean-life-token-hack-analysis-flash-loan-attack-ded51d0ee574]( https://blog.solidityscan.com/ocean-life-token-hack-analysis-flash-loan-attack-ded51d0ee574)
- [ https://twitter.com/CertiKAlert/status/1648512961521283077]( https://twitter.com/CertiKAlert/status/1648512961521283077)


