# xWin Finance
![xWin Finance](/rektimages/xWin-Finance.png)
- Amount Lost: $270,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-6-25

The attacker's address:  
https://bscscan.com/address/0xb63f0d8b9aa0c4e68d5630f54bfefc6cf2c2ad19  
  
The transaction behind the attack:  
https://bscscan.com/tx/0xba0fa8c150b2408eec9bbbbfe63f9ca63e99f3ff53ac46ee08d691883ac05c1d  
  
The attacker:  
\- flash loaned 76,000 BNB from Fortube Bank  
  
\- swapped 37999.99 BNB for 95.409 xWin tokens via PancakeSwap V1 BNB+xWin Pool due to an invalid slippage control in the _xWinFundP::_swapBNBToTokens_ () function  
  
\- deposited 37999.99 BNB and 0.003 xWin tokens into PancakeSwap V1 BNB+xWin Pool as liquidity and minted in return 11.28 PancakeSwap LP tokens. Got an extra amount of xWin tokens as a reward from xWin Finance  
  
\- swapped 95.406 xWin tokens for 75995.77 BNB via the above PancakeSwap V1 BNB+xWin Pool and burnt 11.28 PancakeSwap V1 LP tokens to get 4.19 BNB  
  
\- repeated one to four twenty times, the attacker got about an extra 303,998.86 xWin tokens reward from xWin Finance for this attack  
  
\- swapped 303,998.86 xWin tokens for 903.92 BNB via PancakeSwap V2 BNB+xWin Pool and returned the flash loan in the first step  
  
607,998 xWin tokens were transferred to the attacker, and then it was used to swap for BNB. This incident was due to a bug in the internal __swapBNBToTokens_ () function of the _xWinFund_ contract which implements a price slippage control.


Proof Links:
- [https://xwin.medium.com/summary-of-the-misuse-of-flash-loan-against-xwin-protocol-a04f7719a0ee](https://xwin.medium.com/summary-of-the-misuse-of-flash-loan-against-xwin-protocol-a04f7719a0ee)
- [ https://peckshield.medium.com/xwin-finance-incident-root-cause-analysis-71d0820e6bc1]( https://peckshield.medium.com/xwin-finance-incident-root-cause-analysis-71d0820e6bc1)


