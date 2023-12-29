# DEUS Finance
![DEUS Finance](/rektimages/DEUS-Finance.png)
- Amount Lost: $3,024,325.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-3-15

The attacker's address:  
https://ftmscan.com/address/0x1ed5112b32486840071b7cdd2584ded2c66198dd  
  
The transaction behind the attack:  
https://ftmscan.com/tx/0xe374495036fac18aa5b1a497a17e70f256c4d3d416dd1408c026f3f5c70a3a9c  
  
The hack is made possible due to the flash loan-assisted manipulation of the price oracle that takes the price from the pair of StableV1 AMM - USDC/DEI.  
  
The attacker:  
\- flash loaned 9,739342 DEI via SPIRIT-LP_USDC_DEI  
  
\- flash loaded 24,772,798 DEI out of the sAMM-USDC/DEI pair (used as price oracle to calculate the collateral value)  
  
\- liquidated users  
  
\- repaid the borrowed 24,772,798 DEI to the sAMM-USDC/DEI pair  
  
\- burnt the liquidated LP token to get 5,218,173 USDC + 5,246,603 DEI  
  
\- swapped 5,218,173 USDC to 5,170,594 DEI  
  
\- repaid the flash loan with 3,001,552 DEI as hack profit.  
  
The attack profit was bridged via Multichain to Ethereum:  
https://ftmscan.com/tx/0x09dc3a1afd1dae211c31d7ad4b5cd6f68c9350727fa5d4c7c63efb9d287e3210  
  
Then funds were deposited into Tornado Cash mixer to hide traces:  
https://etherscan.io/address/0x1ed5112b32486840071b7cdd2584ded2c66198dd


Proof Links:
- [https://lafayettetabor.medium.com/deus-post-mortem-3c65df12927f](https://lafayettetabor.medium.com/deus-post-mortem-3c65df12927f)
- [ https://rekt.news/deus-dao-rekt/]( https://rekt.news/deus-dao-rekt/)
- [ https://twitter.com/peckshield/status/1503632734299701250]( https://twitter.com/peckshield/status/1503632734299701250)


