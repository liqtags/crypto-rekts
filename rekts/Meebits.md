# Meebits
![Meebits](/rektimages/Meebits.png)
- Amount Lost: $700,000.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2021-5-8

The exploiter's address:  
https://etherscan.io/address/0x009988ff77eeaa00051238ee32c48f10a174933e  
  
The exploiter's smart contract:  
https://etherscan.io/address/0x270ff2308a29099744230de56e7b41c8ced46ffb  
  
Affected NFT smart contract:  
https://etherscan.io/address/0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7#code  
  
Minting function in NFT uses pseudo randomization depends on block values:  
uint index = uint(keccak256(abi.encodePacked(nonce, msg.sender, block.difficulty, block.timestamp))) % totalSize.  
  
It means close to zero randomnesses of the returned index. The exploiter has used a bot and deployed a contract to interact with the NFT contract. The exploiter used open information which exactly what metadata he should receive to sell NFT with the highest profit. If the bot minted an undervalued NFT, the bot reverted the transaction. This vulnerability allowed exploiter minting predictable expensive NFTs.


Proof Links:
- [https://forum.openzeppelin.com/t/understanding-the-meebits-exploit/8281](https://forum.openzeppelin.com/t/understanding-the-meebits-exploit/8281)
- [ https://cointelegraph.com/news/85-million-meebits-nft-project-exploited-attacker-nabs-700-000-collectible]( https://cointelegraph.com/news/85-million-meebits-nft-project-exploited-attacker-nabs-700-000-collectible)


