# CoinSWOP
![CoinSWOP](/rektimages/CoinSWOP.png)
- Amount Lost: $21,049.00
- Funds Returned: $0.00
- Category: CeFi
- Date: 2020-12-4

The contract owner invoked _setMigrator_ () function at:  
https://etherscan.io/tx/0xf73a10ee956a010b5b1f3174f60ca02a5dce171808ad76f1ae9bc131259007f1  
  
CoinSWOPMaster smart contract was set as migrator. The smart contract owner called _migrate_ () functions 11 times to withdraw the user's LP tokens with the help of infinite approval. LP tokens were migrated to an unverified smart contract that received real LP tokens and returned fake ones. Then real LP tokens went to the contract deployer as the final recipient. Migrate transaction example:  
https://etherscan.io/tx/0x5b19f1e334697646c855a17d909f141f2a64ded4f2db4944a0aa8fcae848c592  
  
The final recipient is getting LP tokens:  
https://etherscan.io/tx/0xe6543f5b2725354ead24844f941e53cc8324903caf418450b4cb6765e03c5aea  
  
LP tokens were exchanged for ETH and deposited to the Tornado Cash mixer at these transactions:  
https://etherscan.io/tx/0xd6584b95f0192ab01717a092dc80fbe1afaef38bc46b9bc96626736a15f8578c  
https://etherscan.io/tx/0x90bd78b453ed65f02f5299211808947d864e9669c0ea9d00828ed5c83005b47c  
https://etherscan.io/tx/0x5d530f23b669fb363fd8035b76d723373282c0accb2cc560447636183208667d  
  
6.8 ETH were transferred to some external wallet:  
https://etherscan.io/tx/0xf875951759eb516db585b08191d5eb6b973b5892d86bd6a85e1c1063e3b48867


Proof Links:
- [https://twitter.com/CaptainJackAPE/status/1333759436792315905](https://twitter.com/CaptainJackAPE/status/1333759436792315905)


