# TreasureDAO
![TreasureDAO](/rektimages/TreasureDAO.png)
- Amount Lost: $0.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2022-3-3

The exploiter's address:  
https://arbiscan.io/address/0x9b1acd4336ebf7656f49224d14a892566fd48e68  
  
The example of the transaction:  
https://arbiscan.io/tx/0x37222d3ad371dff2d3f3ae1c788d1cc4ad69e9f1839776830726485119a89269  
  
The protocol was exploited in several transactions, leading to more than 100 NFTs being stolen from different collections of Treasure Marketplace.  
  
The exploiter:  
\- called _buyItem_ () with valid NFT token and NFT ID, but with the invalid 0 quantity  
\- Treasure Marketplace sells the NFT but charges 0 MAGIC (due to 0 quantity)  
  
The hack is made possible due to a bug in distinguishing ERC721 and ERC1155 in _buyItem(_ ), which miscalculates the price of ERC721 as ERC1155 with the given 0 quantity.


Proof Links:
- [https://twitter.com/Treasure_DAO/status/1499864896166584336](https://twitter.com/Treasure_DAO/status/1499864896166584336)
- [ https://twitter.com/peckshield/status/1499250224455245825]( https://twitter.com/peckshield/status/1499250224455245825)


