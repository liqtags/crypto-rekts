# Casper DeFi
![Casper DeFi](/rektimages/Casper-DeFi.png)
- Amount Lost: $172,411.00
- Funds Returned: $190,383.00
- Category: Yield Aggregator
- Date: 2021-8-4

In the official post mortem, the project team says that their Solidity developer left the minting possibility in the contract constructor.  
  
Their Solidity developer is the contract deployer as well:  
https://ftmscan.com/address/0xe6a025845e9ab116a135dbaec6de0f521219782b  
  
The contract deployer invoked the _mint_ () function in the following transactions:  
https://ftmscan.com/tx/0xf296baf2e970316949e6910b54decbea52aaabc94447cb52fcbca6049205f29d  
https://ftmscan.com/tx/0x4d02eac3127a00c673f0ce314d5565931e125c98605c2d74ced29543008d4a36  
https://ftmscan.com/tx/0x86360b2e69fd75f62424a17f6241112b0bd831679fe48aaab37f5acf5c7ea35d  
  
The minted tokens were sold by the contract deployer multiple times:  
https://ftmscan.com/txs?a=0xe6a025845e9ab116a135dbaec6de0f521219782b&p=1  
  
Received WFTM tokens were exchanged on BNB tokens and bridged to the BSC:  
https://ftmscan.com/tx/0xf1d92544deb38a4508d85b2810da37aad8d03dae56e051142b80b0c0fc5586f8  
https://ftmscan.com/tx/0xb099c04d0d5ef612e950ab019c9ab5888656f3d7823ff4fe6b9be34eafb6fd80  
  
The token recipient on the Binance Smart Chain:  
https://www.bscscan.com/address/0xe6a025845e9ab116a135dbaec6de0f521219782b  
  
The stolen 516.91 BNB tokens were exchanged on BTCB at:  
https://www.bscscan.com/tx/0xf4bc083c0436311870ca57996bb4de209b7df537a739ce9312d793945141c41b  
  
BTCB tokens were bridged through Ren:  
https://www.bscscan.com/tx/0x2c22bd5fdc0faaf2d025a9bb77ce185c1a8e4b893f53fcd20ec53220f06111c2  
  
According to the announcement below, stolen funds were returned:  
https://casperdefi.medium.com/casper-defi-post-mortem-after-casper-token-hack-part-2-1bae9a65ae5c


Proof Links:
- [https://casperdefi.medium.com/casper-defi-post-mortem-after-casper-token-hack-fe668f6722b9](https://casperdefi.medium.com/casper-defi-post-mortem-after-casper-token-hack-fe668f6722b9)
- [ https://casperdefi.medium.com/casper-defi-post-mortem-after-casper-token-hack-part-2-1bae9a65ae5c]( https://casperdefi.medium.com/casper-defi-post-mortem-after-casper-token-hack-part-2-1bae9a65ae5c)


