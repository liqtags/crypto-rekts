# DeFiPie
![DeFiPie](/rektimages/DeFiPie.png)
- Amount Lost: $269,315.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-7-13

The hacker's address on Ethereum:  
https://etherscan.io/address/0xf6f43f77ef9e561dcb2997d8e7ec1d685b6c0fe1  
  
BSC:  
https://bscscan.com/address/0xf6f43f77ef9e561dcb2997d8e7ec1d685b6c0fe1  
  
Polygon:  
https://polygonscan.com/address/0xce1f4b4f17224ec6df16eeb1e3e5321c54ff6ede  
  
The transaction behind the attack on the BSC:  
https://bscscan.com/tx/0x45f6f792638d114f31f6608dca4c79b1216bd5c7c45218a5fd8f1c2e309c6d75  
  
The hacker:  
\- created a token contract (X token) with a modified transfer function:  
https://etherscan.io/token/0xf8dFD22A3724DE8DF4D03254e4141aDD24966e4B#readContract  
https://etherscan.io/token/0xb5337f26745f59dbdEa1185e25169796256362Ef  
  
\- created pools for X tokens and deposited liquidity  
  
\- provided collateral (USDT, DAI, USDC, etc)  
  
\- borrowed X tokens and real tokens (PIE and others) and with a modified transfer function in X token, could able to borrow more than he provided as collateral  
  
\- after that from his second account he liquidated loans of X tokens in the first account thereby returning the collateral  
  
\- repeated with each pool.  
  
Stolen funds were deposited into Tornado Cash and Typhoon mixers.


Proof Links:
- [https://medium.com/defipie/removing-the-mask-from-the-july-attacker-part-1-5e516de5b84d](https://medium.com/defipie/removing-the-mask-from-the-july-attacker-part-1-5e516de5b84d)


