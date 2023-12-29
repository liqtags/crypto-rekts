# Ankr
![Ankr](/rektimages/Ankr.png)
- Amount Lost: $24,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-2

**Quick Summary**

Ankr protocol was exploited by private key compromisation. The attacker replaced contract implementation and was able to mint aBNBc tokens infinitely. 

  


 **Details of the Exploit**

Ankr is a decentralized infrastructure with a rich ecosystem. The staking contract of the protocol on the Binance Smart Chain was exploited using access control vulnerability. The attacker replaced the implementation for the staking proxy with an unverified malicious contract. Consequently, the malicious contract was used to mint 10,000,000,000,000 $aBNBc which were exchanged for 5,500 $BNB and 5,340,000 $USDC. $aBNBc token price dropped nearly 99% and almost all the liquidity was drained from PancakeSwap and ApeSwap pools. The stolen amount almost completely was transferred through TornadoCash, AnySwap, and CelerBridge. There is just 100 $BNB left in the attacker's original address at the moment.

At this moment proxy implementation was replaced with the new unverified one.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0xf3a465C9fA6663fF50794C698F600Faa4b05c777

  


Malicious transaction:

https://bscscan.com/tx/0x61e0f3f0dc5cc84f0547799ebb19515ce5f5d20c0b57442135263bcb1b506812

https://bscscan.com/tx/0xcbc5ff4a6c9a66274f9bde424777c3dc862ab576e282fbea3c9c2609ca3e282b

  



Proof Links:
- [https://twitter.com/BeosinAlert/status/1598514702849826817](https://twitter.com/BeosinAlert/status/1598514702849826817)
- [ https://twitter.com/CertiKAlert/status/1598547948958371841]( https://twitter.com/CertiKAlert/status/1598547948958371841)
- [ https://twitter.com/PeckShieldAlert/status/1598527823224111104]( https://twitter.com/PeckShieldAlert/status/1598527823224111104)


