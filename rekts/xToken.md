# xToken
![xToken](/rektimages/xToken.png)
- Amount Lost: $24,000,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-5-12

**Quick Summary**

Exploitation of Synthetix's xSNXa contract led to a loss of 2.4k ETH, 781k BNT, and 407k SNX.

  


 **Details of the Exploit**

The attacker initiated the exploit by borrowing a 61.8k ETH flash loan on dYdX. They then deposited 10k ETH to borrow 564k SNX on Aave and swapped 5.5k ETH for 700k SNX on SushiSwap. The attacker sold 1.2M SNX for 818 ETH on Uniswap v2, significantly reducing the SNX price. They then used only 0.12 ETH to mint 1.2B xSNXa, exploiting the protocol's reliance on Kyber for SNX purchases. The attacker then swapped 105M xSNX into 414 ETH and began to do reverse swaps in SushiSwap and Uniswap and repaid loans in Aave. They then sold the existing xSNXa to the Balancer SNX/ETH/xSNXa pool, repaid the flash loan to dYdX, and issued xBNTa four times for 0.03 ETH, which ultimately gave them 3.9B xBNTa. They then swapped half of xBNTa to 781k BNT.

  


Stolen funds:

\- 2.4k ETH ($10.3M)

\- 781k BNT ($6.2M)

\- 407k SNX ($8M)

\- 1.9B xBNTa

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0x07e02088d68229300ae503395c6536f09179dc3e

The transaction behind the attack:

https://etherscan.io/tx/0x7cc7d935d895980cdd905b2a134597fb91004b5d551d6db0fb265e3d9840da22

  



Proof Links:
- [https://medium.com/xtoken/initial-report-on-xbnta-xsnxa-exploit-d6e784387f8e](https://medium.com/xtoken/initial-report-on-xbnta-xsnxa-exploit-d6e784387f8e)
- [ https://rekt.news/xtoken-rekt/]( https://rekt.news/xtoken-rekt/)


