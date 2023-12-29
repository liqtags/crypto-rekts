# Wault Finance
![Wault Finance](/rektimages/Wault-Finance.png)
- Amount Lost: $800,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-8-4

The attacker:  
https://bscscan.com/address/0x886358f9296de461d12e791bc9ef6f5a03410c64  
  
The transaction behind the attack:  
https://bscscan.com/tx/0x31262f15a5b82999bf8d9d0f7e58dcb1656108e6031a2797b612216a95e1670e  
  
The attacker:  
\- flash loaned 16.8M WUSD from WSwap’s WUSD-USDT pool and redeemed it for 15M USDT and 106M WEX  
  
\- flash loaned 40M USDT from PCS’s WBNB-USDT pool  
  
\- swapped a part of the flash loaned USDT to WEX before the price is pumped  
  
\- staked the flash loaned USDT to WUSDMaster contract. The 10% of staked USDT was used to buy WEX and the attacker gained the WUSD with a 1:1 rate  
  
\- since there was a limit on the staking amount, the attacker performed the previous step repeatedly to increase the WEX price with almost no cost  
  
\- gained profit in USDT by swapping WEX from steps 1 and 3 back to USDT  
  
\- returned the flash loaned WUSD and USDT  
  
\- swapped the remaining WUSD and the USDT profit to ETH.


Proof Links:
- [https://watchpug.medium.com/wault-wusd-minting-attack-root-cause-analysis-73b055499c6e](https://watchpug.medium.com/wault-wusd-minting-attack-root-cause-analysis-73b055499c6e)
- [ https://inspexco.medium.com/wault-finance-incident-analysis-wex-price-manipulation-using-wusdmaster-contract-c344be3ed376]( https://inspexco.medium.com/wault-finance-incident-analysis-wex-price-manipulation-using-wusdmaster-contract-c344be3ed376)
- []()


