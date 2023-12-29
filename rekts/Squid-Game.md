# Squid Game
![Squid Game](/rektimages/Squid-Game.png)
- Amount Lost: $5,723,268.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2021-11-1

**Quick Summary  
**

The Squid game project has been rug pulled by its team by way of blacklisting users from selling the $SQUID token. Investors were collectively alleviated of approx. $ 5,7 million.

  


 **Details of the Exploit  **

The Squid game project was inspired by the hit Netflix show and promised to be a play to earn game, hereby resembling the actions in the series. The hype surrounding the Netflix show combined with the increased interest in crypto due to the bull market incentivized big news outlets such as BBC and CNBC to write about the rapid surge in price of the new $SQUID token. Retailers around the world pushed the price from $0,01 to $2,861 in little over a week. CoinMarketCap published a warning concerning this project from the start as early investors reported that the sell of the token on pancake swap was not possible. A look at the smart contract revealed that all 3 contracts: SQUID, Marbles, and MasterChef were upgradable. Meaning the contract deployer would change the mechanisms of the project at will.  
For example a new MasterChef made it possible for the 0x71 EOA to withdraw all tokens from the MasterChef contract at the following transaction:  
https://bscscan.com/tx/0xf7c9d0e5a81999f9e06fe78df7ce41da112d8bd4f2da7b16cfdbbe46c92cb6af

The Squid game project boasted two token. The $Marbels token was required in order to be eligible to sell $SQUID on the open market. $Marbles were not tradable on the market and could only be obtained by participating in the game with an entrance fee of $SQUID 456. Meaning at the all time high price of the SQUID token a withdrawal would have costed at least $1,3 million.

The contract deployer also blacklisted all users that did not hold Marble's token to prevent from selling SQUID in this transaction:  
https://bscscan.com/tx/0x5b82e96fccaa9ccc3255b509df51d127aa7ad402624f07683855d0e1c4555041

  


  


  


 **Block Data Reference**

Involved EOA addresses:  
https://bscscan.com/address/0x71d934aa2119ca3995f702f075d540f7a6b0f728  
https://bscscan.com/address/0x34400280a169f4685193926a513618cf7fe7f0aa  
https://bscscan.com/address/0x1f5eabba9c56bca4a7828969b79bc87051125b31  
https://bscscan.com/address/0x3228eea3d2b7118f09f13a936f26c54e8f9bfb65

  


  


0x32 invoked the internal protocol's contract which worked as the interface of the PancakeSwap pair contract to sell SQUID tokens at multiple transactions under the "0x5c2a8729" method:  
https://bscscan.com/address/0x3228eea3d2b7118f09f13a936f26c54e8f9bfb65  
  
Example of "0x5c2a8729" transaction:  
https://bscscan.com/tx/0x98a07fde52914566a72b7eeb2ec1b1af3cb9a0a1d817bb1fb8d6d204993ae96a  
  
The WBNB recipient was EOA, marked as SQUID Token Rug 2, which then deposited stolen funds into Tornado Cash Proxy:  
https://bscscan.com/address/0x34400280a169f4685193926a513618cf7fe7f0aa  
  
2 unverified smart contracts were used to sell SQUID tokens:  
https://bscscan.com/address/0x95eb532f23a97191324103755332a3dff97d722f  
https://bscscan.com/address/0x5b871670d4f1d81591ecf641588a28f5032c9dcd


Proof Links:
- [https://cryptopotato.com/squid-game-pulls-the-rug-squid-price-crashes-99-99/](https://cryptopotato.com/squid-game-pulls-the-rug-squid-price-crashes-99-99/)
- [ https://www.cmnnews.live/squid-game-rugpull-from-2856-to-0-0008-in-10-minutes/]( https://www.cmnnews.live/squid-game-rugpull-from-2856-to-0-0008-in-10-minutes/)
- [ https://twitter.com/TrustWallet/status/1455148681351483393]( https://twitter.com/TrustWallet/status/1455148681351483393)
- [ https://twitter.com/CoinMarketCap/status/1455183210149818371]( https://twitter.com/CoinMarketCap/status/1455183210149818371)


