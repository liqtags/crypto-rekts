# Qubit Finance
![Qubit Finance](/rektimages/Qubit-Finance.png)
- Amount Lost: $80,000,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-1-27

**Quick Summary**

Qubit Finance lending protocol was hacked due to smart contract vulnerability. The hacker minted $xETH tokens to steal 80,000,000 worth of $BNB

  


 **Details of the Exploit**  

Qubit Finance is DeFi protocol for lending and borrowing on both Ethereum and Binance SmartChain. The protocol confirmed a hack on Twitter, 206,809 $BNB was stolen which was worth 80,000,000 $USD up to that time. The attack flow is below:  
The attacker:  
\- funded his wallet with 0.8887725 ETH from Tornado Cash

\- sent 16 deposit transactions to QBridge of Ethereum

\- sent 16 _voteProposal_ transactions to QBridge contract of BSC by Qubit Relayer

 \- a number of $xETH tokens were minted by 16 _voteProposal_ transactions, and liquidity in Qubit was withdrawn using this as collateral.  
  
The attacker called the QBridge deposit function on the Ethereum network, which calls the deposit function QBridgeHandler. QBridgeHandler should receive the $WETH token, which is the original _tokenAddress_ , and if the person who performed the tx does not have a $WETH token, the transfer should not occur.  
  
 _tokenAddress.safeTransferFrom_ (depositer, address(this), amount);  
  
In the deposit function above, _tokenAddress_ is 0, so _safeTransferFrom_ didn’t fail and the deposit function ended normally regardless of the amount value. Additionally, _tokenAddress_ was the $WETH address before _depositETH_ was added, but as _depositETH_ is added, it is replaced with the zero address that is the _tokenAddress_ of ETH.  
  
In summary, the deposit function was a function that should not be used after _depositETH_ was newly developed, but it remained in the contract, which allows the attacker to use this to steal the funds.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0xD01Ae1A708614948B2B5e0B7AB5be6AFA01325c7


Proof Links:
- [https://archive.is/0Ubc7](https://archive.is/0Ubc7)


