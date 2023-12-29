# Blizzard
![Blizzard](/rektimages/Blizzard.png)
- Amount Lost: $1,109,632.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-11-13

The insider attack was performed by 2 team members: front-end and back-end developers.  
  
Developers had access to the key contracts as they were members of a multisignature account, which requires only 2 signs.  
  
1\. Whitehat reported found bug in the vault contracts to the Immunefi team  
2\. Whitehat received bug bounty and the core team of Blizzard asked the back-end developer to remove retired vaults, put 0 reward rate and disable deposits.  
3\. Front-end and back-end started testing new vaults:  
https://snowtrace.io/tx/0xf66a695d7df17771a649d9bf2c6076c324453c7a199d6da78dbc58b0baf3f48e  
  
4\. Back-end dev set the _rewardMintRate_ to 50 BLIZZ per block  
5\. Developers exploited the harvesting issue:  
https://snowtrace.io/tx/0xa7818cb803c1f29f4e5fd0d1cbc591e8514e07db4ed6042f76e23298c84b0363  
  
6\. Front-end dev had removed the retired PNG-AVAX vaults from the website front.  
7\. Developers exploited a single USDC vault:  
https://snowtrace.io/address/0xdb6969402dd0b431d26cdf539acffc6db649b64e#code  
  
8\. Developers dumped received tokens:  
https://snowtrace.io/tx/0x7cd6c8c8d8fb5d60a08780d95df01a257a00be910b3445130a2649394a00e482  
  
9\. Attackers used Anyswap bridge to transfer funds on Ethereum, and then, on the Binance Smart Chain  
https://snowtrace.io/tx/0x198c7303d1e9f05ac9da81b7d4b2a02c2ffcb735b56c84c331c7a3e00a111495  
  
10\. Stolen funds were deposited into Tornado Cash mixer at:  
https://explorer.bitquery.io/bsc/txs/transfers?sender=0xbb2c0ef4bad535e042b0f2686f83abec7e2ea965&currency=BNB&receiver=0x0d5550d52428e7e3175bfc9550207e4ad3859b17  
  
The exploit is described in 3 steps:

\- Modify the _rewardRate_ , by calling _setRewardMintRate_ (uint256 _rate) with the following parameter: 50000000000000000000

\- Deposit any amount of USDC and wait until the desired amount of tokens has been minted

\- Call _claim_ () to transfer the rewards from the origin pool and additional minted token rewards from the aggregator to the beneficiary.


Proof Links:
- [https://medium.com/@blizzardavalanche/blizzard-exploit-a-post-mortem-a09e19b04ae7](https://medium.com/@blizzardavalanche/blizzard-exploit-a-post-mortem-a09e19b04ae7)


