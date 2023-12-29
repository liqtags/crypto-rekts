# BadgerDAO
![BadgerDAO](/rektimages/BadgerDAO.png)
- Amount Lost: $120,285,547.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-2

**Quick Summary**

BadgerDAO lost 120,000,000 $USD worth of assets due to dApp exploit

  


 **Details of the Exploit**

BadgerDAO is a Yield Aggregation protocol. The attacker exploited the front end of the BadgerDAO dApp. Many impacted users alleged that while receiving yield farming rewards and engaging with Badger vaults, their wallet providers prompted them with spurious requests for extra permissions.  
  
One of the most affected users (896 Badger WBTC):  
https://etherscan.io/address/0x53461e4fddcc1385f1256ae24ce3505be664f249  
  
The following transaction shows that this user invokes additional approval for spending tokens for the attacker's address inside _increaseAllowance_ () function:  
https://etherscan.io/tx/0x5e4c7966b0eaddaf63f1c89fc1c4c84812905ea79c6bee9d2ada2d2e5afe1f34  
  
After that, the attacker can withdraw users' funds using _transferFrom_ () function, for example:  
https://etherscan.io/tx/0xe4e152f5327cb1341970f73c6e91cc9a1de3eb90e8bb84361fc306f912828126  
  
Stolen funds are calculated up to $120m at the moment.  
  
Approximately 500+ users were affected, based on the Bloxy data:  
https://bloxy.info/txs/references_address/0x1fcdb04d0c5364fbd92c73ca8af9baa72c269107?argument=spender&signature_id=5

  


 **Block Data Reference**

The attacker's address:  
https://etherscan.io/address/0x1FCdb04d0C5364FBd92C73cA8AF9BAA72c269107


Proof Links:
- [https://archive.is/TIObp](https://archive.is/TIObp)


