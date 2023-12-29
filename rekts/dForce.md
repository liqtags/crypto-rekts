# dForce
![dForce](/rektimages/dForce.png)
- Amount Lost: $3,650,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2023-2-10

**Quick Summary**

On February 10th, the dForce protocol was exploited, and the attacker made a profit worth 3.65 million dollars. 

  


 **Details of the Exploit**

On February 10th, the DeFi aggregator platform dForcenet was attacked and the attacker made a profit of approximately $3.65 million. The attacker used flashloans to borrow WETH and swapped it into ETH, then added liquidity to the wstETH/ETH pool on Curve, earning wstETHCRV tokens. They deposited some of the tokens in the Curve wstETHCRV-gauge, receiving wstETHCRV-gauge tokens, which were used to deposit in the dForce wstETH/ETH Vault and mint share tokens and USX tokens. The attacker then removed liquidity using the remove_liquidity function, which triggered the fallback function of the attack contract, ultimately decreasing the virtual price in the wstETH/ETH pool. The attacker then liquidated other users in the dForce wstETH/ETH Vault, profiting from the manipulated virtual price. The hacked funds are still in the attacker's address as of now. The root cause was the attacker's exploitation of the process of transferring native tokens before burning LP when removing liquidity in the wstETH/ETH Pool, triggering the callback for receiving native tokens to manipulate virtual prices and liquidate other users for profit.

  


 **Block Data Reference**

Exploit TXs:

https://optimistic.etherscan.io/tx/0x6c19762186c9f32c81eb2a79420fc7ad4485aa916cab37ec278b216757bfba0d

https://phalcon.blocksec.com/tx/arbitrum/0x5db5c2400ab56db697b3cc9aa02a05deab658e1438ce2f8692ca009cc45171dd


Proof Links:
- [https://twitter.com/BlockSecTeam/status/1623901011680333824](https://twitter.com/BlockSecTeam/status/1623901011680333824)
- [ https://twitter.com/SlowMist_Team/status/1623956763598000129]( https://twitter.com/SlowMist_Team/status/1623956763598000129)


