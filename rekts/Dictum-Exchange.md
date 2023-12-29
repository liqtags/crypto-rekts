# Dictum Exchange
![Dictum Exchange](/rektimages/Dictum-Exchange.png)
- Amount Lost: $2,100,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-31

**Quick Summary**

Dictum Exchange has rugged pulled. On the 31st of Dec 2022, just after airdropping its $DIC token, the project shut down all of its social networks and performed hard rug from unverified proxy liquidity pool contracts.

  


 **Details of the Exploit**

The protocol built on the Arbitrum network Dictum Exchange performed hard rug from its LPs. 

Most of the contracts of the protocol are built using a proxy upgradeability pattern. In this case, it allows deploying new implementations with any malicious logic. Currently, the source code of all LPs is not verified and includes malicious logic in the burn() function. 

This function was called on each LP contract to drain a huge share of liquidity from them.

Currently, all stolen funds are bridged to the Ethereum Mainnet as ETH and stored in the account: 0xaF8f284e93c5bF5795ccA636D8AeE62a2616e21d

  


 **Block Data Reference**

Scammer addreses:

https://arbiscan.io/address/0xaf8f284e93c5bf5795cca636d8aee62a2616e21d

https://etherscan.io/address/0xaF8f284e93c5bF5795ccA636D8AeE62a2616e21d

  


Liquidity draining TXs:

https://arbiscan.io/tx/0xbe0e8d8304f1057a19cb15e1bbb8917d1e3dac60e9b779ab628d9a4c1ce17112

https://arbiscan.io/tx/0xe7275b599228ffe565a9894011c949c3037a2ad90dc1b1adee14284bfe02b307

https://arbiscan.io/tx/0xe197f911e263ee6079db65398b3a7e4dbf2fdff5cce9dbe79c43137eed4c187f

https://arbiscan.io/tx/0x874e189e44ef1d378a0c94bf9a2df2102444f55e7c08dde658fa72cf05667f66

https://arbiscan.io/tx/0xf3b3099021a657383c5af009ffa0fdbabb062d7cc360c2de96b018299533540a

https://arbiscan.io/tx/0x4812d74fd976e42798f4b61e6a008fcec0f89ba1cf51ffab94051bfdd651c7bc

https://arbiscan.io/tx/0x67ac2279d9ac0cb49bc5269c8edc79f4a999fcffa08eb2ddcbb0a196470723b1

https://arbiscan.io/tx/0xb0f0bc34f36c12cf32c94a1965999e400bb84ce3bc56eb3d8e3303eca2e8effc

https://arbiscan.io/tx/0x48805ffac3d061aff5d96b115e2991a01be87083432d900f725575e3c7123876

  



Proof Links:
- [https://twitter.com/olimpiocrypto/status/1609183982821818369](https://twitter.com/olimpiocrypto/status/1609183982821818369)
- [ https://twitter.com/DefiyieldSec/status/1609273620039090176]( https://twitter.com/DefiyieldSec/status/1609273620039090176)


