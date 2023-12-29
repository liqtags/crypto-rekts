# OMNI
![OMNI](/rektimages/OMNI.png)
- Amount Lost: $1,430,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,NFT
- Date: 2022-7-10

**Quick Summary**

A reentrancy attack was carried out on the OMNI protocol, yielding the attacker 1300 $ETH, which were subsequently laundered through Tornado.cash.

  


 **Details of the Exploit**

OMNI is a NFT finance platform that lends out cryptocurrency in exchange for staked NFTs. This platform allows users to stake NFT tokens to receive fungible tokens e.g. $ETH. The attacker deposited NFTs from the collection Doodles that were used as a collateral to borrow $WETH. Then the attacker exploited a vulnerability in order to execute a reentrancy attack by withdrawing all NFTs deposited as collateral by the attacker except for one NFT. This action triggered a malicious callback function that allowed the attacker to buy more Doodles before  liquidating the loan position: 

https://etherscan.io/tx/0x05d65e0adddc5d9ccfe6cd65be4a7899ebcb6e5ec7a39787971bcc3d6ba73996

When the position is liquidated, the remaining Doodle NFT from the collateral were returned to the attacker. The credit position is liquidated because NFT value from initial collateral is insufficient to cover the debt position. As the attacker is able to force through using the borrowed WETH to buy more NFTs before the liquidation occurs. As a result, the money received from the attack was withdrawn through Tornado.cash.

 

 **Block Data Reference**

Attacker account address: https://etherscan.io/address/0x627a22ff70cb84e74c9c70e2d5b0b75af5a1dcb9

Attacker contract address: https://etherscan.io/address/0x5992f10a5b284be845947a1ae1694f8560a89fa8

Contract creations transaction: https://etherscan.io/tx/0x193016ce1ed6c7ec6377efd89309f7415c21190619b8e1fe625a6cdcca4f5ba5

Exploited smart contract address: https://etherscan.io/address/0xba12222222228d8ba445958a75a0704d566bf2c8


Proof Links:
- [https://www.theblock.co/post/156800/hacker-drains-1-4-million-worth-of-eth-from-nft-lender-omni](https://www.theblock.co/post/156800/hacker-drains-1-4-million-worth-of-eth-from-nft-lender-omni)
- [ https://cryptopotato.com/nft-platform-omni-hit-by-re-entrancy-exploit-lost-1-4m-in-eth/]( https://cryptopotato.com/nft-platform-omni-hit-by-re-entrancy-exploit-lost-1-4m-in-eth/)
- [ https://dailycoin.com/1300-eth-stolen-from-nft-lending-platform-omni-in-re-entrancy-exploit/]( https://dailycoin.com/1300-eth-stolen-from-nft-lending-platform-omni-in-re-entrancy-exploit/)
- [ https://m.investing.com/news/cryptocurrency-news/1300-eth-stolen-from-nft-lending-platform-omni-in-reentrancy-exploit-2845944?ampMode=1]( https://m.investing.com/news/cryptocurrency-news/1300-eth-stolen-from-nft-lending-platform-omni-in-reentrancy-exploit-2845944?ampMode=1)


