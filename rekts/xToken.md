# xToken
![xToken](/rektimages/xToken.png)
- Amount Lost: $4,500,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-8-29

**Quick Summary**

The exploitation of Synthetix and Bancor protocols led to a loss of $24.5M in ETH, BNT, SNX, and xBNTa tokens.

  


 **Details of the Exploit**

The attacker initiated the exploit by borrowing a 61.8k ETH flash loan from dYdX. They then deposited 10k ETH to borrow 564k SNX on Aave and swapped 5.5k ETH for 700k SNX on SushiSwap. The attacker sold 1.2M SNX for 818 ETH on Uniswap v2, significantly reducing the SNX price. They then used only 0.12 ETH to mint 1.2B xSNXa, because the protocol buys SNX through Kyber, who in turn led to use Uniswap v2 for this swap. However, within the protocol, the xSNXa price turned out to be normal, which made it possible to swap 105M xSNX into 414 ETH. The attacker then began to do reverse swaps in SushiSwap and Uniswap and repaid loans in Aave. They began to sell the existing xSNXa to the Balancer SNX/ETH/xSNXa (25/25/50) pool, repaid the flash loan to dYdX, issued xBNTa four times for 0.03 ETH, which ultimately gave them 3.9B xBNTa, and swapped half of xBNTa to 781k BNT.

  


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
- [https://medium.com/xtoken/xsnx-post-mortem-666d35071f38](https://medium.com/xtoken/xsnx-post-mortem-666d35071f38)
- [ https://rekt.news/xtoken-rekt-x2/]( https://rekt.news/xtoken-rekt-x2/)


