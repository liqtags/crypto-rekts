# ApeRocket
![ApeRocket](/rektimages/ApeRocket-2.png)
- Amount Lost: $1,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-7-14

The attacker's address:  
https://polygonscan.com/address/0xfabd1c2f4f16f2f6e2007abbed5549c84d82c19d  
  
The transaction behind the attack:  
https://polygonscan.com/tx/0x377fb92f6e04db4bf5a0917a79d171ce27b28deaa23594b7fc498dd080cf9d35  
  
The attacker:  
\- borrowed 24M DAI and 54M MATIC of flash loans from Aave  
  
\- created 25M DAIMATIC LP  
  
\- deposited 10M LP to the DAI-MATIC LP vault. Got the majority share (99%) of the vault  
  
\- deposited 15M LP from the MiniApeV2 contract of ApeSwap to the DAI-MATIC LP vault of ApeRocket  
  
\- called _withdrawAll_ () on the vault  
  
\- with the rather large amount of LP token added (deposited from ApeSwap’s MasterChef) by the attacker at step 3, it returned a large amount of profit. As a result, the system minted 2.5M pSAPCE as a reward to the attacker  
  
\- swapped the rewarded pSPACE token to ETH, repaid the flash loan  
  
\- taken out 521 ETH.  
  
The _deposit_ () function of ApeSwap Polygon's MiniApeV2 (a fork of SushiSwap's MiniChefV2) allows deposits to any address, which is not possible for a regular MasterChef v1, allowing the profit amount for everyone in the vault to be increased.

  


Even if the attacker owns the bulk of the vault, virtually all of the profit will be returned to the attacker.


Proof Links:
- [https://aperocket.medium.com/moving-forward-24b9ae22c428](https://aperocket.medium.com/moving-forward-24b9ae22c428)
- [ https://watchpug.medium.com/aperocket-polygon-performance-fee-minting-incident-root-cause-analysis-ed216f422f56]( https://watchpug.medium.com/aperocket-polygon-performance-fee-minting-incident-root-cause-analysis-ed216f422f56)


