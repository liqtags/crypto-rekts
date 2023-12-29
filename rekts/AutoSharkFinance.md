# AutoSharkFinance
![AutoSharkFinance](/rektimages/AutoSharkFinance.png)
- Amount Lost: $759,046.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-5-24

The transaction behind the attack:  
https://bscscan.com/tx/0xfbe65ad3eed6b28d59bf6043debf1166d3420d214020ef54f12d2e0583a66f13  
  
The attacker's address:  
https://bscscan.com/address/0xd9c7efe29f3e90ce3630ea1c665217c7ab298a3b  
  
The attacker:  
\- added a small sum of deposit to the SHARK-BNB Vault:  
https://bscscan.com/tx/0x2a2003fb4c57c0e03dfbdda8eb695ef8f39022df30da977942d930fffbb8e125  
  
\- borrowed 100K BNB of flash loan from PancakeSwap  
  
\- swapped 50K BNB into SHARK token and sent them alongside the rest 50K BNB to the SharkMinter contract  
  
\- called _getReward_ () with the deposit of SHARK-BNB Vault from the first step  
  
\- with the huge amount of SHARK token and WBNB in the wallet balance of the minter contract, it returned an extremely large amount of profit. As a result, the system minted 100M SHARK as a reward to the hacker  
  
\- sold SHARK token for 102K WBNB, repaid flash loans, taken out 2.2K WBNB  
  
\- exchanged BNB on ETH at:  
https://bscscan.com/tx/0xa6e265b96d92a24b1b3307f14367ac18031c33062fa6c195331db50417011df7  
  
\- bridged ETH into Ethereum network:  
https://bscscan.com/tx/0x33c01cf4885553542a8b820ef57f079ea8fe165e41b57d30b5492cfe47b0ba3b


Proof Links:
- [https://medium.com/autosharkfin/how-autoshark-got-economically-exploited-3c644de5073a](https://medium.com/autosharkfin/how-autoshark-got-economically-exploited-3c644de5073a)
- [ https://watchpug.medium.com/sharkfinance-performance-fee-minting-incident-analysis-4b2e3bd03923]( https://watchpug.medium.com/sharkfinance-performance-fee-minting-incident-analysis-4b2e3bd03923)
- [ https://rekt.news/autoshark-rekt/]( https://rekt.news/autoshark-rekt/)


