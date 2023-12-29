# LV Finance
![LV Finance](/rektimages/LV-Finance.png)
- Amount Lost: $333,987.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2020-9-19

The core staking smart contracts were backdoored with the _addReward_ () function. The following contracts accepted deposits from users in different tokens:  
https://etherscan.io/address/0x80c09d3cc108fa52b7b63cdcc071daebc059a494#code  
https://etherscan.io/address/0x9e1d0964d519ccb470151dd85e78fc798c75deb7#code  
https://etherscan.io/address/0x7b63771fdc7ae30bad88b84cf902161ef3c39f80#code  
https://etherscan.io/address/0xa2a430ce64c1f15f6d3c4a6cce04613986d6f27d#code  
https://etherscan.io/address/0xb7b3ab6363507e5f36e744607696d60b2cdd2f3e#code  
https://etherscan.io/address/0x828995b479999abb8e9e3f82381f34b2c05f7a27#code  
https://etherscan.io/address/0x5a529c3a12006d5a5ecbb5044b66bed0a872bc6c#code  
https://etherscan.io/address/0xd76e44702168e5d3270344e0d14ca10bb902f7f1#code  
https://etherscan.io/address/0xbca5fc48d3d0310204965f6d22764add6989ca06#code  
https://etherscan.io/address/0xc3dc2d24fe3e9127d86ed822e86ddc42b87b903f#code  
https://etherscan.io/address/0xe52dfd3d4bfe8aa76a0cd4ae2f8ad443fa2a3e14#code  
https://etherscan.io/address/0x478e26cbd368aeb8b0b23a43255ccc2d41d28c02#code  
  
In the example below, the external address refers to each smart contract by invoking _addReward_ () function and withdrawing user's deposits:  
https://etherscan.io/tx/0xa5b92bb943f4ddae839145abf11b059b79d3353f4254b989325e415295f03325  
  
In total, 201.5K USDC, 79.6K USDT, 8.1 LEND, 2.7K SUSHI, 816 UNI, 1K LINK, 1.3 SNX, 261 YFV, 0.02 YFI, 82.1 PYLON and 0.76 YFII were stolen and exchanged on ETH.



