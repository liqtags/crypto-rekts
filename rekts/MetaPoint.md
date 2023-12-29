# MetaPoint
![MetaPoint](/rektimages/MetaPoint.png)
- Amount Lost: $803,242.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2023-4-11

**Quick Summary**

MetaPoint was exploited due to a vulnerability in the deposit function, resulting in the loss of $700K worth of USDT/POT pool tokens.

  


 **Details of the Exploit**

MetaPoint is a metaverse running on the Binance Smart Chain. The project was hacked through a vulnerability found within their deposit function. When a user used the deposit function, it created a new contract and deposited tokens into that contract. The issue arose because this newly created contract had an "approve" function that gave unrestricted access to $META tokens without any restrictions or limitations. An attacker took advantage of this by deploying a malicious smart contract with unverified source code, and draining mass amounts of funds from users who had deposited $POT tokens onto their platform. The exploiter was able to steal 2,518 $BNB which is worth 803,242 $USD at current market rates. All the stolen money transferred through TornadoCash.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0x0d1969a30bb4ba02e731862edbced5f5abba8373

  


Malicious Contract:

https://bscscan.com/address/0xc6e451c8fa3418b703121ac23e44803d143c5d5c

  


Malicious Transaction Example:

https://bscscan.com/tx/0x0ed5cc9abb0f97b27a673cc6f89d6f2e30bde01834887a21092f38c0dc59c4c4


Proof Links:
- [https://twitter.com/YannickCrypto/status/1645925807724929024](https://twitter.com/YannickCrypto/status/1645925807724929024)
- [ https://twitter.com/AnciliaInc/status/1645894518494076928?s=20]( https://twitter.com/AnciliaInc/status/1645894518494076928?s=20)


