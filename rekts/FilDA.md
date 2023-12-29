# FilDA
![FilDA](/rektimages/FilDA.png)
- Amount Lost: $2,000,000.00
- Funds Returned: $229,000.00
- Category: Borrowing and Lending
- Date: 2023-4-12

**Quick Summary**

On April 12th, 2022, an exploit occurred on FilDA resulting in compromised funds of up to $2 million. The dev team has identified the root cause and suspended all deposits and borrowing on FilDA-ESC. FilDA contracts on other chains remain unaffected.

  


 **Details of the Exploit**

The compromised funds amount to around 1.6 million USD and were mainly in the form of USDC, HUSD, BUSD, BTC, and ETH. The root cause of the issue is due to the protocol's inability to handle flashloans of ERC677 tokens properly. The attacker used a flashloan to borrow the underlying token, which was then deposited into the protocol via a callback function controlled by the attacker. This resulted in lots of extra f tokens being minted. The borrowed token was then returned to the protocol via a flashloan callback, but lots of fTokens were left to the attacker, allowing them to redeem most of the cash in the lending pool. FilDA on other chains is not affected since the issue is only related to ERC677 tokens.

  


 **Block Data Reference**

Attacker Address: 0x4a9a0cC103199F67730bdC61337d192788858874

Money Laundering address: 0x93c3A8051b8ba814eB5FB22d655681720E6a4d74

Attacker contract: 0x00Ff915E663F4037D18B0C83575Ac8f3D4D05BC3


Proof Links:
- [https://fildafinance.medium.com/filda-incident-community-update-ii-e80b05cd0d2](https://fildafinance.medium.com/filda-incident-community-update-ii-e80b05cd0d2)
- [ https://twitter.com/FilDAFinance/status/1650440170699739141?s=20]( https://twitter.com/FilDAFinance/status/1650440170699739141?s=20)


