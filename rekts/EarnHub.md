# EarnHub
![EarnHub](/rektimages/EarnHub.png)
- Amount Lost: $244,938.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-2-7

The exploiter's address:  
https://bscscan.com/address/0x3d98aee279c82d8178b87d9d4dc442d65224dacc  
  
Attacker contract A:  
https://bscscan.com/address/0x89011932e486fc3548f82c279eb502ba7b4ad55f  
  
Attacker contract B:  
https://bscscan.com/address/0xf7acfa1ce0e235e7072fa76bd0dc3c3e519bdfe5  
  
The root of the issue:  
The _makeHop()_ function allowed shareholders to shift their funds through different staking pools in a gas-efficient manner. This feature was intended to be implemented on the next dApp update, however, it’s been around for about 1 month on the contract side.  
  
The issue is in the line below, which assumes that there can not be a malicious smart contract on the pool that is called on _receiveHop_ (_pool):  
  
tokenPool.stakingToken.approve(address(_newPool),  
tokenPool.stakingToken.totalSupply());  
  
By approving the totalSupply to the new pool, Contract B was able to have allowance to spend the staking contract tokens. This basically means they were able to withdraw them from the staking contract at a whim once that initial setup was made.  
  
The attacker:  
\- created contract A

\- created contract B

\- the attacker contract then proceeded to buy some EarnHub, stake it, and make it hop to contract B (makeHop(contractBaddress))

\- after receiving the hop, the contract was able to drain the funds from the staking contract by just using the _transferFrom_ () function repeated times.  
  
The example transaction:  
https://bscscan.com/tx/0x40e69064c70d7db8b2dcbad441da9a06a507f8f90959da3c2583242f89e01d3c  
  
Stolen funds were deposited into Tornado Cash mixer:  
https://explorer.bitquery.io/bsc/address/0x3d98aee279c82d8178b87d9d4dc442d65224dacc/outflow


Proof Links:
- [https://earnhub.medium.com/b9d39169655f](https://earnhub.medium.com/b9d39169655f)
- [ https://twitter.com/earnhubBSC/status/1490822840991744000]( https://twitter.com/earnhubBSC/status/1490822840991744000)
- [ https://twitter.com/peckshield/status/1490844427794862084]( https://twitter.com/peckshield/status/1490844427794862084)


