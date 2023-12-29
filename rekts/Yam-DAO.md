# Yam DAO
![Yam DAO](/rektimages/Yam-DAO.png)
- Amount Lost: $750,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2020-8-13

The bug is in the rebase function of smart contract YAM.sol in the YAM project:  
https://github.com/yam-finance/yam-protocol/blob/767e3a4a6918b6fb6100ad6bb356164408f5d82f/contracts/token/YAM.sol#L340  
  
The rebase function was built to keep the token at a stable price. However, the line in the code mistakenly calculates the _totalSupply_ wrong, which would reserve too many minted tokens. The correct code/calculation equation for the line of code should be:  
  
totalSupply = initSupply.mul(yamsScalingFactor).div(BASE);  
  
The rebase bug led to the minting of decillions of YAM to the governance vault. As a result, a larger supply diluted the intended price. YAM token has lost more than 90% of its market capitalization. The bug resulted in a loss of funds worth $750,000.


Proof Links:
- [https://medium.com/yam-finance/yam-post-rescue-attempt-update-c9c90c05953f](https://medium.com/yam-finance/yam-post-rescue-attempt-update-c9c90c05953f)
- [ https://www.theblockcrypto.com/post/74810/yam-token-market-cap-collapses-by-more-than-90-flaw]( https://www.theblockcrypto.com/post/74810/yam-token-market-cap-collapses-by-more-than-90-flaw)
- [ https://medium.com/certik/2020-08-13-yam-finance-smart-contract-bug-analysis-future-prevention-b4220976ebea]( https://medium.com/certik/2020-08-13-yam-finance-smart-contract-bug-analysis-future-prevention-b4220976ebea)


