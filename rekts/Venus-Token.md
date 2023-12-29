# Venus Token
![Venus Token](/rektimages/Venus-Token.png)
- Amount Lost: $16,937.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-5-11

**Quick Summary**

Venus Token vault was exploited, resulting in a loss of 16,937 $USD.

  


 **Details of the Exploit**

Venus Token is a BEP20 token trading on PancakeSwap. The vault contract VenusDevide was exploited. Worth mentioning that the affected contract has no relationship with the original token, and the token has over 600,000 $USD in liquidity after the exploit. An EOA address could call an unprotected function on an unverified contract named VenusDevide which held more than 8 million $VUS tokens. The attacker deployed multiple malicious contracts and withdrew $VUS tokens from the vulnerable contract. They then swapped them for 54.7 $BNB (worth 16,937 $USD at the time) before self-destructing their malicious contracts. All stolen funds remain in possession of the attacker's original address.

  


 **Block Data Reference**

Attacker Address:

https://bscscan.com/address/0x4C1F90281421CA00207F7890342EAA808C322E5A

  


Malicious Transaction:

https://bscscan.com/tx/0x90ee7abd5d6ec0f0f3eb61e1e8a559393aa879b90ad2da4fa2739ab6233c249f

  


Swap Transaction:

https://bscscan.com/tx/0x457a20d140b63485c1edd53b76842be3521b723f5f8256a5b8d8227bfd606eb1

  


Main Malicious Contract:

https://bscscan.com/address/0x78C6FA5F00B8968F5279EE3ECB5F95B3AD232759



