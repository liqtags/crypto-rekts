# DefiLabs
![DefiLabs](/rektimages/DefiLabs-Rugpull.png)
- Amount Lost: $1,634,351.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-7-27

**Quick Summary**

DefiLabs Farm was rugpulled via a deployer-related address, draining multiple assets worth 1,634,351 $USD.

  


 **Details of the Exploit**

DefiLabs Farm, a staking platform on the Binance Smart Chain, experienced an exitscam. The deployer of the vPoolv6 contract set a new privileged address 'funder'. This address then withdrew funds from the contract using the 'withdrawFunds' function and transferred them to another EOA. The exploited assets included USDT, BTC, ETH, and CAKE tokens, with a total loss estimated at 1,634,351 $USD.

  


 **Block Data Reference**

Deployer Address:

https://bscscan.com/address/0xfd2f26dc8789c598e86e7641a74cc60a77b34115

  


Scammer's Address:

https://bscscan.com/address/0xee08d6c3a983eb22d7137022f0e9f5e7d4cf0be2

  


Funds Holder Address:

https://bscscan.com/address/0xfd2f26dc8789c598e86e7641a74cc60a77b34115

  


Setting Privileged Address Transaction:

https://bscscan.com/tx/0x0f029cc8daf082613648a26274f09e47b9124b052d9f903c5eb7996af29b57c4

  


Draining Transaction:

https://bscscan.com/tx/0xcd255e0d507d59ac4a357b64a8e0649fc16995f7950fd0421f2010e27cc01e99


Proof Links:
- [https://twitter.com/HashDit/status/1684579783261458434](https://twitter.com/HashDit/status/1684579783261458434)


