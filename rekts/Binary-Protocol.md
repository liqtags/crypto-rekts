# Binary Protocol
![Binary Protocol](/rektimages/Binary-Protocol.png)
- Amount Lost: $3,924.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-1-29

The contract deployer used a hidden minting functionality under the function _initialSupply_ (), which was invoked by the contract deployer 3 times:  
https://etherscan.io/tx/0x7467abb573c49a7f9afa29a0d086db87b05470132e5a3e4f1c32cee80293a521  
https://etherscan.io/tx/0xf4b6c14069f1d9761c40c11f4132be2cc0361d86b2b069c551e51deadbc2293c  
https://etherscan.io/tx/0x672689de6495180d7301f9282dac828d6aad609d9a1fb7bb7f36b7a6623dc887  
  
In the function input data, the recipient address of the minted tokens was this address:  
0xD97A750139bC69A8e206b67B54288463C634050C  
  
This external wallet added initial liquidity at:  
https://etherscan.io/tx/0x1cdad510f30826e2d54b15a61942d9a33fdb0271a6d1b11c935a1f99ea825da5  
  
The transaction, where the external wallet sold tokens:  
https://etherscan.io/tx/0x0c02a010cf511dc7ef859e8f64daaa38ce4f1d0021523bfc5cc29a9feb41b083


Proof Links:
- [https://twitter.com/CaptainJackAPE/status/1355054630770626560](https://twitter.com/CaptainJackAPE/status/1355054630770626560)


