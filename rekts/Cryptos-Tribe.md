# Cryptos Tribe
![Cryptos Tribe](/rektimages/Cryptos-Tribe.png)
- Amount Lost: $91,023.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-7-27

**Quick Summary**  
The $CSTC token has been rugpulled by it's team. Scammers took a profit of $91k.  
 **  
Details of the Exploit**

The creator of the token deployed the contract to the BSC network, where 1B tokens were minted to him:

https://bscscan.com/tx/0xec710cbf64daa40432701a092da485be09620e5174aec20d8647cbaeb4eb3ba0

After that, the token creator started sending tokens to other addresses: 

https://bscscan.com/token/0x78f1a611cceba2ff17ea53570dbee7d43629e8bc?a=0xce213442ad304c077099de1a37f6cc089fd6c105

Scammer address (C) interacted with the _finalize  _function, which created a pool of liquidity between the CSTC/BNB pair: https://bscscan.com/tx/0x85065f9b72ee6f8d4f30d00ffef8cb2f49b3ccacc38e747fa32ae7cf474ca479

After a while, when investors invested in the token, scammer address (B) started dumping the price of the token in this transaction:

https://bscscan.com/tx/0xe439ffd5707488e00244b23e9db32a38087fb6ec7708cb6e981bfacb7da9511c

$CSTC tokens were received by scammer address (B) in this transaction: https://bscscan.com/tx/0x6c8cdeaf81eacfe52babfd20ab9e1c1d330f2fda6738ed75e1d1fda9e801bce7

Funds were laundered via Tornado.cash.

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Involved addresses:

Token creator, scammer address (A): https://bscscan.com/address/0xce213442ad304c077099de1a37f6cc089fd6c105

Scammer address (B): https://bscscan.com/address/0x17fb844d1bd8142e2fc05b3cc440f01e0a132898

Scammer address (C) - LP creator: https://bscscan.com/address/0x664b67afcce3c19f23fb197efc5125a35b831bba

  


Liquidity pool creation transaction: https://bscscan.com/tx/0x85065f9b72ee6f8d4f30d00ffef8cb2f49b3ccacc38e747fa32ae7cf474ca479

  


Contracts interacted with:

Bonus Pools: 

1) https://bscscan.com/address/0xa49e4193df2d74965f7b2e7882d46928d773db37

2) https://bscscan.com/address/0x82e9be2e5a1a7f411dc332ab11b8726472ad3df3

3) https://bscscan.com/address/0x4459a559b9da3f77adfdbf1aee649693d7f13327



