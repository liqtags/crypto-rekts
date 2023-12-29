# WOLF Protocol
![WOLF Protocol](/rektimages/WOLF-Protocol.png)
- Amount Lost: $30,022.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-1-23

**Quick Summary**

The deployer of the WOLF Protocol exploited users by trapping liquidity providers through locking funds and minting $WFLP token to an EOA that was not blacklisted. This exploit netted the deployer approx. $30k in ill-gotten funds.

  


 **Details of the Exploit**

The Wolf protocol promised to be a DeFi revolution offering staking and yield solutions on three different blockchains. The website boasted a fake team and a fake roadmap. The smart contract contained malicious rights that could only be invoked by the token deployer and enabled a centralized token balance modification. In simple terms, the token deployer could change the balance of any holder.

The contract deployer added initial liquidity at:  
https://etherscan.io/tx/0x28d4d2d427c2c18295bcdc92f95af81f1e5ba9de78072d0d08cf647625800bb1

This made the token tradable. Within 11 days, the community noticed that the $WLFP could not be sold or withdrawn. The root of this can be found in this transaction, where the contract deployer locked liquidity:  
https://etherscan.io/tx/0x4b4c05789728e2f0a1652e992c81af6b2b1a03685731b1b9f5cea41845872912  
After users were trapped the contract deployer proceeded to invoke the _approveAndCall_ () function, which included an external wallet and _addedValue  _amount as the input data:  
https://etherscan.io/tx/0xa0dcdb89aefaf04ab17bf00ba028d5dc0ef763c61143eea137cd69eaff964401  
After the external wallet received the enhancement in its token balance, the external wallet dumped $WLFP for $ETH34t:  
https://etherscan.io/tx/0x54e39afc20e9884205e77a9bf81296f41ec3ad21815e449693834045f6b88593

  


 **Block Data Reference**

Project deployer

https://etherscan.io/address/0x871f91e2d25edcec66a5c03fe82178d55c1bbd34

  



Proof Links:
- [https://twitter.com/CaptainJackAPE/status/1352985427259473920](https://twitter.com/CaptainJackAPE/status/1352985427259473920)


