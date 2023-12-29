# ApeRocket
![ApeRocket](/rektimages/ApeRocket.png)
- Amount Lost: $260,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-7-14

The attacker's address:  
https://bscscan.com/address/0x53d07afa123702469ab6cf286e9ff7033a7eff65  
  
The transaction behind the attack:  
https://bscscan.com/tx/0x701a308fba23f9b328d2cdb6c7b245f6c3063a510e0d5bc21d2477c9084f93e0  
  
The attacker:  
\- borrowed 1.6M CAKE ($21.8M) of flash loan from PancakeSwap  
  
\- added 509K CAKE of deposit to the CAKE vault. Got the majority share (99.5%) of the vault  
  
\- sent 1.1M CAKE to the CAKE vault contract  
  
\- called _harvest_ () and _getReward_ () on the CAKE vault  
  
\- with the rather large amount of CAKE token in the wallet balance of the vault contract (sent by the hacker at step 3), it returned a large amount of profit. As a result, the system minted 508K SAPCE as a reward to the attacker  
  
\- repeated one more time  
  
\- swapped the rewarded SPACE token to CAKE, repaid the flash loan  
  
\- taken out 883 BNB.  
  
By delivering a large number of CAKE tokens to the vault and calling harvest(), the profit amount for everyone in the vault is increased. Despite the fact that the hacker owns the bulk of the vault, virtually all of the earnings will be returned to the hacker.


Proof Links:
- [https://aperocket.medium.com/moving-forward-24b9ae22c428](https://aperocket.medium.com/moving-forward-24b9ae22c428)
- [ https://watchpug.medium.com/aperocket-finance-performance-fee-minting-incident-root-cause-analysis-b959c1e963ba]( https://watchpug.medium.com/aperocket-finance-performance-fee-minting-incident-root-cause-analysis-b959c1e963ba)


