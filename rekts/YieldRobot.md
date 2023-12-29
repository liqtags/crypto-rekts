# YieldRobot
![YieldRobot](/rektimages/YieldRobot.png)
- Amount Lost: $2,100,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2023-1-17

**Quick Summary**

The Yield Robot contract on the Binance Smart Chain was rug pulled with a profit worth $2.1M USD.

  


 **Details of the Exploit**

The Yield Robot contract on the Binance Smart Chain was drained of $2.1 million on January 17th, 2023. The project team initially announced it was exploited, but further investigation shows evidence of an exit scam. The incident was possible due to a change in the signer wallet, which allowed the attacker to redeem a coupon that would otherwise have been rejected. The attacker used the coupon system to claim a coupon worth $2.1 million and then transferred the reward balance to their wallet. The Yield Robot deployer later used the wallet to create an unverified contract, which was likely a copy of the original contract, but with the deposit address changed to the attacker's wallet. New deposits were made, but later reverted back to the original deposit wallet.

  


 **Block Data Reference**

Set signer TX:

https://bscscan.com/tx/0x31bf8f7f5ac1664ba1b45985f4070c7358e57db3f7ca26f058910b4c2f156cab

  


Rug TX:

https://bscscan.com/tx/0xb66c4003aa9861222a69ec63f21c076e20678803ad065856ced0c26f670995ed

  


Scammer address:

https://bscscan.com/address/0x8f2dba873c24498f4a82f990ab04cb5aa5654a4a


Proof Links:
- [https://twitter.com/CertiKAlert/status/1617534035806355456](https://twitter.com/CertiKAlert/status/1617534035806355456)
- [ https://www.certik.com/resources/blog/6BoyRgbftDuzAIAXBFrCLb-yield-robot-exit-scam]( https://www.certik.com/resources/blog/6BoyRgbftDuzAIAXBFrCLb-yield-robot-exit-scam)


