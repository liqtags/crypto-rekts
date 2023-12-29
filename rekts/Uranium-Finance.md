# Uranium Finance
![Uranium Finance](/rektimages/Uranium-Finance.png)
- Amount Lost: $1,300,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-4-8

The attacker's address:  
https://bscscan.com/address/0x36ad9ee78bfb730955993d2aa77ecccf95e3313e  
  
The exploited contract:  
https://bscscan.com/address/0xd5aac41d315c1d382dcf1c39d4ed9b37c224edf2  
  
The attacker:  
\- called the _deposit_ () function to increase the value of _u_ _ser.amountWithBonus_  
https://bscscan.com/tx/0x09976b55015997df711be8f911afe6db2f21b40728532f16ee96257b4a52a48f  
  
\- called the _emergencyWithdraw_ () function to get his deposit back and set _user.rewardDebt_ equal to 0  
https://bscscan.com/tx/0x730ad83dd0aa96519a8876ef28f26620ad6a4ca7a614d2aca661b51e874c6c07  
  
\- called the _withdraw_ () function to receive the RADS/sRADS reward tokens  
https://bscscan.com/tx/0xb9b7005fcf0b05161c5db136092372c743e74b48ecf7e85e588a84fee777ffcf  
  
\- repeated the process to drain most of the reward tokens from the pool.  
  
Reward tokens were withdrawn from the MasterChef contract onto the attacker's address multiple times at:  
https://explorer.bitquery.io/bsc/txs/transfers?receiver=0x36ad9ee78bfb730955993d2aa77ecccf95e3313e&currency=0x7ca1ebc56496e3d78e56d71a127ea9d1717c4be0  
  
Received tokens were sold for $1.3M worth of BUSD and BNB.


Proof Links:
- [https://uraniumfinance.medium.com/uranium-post-mortem-v2-compensations-aac4b0706d7d](https://uraniumfinance.medium.com/uranium-post-mortem-v2-compensations-aac4b0706d7d)
- [ https://medium.com/certik-foundation/uranium-finance-exploit-analysis-d135055d6a6a]( https://medium.com/certik-foundation/uranium-finance-exploit-analysis-d135055d6a6a)


