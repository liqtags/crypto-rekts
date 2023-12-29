# PolkaTrain
![PolkaTrain](/rektimages/PolkaTrain.png)
- Amount Lost: $3,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-4-5

Around 3:00 a.m. UCT + 8 on April 5, 2021, the smart contract of Polkatrain was attacked by hackers during the LBP auction, 57000 DOT were stolen in the contract and turned away.  
  
The LBP contract has a swap function and a rebate mechanism. When users buy PLOT tokens through the swap function, they get a certain amount of rebates, and the rebates will be It is sent to the user by calling _transferFrom_ in the __update_ function in the contract. Since the __update_ function does not set the maximum amount of rebates in a pool, nor does it determine whether the total rebates are used up when rebates, malicious arbitrageurs can continue to call the swap function to exchange tokens to get the contract. 


Proof Links:
- [https://polkatrain.medium.com/the-response-for-hacker-attack-incident-from-polkatrain-team-bdc13a56b0f6](https://polkatrain.medium.com/the-response-for-hacker-attack-incident-from-polkatrain-team-bdc13a56b0f6)
- [ https://hacked.slowmist.io/]( https://hacked.slowmist.io/)


