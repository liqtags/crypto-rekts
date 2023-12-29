# PolBase Cash
![PolBase Cash](/rektimages/PolBase-Cash.png)
- Amount Lost: $353,807.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-1-7

**Quick Summary**

PolBase Cash was an algorithmic stable coin project that contained unverified smart contracts which empowered the contract deployer to withdraw funds from the operation. Investors were deprived of $350k.

  


 **Details of the Exploit**

PolBase Cash an algorithmic stable coin project that boasted three coins. $PBC (PolBase Cash) was the dollar pegged stable coin. In order to enable stabilization mechanisms $PBB (PolBase Bonds) and $PBS (PolBase Share) were introduced, similar to the popular Tomb Finance protocol on the Fantom network.

The contract deployer created four smart contracts for staking $USDT, $USDC, DAI and LP tokens separately. The staking contracts were unverified, meaning the code was not visible on the block explorer for everyone to review.

The contract deployer interacted with these 4 smart contracts using function _setOperation_ () with the below address as input data:  
0x5C0D86B9c5de0b2b88895a6Cb0441a0Cdd5d52eA.  
This address received permission to withdraw funds from the staking smart contracts. The stolen funds were then transferred to a variety of external wallets. In addition, the liquidity from the pair was removed by this address as well:  
https://etherscan.io/tx/0xbf17223dc8c0aba097a79ec1e63b40fee758dd62ece339384de20a15a51d62fc

  


 **Block Data Reference**

USDT staking contract:

https://etherscan.io/address/0x4f2582fe5e50b5c77cb5f57e6bc958b49fe3381b

USDC staking contract:

https://etherscan.io/address/0x2b3e2fe7c8718353fc6cebaa79451c7193025bc3

DAI staking contract:

https://etherscan.io/address/0xa72180b8ce83f5717228d87bed3ef520093faf2c

LP contract:

https://etherscan.io/address/0x386e747afbd6cf412a055816820fa0d4948b63a9

  


Outgoing transactions could be found at:  
https://bloxy.info/address/0x5c0d86b9c5de0b2b88895a6cb0441a0cdd5d52ea


Proof Links:
- [https://twitter.com/CaptainJackAPE/status/1347043179976003585](https://twitter.com/CaptainJackAPE/status/1347043179976003585)


