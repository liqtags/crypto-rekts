# StableMagnet
![StableMagnet](/rektimages/StableMagnet.png)
- Amount Lost: $27,000,000.00
- Funds Returned: $24,000,000.00
- Category: Other
- Date: 2021-6-23

**Quick Summary**

StableMagnet was rugpulled for over 27,000,000 $USD. The scammer used an unverified contract to transfer approved tokens.

  


 **Details of the Exploit**

The exit scam started from this transaction:  
https://bscscan.com/tx/0xf0ba46c8a20e1e75ad382e42c509bf71393e1b3b90326165c747a5d3cc5d967c  
  
As a result, 8M USDT, 7.2M USDC, and 7M BUSD were taken from the StableMagnet 3Pool via an unverified source code.  
  
The unverified SwapUtil library did not only contain code to drain all pairs, it also contained code to transfer more tokens to everyone who had approved StableMagnet.

  


 **Block Data Reference**  
SwapUtils library containing the exploit:  
https://bscscan.com/address/0xE25d05777BB4bD0FD0Ca1297C434e612803eaA9a  
  
The stolen funds were distributed between some external wallets. BUSD sent to Binance hot wallet:  
https://bscscan.com/address/0x2bac04457e5de654cf1600b803e714c2c3fb96d7#tokentxns  
  
Tether received on ETH chain:  
https://etherscan.io/address/0xDF5B180c0734fC448BE30B7FF2c5bFc262bDEF26#tokentxns  
  
Tether changed to DAI:  
https://etherscan.io/address/0xe5daac909a3205f99d370bc2b32b1810a4912a07#tokentxns


Proof Links:
- [https://rekt.news/stablemagnet-rekt/](https://rekt.news/stablemagnet-rekt/)
- [ https://twitter.com/RugDocIO/status/1407830298251964427]( https://twitter.com/RugDocIO/status/1407830298251964427)
- [ https://twitter.com/peckshield/status/1407845381312892931]( https://twitter.com/peckshield/status/1407845381312892931)
- [ https://twitter.com/cryptogle/status/1598025871545495552]( https://twitter.com/cryptogle/status/1598025871545495552)


