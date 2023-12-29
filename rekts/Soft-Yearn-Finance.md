# Soft Yearn Finance
![Soft Yearn Finance](/rektimages/Soft-Yearn-Finance.png)
- Amount Lost: $281,382.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2020-9-3

The protocol did not handle the rebase event correctly. It enabled a user to start Uniswap sell transaction immediately following the modification of wallet balances, but before any price change in the token was registered.  
  
The rebase event functioned wrong. Because the YFI to SYFI conversion rate was incorrectly entered, an erroneous balance change was started. Together, these two errors permitted a transaction to be initiated that would basically remove the pool's aggregate cash.  
  
The transaction, where the external address buys 2 SYFI using 0.5 ETH on the Uniswap:  
https://etherscan.io/tx/0xed33e727dd5b2f8e5164f6e15dabc1923652f2e933645378a87c45bf33c4e59a  
  
15 minutes later, the same external address sells 15,551 SYFI for 747 ETH after the positive rebase event:  
https://etherscan.io/tx/0xbb45a3aaa222432f50974b4be0852445e446698d33b0fcd47a4f627a2764ea83


Proof Links:
- [https://www.forbes.com/sites/nicholasgans/2020/09/09/another-project-bites-the-dust-how-someone-turned-200-into-250k/?sh=2fe5c2a86a39](https://www.forbes.com/sites/nicholasgans/2020/09/09/another-project-bites-the-dust-how-someone-turned-200-into-250k/?sh=2fe5c2a86a39)
- [ https://cointelegraph.com/news/jackpot-user-turns-200-into-250k-thanks-to-a-buggy-defi-protocol]( https://cointelegraph.com/news/jackpot-user-turns-200-into-250k-thanks-to-a-buggy-defi-protocol)


