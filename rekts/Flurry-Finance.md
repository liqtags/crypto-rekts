# Flurry Finance
![Flurry Finance](/rektimages/Flurry-Finance.png)
- Amount Lost: $293,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-2-23

The attacker's address:  
https://bscscan.com/address/0x0f3c0c6277ba049b6c3f4f3e71d677b923298b35  
  
The malicious token contract:  
https://bscscan.com/address/0xb7a740d67c78bbb81741ea588db99fbb1c22dfb7  
  
The attacker deployed a malicious token contract, which is also used as the attack contract, and created a PancakeSwap pair for the token and BUSD.  
  
The attacker made a flash loan from the Rabbit Bank contract and called the execute function on StrategyLiquidate:  
https://bscscan.com/address/0x5085c49828b0b8e69bae99d96a8e0fcf0a033369  
  
The execute method decodes input data as the LP token address, allowing the attacker to execute code from the malicious token contract.  
  
The malicious token contract called _FlurryRebaseUpkeep.performUpkeep_ () which rebases all vaults and updates multipliers for Rho Tokens. The update is based on all strategies' balances.  
  
The update was triggered in the process of a flash loan and the tokens borrowed from the Bank contract were not returned yet, the low balance led to a low multiplier.  
  
The attacker returned the flash loan and finished the preparation transaction.  
  
In the next transaction, the attacker deposited tokens with the low multiplier, updated the multiplier to a higher (normal) value, and withdrew the tokens with the high multiplier.  
  
Because the multiplier is one of the factors deciding the RhoToken balance, the attacker's RhoToken balance was increased in the transaction so they were able to withdraw more tokens than they deserve from the Vault.  
  
The attacker repeated this process multiple times.  
  
Stolen funds were transferred to this address and then redistributed between several external addresses:  
https://bscscan.com/address/0xb7a740d67c78bbb81741ea588db99fbb1c22dfb7#tokentxns


Proof Links:
- [https://twitter.com/FlurryFi/status/1496294559428780034](https://twitter.com/FlurryFi/status/1496294559428780034)
- [ https://twitter.com/CertiKCommunity/status/1496263106485444608]( https://twitter.com/CertiKCommunity/status/1496263106485444608)


