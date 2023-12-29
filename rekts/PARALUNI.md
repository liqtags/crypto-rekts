# PARALUNI
![PARALUNI](/rektimages/PARALUNI.png)
- Amount Lost: $1,661,107.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-3-13

The exploiter:  
https://bscscan.com/address/0x94bc1d555e63eea23fe7fdbf937ef3f9ac5fcf8f  
  
The example transaction behind the exploit:  
https://bscscan.com/tx/0x70f367b9420ac2654a5223cc311c7f9c361736a39fd4e7dff9ed1b85bab7ad54  
  
The hack is made possible due to a reentrancy bug (introduced by the use of a crafted token contract) in the _depositByAddLiquidity_ () function, which somehow doubles the credits the hacker is able to claim. The result gains were swapped via PancakeSwap.  
  
Stolen funds were bridged via cBridge and deposited into Tornado Cash mixer:  
https://etherscan.io/address/0x94bc1d555e63eea23fe7fdbf937ef3f9ac5fcf8f


Proof Links:
- [https://twitter.com/peckshield/status/1502817503877074947](https://twitter.com/peckshield/status/1502817503877074947)


