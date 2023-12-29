# yearn.finance
![yearn.finance](/rektimages/yearn.finance.png)
- Amount Lost: $11,512,509.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,Yield Aggregator
- Date: 2023-4-13

**Quick Summary**

Yearn Finance and Aave Protocol were exploited via a flash loan attack, resulting in the loss of 11,512,509 $USD worth of $ETH and $DAI. 

  


 **Details of the Exploit**

Yearn Finance is a Yield Aggregator, and Aave Protocol is a Lending and Borrowing platform. The hacker performed an attack using two malicious smart contracts. The attack started with the exploiter taking a flash loan for 2,000,000 $USDT, 5,000,000 $USDC, and 5,000,000 $DAI from Balancer. Borrowed assets are used to exploit Yearn Finance’s USDT pool vulnerability and mint a big amount of ycUSDT (~204 billion) and yUSDT (~33 trillion) tokens then swap them for various stablecoins worth 11,512,509 $USD. Another smaller attack took place during the exploit which affected Aave’s LendingPoolCoreV1 contract. Worth noticing that the exploiter repaid all users USDT positions in the Aave V1 protocol. During multiple transactions stolen assets were transferred to destination wallets part of which as 1,000 $ETH was bridged through TornadoCash.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x5bac20beef31d0eccb369a33514831ed8e9cdfe0

  


Attacker wallets with funds:

https://etherscan.io/address/0x16af29b7efbf019ef30aae9023a5140c012374a5 

https://etherscan.io/address/0x6f4a6262d06272c8b2e00ce75e76d84b9d6f6ab8

  


Malicious transaction examples:

https://etherscan.io/tx/0x8db0ef33024c47200d47d8e97b0fcfc4b51de1820dfb4e911f0e3fb0a4053138

https://etherscan.io/tx/0xd55e43c1602b28d4fd4667ee445d570c8f298f5401cf04e62ec329759ecda95d

  


Malicious Contracts:

https://etherscan.io/address/0x8102ae88c617deb2a5471cac90418da4ccd0579e

https://etherscan.io/address/0x9fcc1409b56cf235d9cdbbb86b6ad5089fa0eb0f


Proof Links:
- [https://www.theblock.co/post/226134/exploit-involving-aave-v1-and-yearn-estimated-to-be-around-10-million-peckshield](https://www.theblock.co/post/226134/exploit-involving-aave-v1-and-yearn-estimated-to-be-around-10-million-peckshield)
- [ https://blog.solidityscan.com/yearn-finance-hack-analysis-misconfigured-yusdt-mint-5196761b70ac]( https://blog.solidityscan.com/yearn-finance-hack-analysis-misconfigured-yusdt-mint-5196761b70ac)
- [ https://twitter.com/beosinalert/status/1646413885409476608]( https://twitter.com/beosinalert/status/1646413885409476608)


