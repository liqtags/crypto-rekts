# Snowflake Floki
![Snowflake Floki](/rektimages/Snowflake-Floki.png)
- Amount Lost: $70,375.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-12-28

**Quick Summary**

The Snowflake Floki smart contract contained a transfer tax component that allowed the project deployer to ramp up the transfer fee of each transaction up to 100%, netting the deployer approx. $ 70k in ill-gotten funds.

  


 **  
Details of the Exploit**

The Snowflake Floki project was practically an imitation of the meme coin Floki Inu but promised to develop a metaverse casino. The $SFF token would have played the role of the in-game currency used for bets in Poker, Blackjack and Roulette. In order to make the $SFF token tradable, the contract deployer added initial liquidity in the below transaction:  
https://bscscan.com/tx/0x371a142d01aff8414cda58baf96cc36fcee29b16f34c4990b83f6022ed02fd57

A closer look at the $SFF smart contract should have alerted investors since the transfer taxes were adjustable by the contract deployer. This empowered the contract deployer to set fees up to 100% for each transaction, sending the tokens to his address:  
https://bscscan.com/address/0x78cd0ea1108a146dc493b086170e2d9771b67570#code#L1092  
The deployer took advantage of the changeable transfer fee set it to 95% for selling SFF token:  
https://bscscan.com/tx/0xe8e6680e9ed778c6bc9f01e86986b54fdb8462df43bc628b193cdca46ef678e5

In order to squeeze as much as possible out of the project, the deployer also removed liquidity several times :  
https://bscscan.com/tx/0x18168c04bacaea98fea69d9c8b87fe9ab1dcd2313fb507ab240e4d63b0f73957  
https://bscscan.com/tx/0xd9018a15ab1bd566f030d3b0ca7ece1bc5985156ccebb947d32d6bebba1cee15  
https://bscscan.com/tx/0xd3ddc09b48ee87f402aebb9757b39a4e8d9f4ae5c996372d930439ddba126e04  
https://bscscan.com/tx/0x3cbb6a948ba7f4fc31e9e36541d74fc2b3343a36de0dbef09929108da506144a  
https://bscscan.com/tx/0x555b73292e889211214a164b402f09b884a6dce9316fdba40420cc311446f65b  
  
The website and social media have been taken down.

  


  


 **Block Data Reference**

Contract Deployer Address:

https://bscscan.com/address/0x731e5bb934128bcf787c49f0dfcf7432e6fbf44c


Proof Links:
- [https://twitter.com/PeckShieldAlert/status/1475661511603281921](https://twitter.com/PeckShieldAlert/status/1475661511603281921)


