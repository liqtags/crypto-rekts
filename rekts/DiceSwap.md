# DiceSwap
![DiceSwap](/rektimages/DiceSwap.png)
- Amount Lost: $29,780.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-3-10

The Master Chef contract contains hidden functionality under the set() function, which was invoked multiple times by the contract deployer at:  
https://explorer.bitquery.io/bsc/txs/calls?internal=false&contract=0x08eee9c8d38804dcba77e66aab0deb5064c21370&method=d9638422  
  
Calling set() function led to the LP tokens and native tokens transfer onto the external wallet, example transaction:  
https://bscscan.com/tx/0x6a16dd9fcc7c6ec3d563096269f9f70eac5edd7d4b1a5ec1509fac62de3ecbf6  
  
The liquidity was removed by the external wallet multiple times at:  
https://bscscan.com/tx/0xb523ea3c3e72b15ce8208a7b2c86fce054be0d86d73c5e562c7e3637183065a4  
https://bscscan.com/tx/0x3f6d3d3e11c5a27e3dde01069de1091ada93f093dacaeaf8070899ec685cf0eb  
https://bscscan.com/tx/0x751d3f478393b7f208b67f66c2e085b0815f7ebf84237943980ef3113a3d5a12  
https://bscscan.com/tx/0x3197c878356b33f1175f770259afbcd2b7bb4909732ed60a68c856714a808af3  
https://bscscan.com/tx/0x83d93a52fe12c627a4cfaed2bdab196f7a4f8f8a72b1a2b2585afb32c60c03a1  
https://bscscan.com/tx/0x89b3c2fc6947f9cf5ea8832546772471e37121580102145e062d10afbe4fec5f  
https://bscscan.com/tx/0x7880e9c318eee8bc900c30b11c94aeebca98d90927871265fd23381cf5603ff3  
https://bscscan.com/tx/0xf25a25c7373755383437af5e03acbfc5698e746e1ebbb0b18fcc95de70d1a285  
https://bscscan.com/tx/0x6a2ac8d46640e2f042c6a0a618991f43df651a0c3d67455f15711388d3f09385



