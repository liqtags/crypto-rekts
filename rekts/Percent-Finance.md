# Percent Finance
![Percent Finance](/rektimages/Percent-Finance.png)
- Amount Lost: $1,900,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2020-11-4

The problem was that the old interest rate contracts have different signatures for ` _getSupplyRate_ ` and ` _getBorrowRate_ `. They return 2 uint values, the first one being an error code. So, after the swap, they were unable to call these functions on the new interest rate contracts, as the signatures do not match. Making the problem worse, these functions are checked before every interaction with these contracts (supplying, borrowing, redeeming, repaying, etc). They are also checked before changing the interest rate contract again. So, because the current interest rate contract does not work, it is impossible to change to a new one.

This meant that these 3 contracts were no longer usable, and the user funds in them were permanently locked. These amounted to: 446,813 USDC, 28 wBTC and 313 ETH.


Proof Links:
- [https://percent-finance.medium.com/percent-finance-incident-post-mortem-d4e419cf35ab](https://percent-finance.medium.com/percent-finance-incident-post-mortem-d4e419cf35ab)
- [ https://percent-finance.medium.com/important-announcement-d35f9a0df112]( https://percent-finance.medium.com/important-announcement-d35f9a0df112)


