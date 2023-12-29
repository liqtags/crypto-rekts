# Origin Protocol
![Origin Protocol](/rektimages/Origin-Protocol.png)
- Amount Lost: $8,000,000.00
- Funds Returned: $0.00
- Category: NFT,Stablecoin
- Date: 2020-11-17

**Quick Summary**

Origin Dollar (OUSD) was exploited due to a reentrancy attack, leading to an excess minting of OUSD and a loss of 70,000 ETH.

  


 **Details of the Exploit**

The attacker borrowed 70,000 ETH from dYdX and exchanged a portion of it for USDT and DAI on Uniswap. They then used these stablecoins to mint OUSD from the Origin Protocol's vault. The attacker exploited a reentrancy vulnerability in the mint function of the OUSD contract to mint more OUSD than the equivalent stablecoin collateral in the vault. This resulted in the attacker holding more OUSD than the total value in the vault. The attacker then exchanged the excess OUSD for USDT and DAI on Uniswap and SushiSwap, and withdrew the remaining stablecoins from the OUSD vault. Finally, the attacker returned the borrowed ETH to dYdX and transferred the stolen funds to their account.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0xb77f7bbac3264ae7abc8aedf2ec5f4e7ca079f83

The transaction behind the attack:

https://etherscan.io/tx/0xe1c76241dda7c5fcf1988454c621142495640e708e3f8377982f55f8cf2a8401

The contract deployed at:

https://www.contract-library.com/contracts/Ethereum/0x47c3d84394043a4f42f6422accd27bb7240fdfe2

  
\- 1,000,000 DAI was transferred to the attacker’s account  
https://etherscan.io/tx/0x8c0459b68555129502a88619df3c89428ba89451f2758f388884192cbe84cd95  
  
\- 1,138,449.12 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0xae6bee2824afe1b0552f2127fb3f124b31adac554e04dba8231fffe4ea83f6bb  
  
\- 531,688.76 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0xa990fe2c4ea7afd6497032a57f005a4d2ba2db1acb044ffa955615d6a126538f  
  
\- 248,059.48 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0xe95b4d3df0a73728cd0d0c32dfb2b41625e6946ac466e055d2fd18fa62c14e55  
  
\- 543,305.34 USDT and 226,832.53 USDC were converted to ETH on Uniswap and transferred to the attacker’s account along with 1,128,244.36 DAI  
https://etherscan.io/tx/0x49d59b45031aa90aa6a096e3e2a6171fa7f5b4882ea9ac997fd64911b6f33aec  
  
\- 115,732.21 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0xcff80ddd8576e19e23116aaacdf37147b9eaa69103bc8dc8b0602aee2fc089b4  
  
\- 53,994.89 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0x47e515d55b4c52302c184cb9323a9e110f37d54ba79d6190756fd7c850847343  
  
\- 300,000.00 OUSD was exchanged for 60,505.30 USDT on Uniswap

1,000,000.00 OUSD was exchanged for 187,152.67 USDT on SushiSwap  
https://etherscan.io/tx/0x8a1907dbf0f687524e6e7869000e1ef5b34d937741a3160611d42e15c8d76b15  
  
\- 25,191.33 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0xf14f4158fcbb5ff1e32638bed7ea0d80848a34d4c228a5477113ab58913633d9  
  
\- 300,000.00 OUSD was exchanged for 29,803.08 USDT on Uniswap

1,000,000.00 OUSD was exchanged for 98,401.29 USDT on SushiSwap  
https://etherscan.io/tx/0x8eba96d3f5851f4d4f703c40fb58effaca1211660b2a96aafd50e3587f3a29e7  
  
\- 11,616.27 OUSD was redeemed for a mix of stablecoins  
https://etherscan.io/tx/0x9a133457d88a79d539cda2353e24c45ed55817da244abe77fefbb0e0d6af0383  
  
\- 434,407.95 USDT and 24,443.08 USDC were converted to ETH on Uniswap and transferred to the attacker’s account along with 121,577.54 DAI  
https://etherscan.io/tx/0x7db4e34811371ff2862fb2532d2d401904bd98917878c27828d4826027ffc45e  
  
\- 498,487.66 OUSD was transferred back to the deployer of the OUSD contract (Origin Protocol)  
https://etherscan.io/tx/0x2c9d20292e5a0edccf9e5713819934161520db0b02aee90f719bd64899ba211f


Proof Links:
- [https://blog.originprotocol.com/urgent-ousd-has-hacked-and-there-has-been-a-loss-of-funds-7b8c4a7d534c](https://blog.originprotocol.com/urgent-ousd-has-hacked-and-there-has-been-a-loss-of-funds-7b8c4a7d534c)
- [ https://rekt.news/hack-epidemic/]( https://rekt.news/hack-epidemic/)


