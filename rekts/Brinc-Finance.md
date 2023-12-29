# Brinc Finance
![Brinc Finance](/rektimages/Brinc-Finance.png)
- Amount Lost: $1,103,568.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-14

The address marked as "hacker" on Etherscan:  
https://etherscan.io/address/0x6B0b61323F6d77ef8A1a35D11FA877631d8f67Bb  
  
1\. The contract deployer of the staking contract invoked _transferOwnership_ () at:  
https://etherscan.io/tx/0x09ae252d00122864070461e78810a3b91c4fb64076f72eb6dba775a80ca00df4  
  
2\. The _newOwner_ was set to "hacker's" address:  
https://etherscan.io/address/0x6B0b61323F6d77ef8A1a35D11FA877631d8f67Bb  
  
3\. The contract deployer of the staking contract upgraded implementation of the contract at:  
https://etherscan.io/tx/0xdc7b986561a0bec76f1565881a2983b2afd34091130c6658275e1b6276efcfa7  
  
4\. The new implementation is:  
https://etherscan.io/address/0x1eC83036A1dbbd6e001bb216e31b8A259ebd8f3D#code  
  
5\. The new implementation includes _rescueTokens_ () function which allows the owner to withdraw all tokens balance from the contract:  
https://etherscan.io/address/0x1eC83036A1dbbd6e001bb216e31b8A259ebd8f3D#code#F1#L817  
  
6\. The "hacker" invokes _rescueTokens_ () at:  
https://etherscan.io/tx/0x729c2888077942764f9c3ea7aae6b22d8d92b37dec0e96f63589a97e2926da27  
https://etherscan.io/tx/0x03bae1ef2096d490e277cc2aa46022b1985db70b59fd8801b3a9bdfbf9c510db  
  
7\. The "hacker" burns BRC and receives DAI in exchange:  
https://etherscan.io/tx/0x160471a45ddf9130b7e1b0d3f87c3612084bfad6ac3df31079eab7fbfdda15bc  
  
8\. The "hacker" swaps gBRC for DAI on SushiSwap at:  
https://etherscan.io/tx/0xfc559fad3bb06e926c2b9736b61b8a61bfdad4f1d5f6db06b33e9ef767e551f7  
  
9\. Stolen DAI were exchanged on ETH at:  
https://etherscan.io/tx/0xc16be592c609728548e74ea7b1d82bf898d7c11eb58b30ada08e11e9615fc9c9  
  
10\. Received ETH were deposited into Tornado Cash mixer at multiple transactions:  
https://bloxy.info/txs/calls_from/0x6b0b61323f6d77ef8a1a35d11fa877631d8f67bb?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967  
  
The hacker was funded by the contract deployer before the incident:  
https://etherscan.io/tx/0xc95e14ea17062bc04bd824fff995a110e07f67ea25c14b2c298768c6bb0c4944


Proof Links:
- [https://twitter.com/BrincFi/status/1470592846009073664](https://twitter.com/BrincFi/status/1470592846009073664)


