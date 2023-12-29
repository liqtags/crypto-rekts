# Eleven Finance
![Eleven Finance](/rektimages/Eleven-Finance.png)
- Amount Lost: $4,500,000.00
- Funds Returned: $4,200,000.00
- Category: Yield Aggregator
- Date: 2021-6-22

The attacker's address:  
https://bscscan.com/address/0xc71e2f581b77de945c8a7a191b0b238c81f11ed6  
  
The transaction behind the attack:  
https://bscscan.com/tx/0x6450d8f4db09972853e948bee44f2cb54b9df786dace774106cd28820e906789  
  
The attacker:  
\- borrowed a flash loan from PancakeSwap with 953,869.62 BUSD, which is returned at the last step with the necessary fee to cover the flash loan cost  
  
\- swapped 340,631.23 BUSD for 474,378.75 NRV via PancakeRouter  
  
\- added liquidity with 474,378.75 NRV and 366,962.02 USDT into NRV+BUSDT pool via PancakeRouter and minted in return 411,515.29 Pancake LP tokens  
  
\- deposited 411,515.29 Pancake LP tokens into Eleven Finance via _ElevenNeverSellVault_ and obtained 411,515.29 11 nrvBUSD LP tokens  
  
\- called _emergencyburn_ () to withdraw 411,515.29 Pancake LP tokens without burning any 11 nvrBUSD LP token. Then called _withdrawAll_ () to get extra 411,515.29 Pancake LP tokens with the related 11 nvrBUSD LP tokens burned.


Proof Links:
- [https://elevenfinance.medium.com/eleven-finance-nrv-vault-exploit-and-loss-of-funds-a-post-mortem-437a79ded743](https://elevenfinance.medium.com/eleven-finance-nrv-vault-exploit-and-loss-of-funds-a-post-mortem-437a79ded743)


