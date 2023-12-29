# Ref Finance
![Ref Finance](/rektimages/Ref-Finance.png)
- Amount Lost: $3,202,539.00
- Funds Returned: $3,202,539.00
- Category: Exchange (DEX)
- Date: 2021-8-15

On August 14 at around 11 am UTC, the Ref Finance dev team deployed a hotfix to an issue surrounding the Ref Finance contracts. Prior to the fix, users that unstaked all of their tokens from the farm contract were unable to remove the deposited liquidity from the pool. This occurred due to the users’ NEAR account being unregistered from the LP token contract, a feature unique to NEAR tokens that generally aids the user experience.  
  
While the hotfix solved that issue, it contained a new issue that did not debit users’ LP token balances when they removed liquidity. This allowed a small number of users to continuously remove tokens, receiving far more tokens than they should have.  
  
In total, 507,000 NEAR and ~1 million REF tokens were withdrawn using this exploit. Over 400,000 of the NEAR were sent to Binance and Huobi.


Proof Links:
- [https://ref-finance.medium.com/a-post-mortem-on-the-ref-finance-exploit-what-happened-9f6140bafde6](https://ref-finance.medium.com/a-post-mortem-on-the-ref-finance-exploit-what-happened-9f6140bafde6)


