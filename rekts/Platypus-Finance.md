# Platypus Finance
![Platypus Finance](/rektimages/Platypus-Finance.png)
- Amount Lost: $51,840.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-7-11

**Quick Summary**

Platypus Finance, an Avalanche-based DEX, was exploited in a reentrancy attack causing a loss of 51,840 $USD.

  


 **Details of the Exploit**

Platypus Finance faced an exploit that caused a loss of approximately $51k. The exploit emerged due to an issue with the liquidity conversion calculation for LP-USDC, which resulted in an excessively large quantity calculation for USDC.e when swapping USDC for USDC.e. The call to asset.addLiability() in the _deposit function caused an increase in the asset.liability() parameter in withdrawFrom, allowing the hacker to withdraw more USDC.e than the amount of USDC previously deposited. The funds remain in the attacker's address, amounting to $31,120 worth of assets in Avalanche and $20,450 worth of $DAI in Ethereum chain.

  


 **Block Data Reference**

Attacker Address:

https://showtrace.io/address/0xc64afc460290ed3df848f378621b96cb7179521a

  


Malicious Transaction Example:

https://showtrace.io/tx/0x5e785b87e62252b1fff3283ce260d74cb5b3efc4588d7a0297f505482cbab388

  


Malicious Contract Address:

https://showtrace.io/address/0x16a3c9e492dee1503f46dea84c52c6a0608f1ed8


Proof Links:
- [https://twitter.com/BeosinAlert/status/1678943417974378496](https://twitter.com/BeosinAlert/status/1678943417974378496)


