# Iron Finance
![Iron Finance](/rektimages/Iron-Finance.png)
- Amount Lost: $170,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2020-3-16

Two vFarms were exploited:

50% IRON — 50% SIL

50% IRON — 50% BUSD  
  
A user who farmed in these two pools claimed all SIL rewards allocated for farming over the next 12 months and made a profit of around $170K by selling SIL for BUSD on vSwap.  
  
Value DeFi team has upgraded FaaS, in which the reward rate is in normal integer instead of Ggwei as before. Iron.Finance team was unaware of the change and updated Iron vFarm pools with reward rate in Gwei. This caused the pools' rewards to inflated by 10^18 times.  
  
The following address took advantage of the mistake and drained all SIL rewards and sold them to the market:  
https://bscscan.com/address/0x69655181a55755adc854cd35c15995393f63e9e5#tokentxns


Proof Links:
- [https://ironfinance.medium.com/iron-finance-vfarms-incident-post-mortem-16-march-2021-114e58d1eaac](https://ironfinance.medium.com/iron-finance-vfarms-incident-post-mortem-16-march-2021-114e58d1eaac)
- [ https://beincrypto.com/iron-finance-defi-exploit-explained-post-mortem/]( https://beincrypto.com/iron-finance-defi-exploit-explained-post-mortem/)


