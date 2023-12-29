# Deri Protocol
![Deri Protocol](/rektimages/Deri-Protocol.png)
- Amount Lost: $144,532.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-10-28

**Quick Summary**

Deri Protocol's trading pool on Arbitrum was exploited resulting in a loss of 143,532 $USD.

  


 **Details of the Exploit**

On October 28th, 2022, an attack took place on Deri Protocol’s trading pool on Arbitrum. The attacker used two associated accounts to execute the exploit. The attacker added margin to these two accounts and gradually established large opposite positions for option BTCUSD-40000-C for both accounts by trading relatively small volumes for each turn. Due to the low margin requirement for far OTM options on Deri Protocol, the attacker repeated this process hundreds of times until they opened a huge long position for account A (notional=100,192 BTC) and a huge short position for account B (notional=-96,940 BTC). With everlasting options’ funding mechanism, Account A continuously paid funding fees to B which pushed up the positive net volume causing higher funding rates making it likely that Account A would get liquidated unless BTC price kept going up. At UTC time 10/28/2022 17:51 when BTC price went down and brought Account A under maintenance margin it got liquidated causing massive sell notional=100,192.4024 $BTC which dragged mark price below zero leading to a loss of around $144k USD but only lost original balance as opposed to full loss due bound by margin balance.

Immediately after liquidation of A; the attacker closed out short position in B resulting in large profits for 144,532 $USDC.

The pool ended up with a net loss since although theoretically B’s profit came from A’s loss but since losses were bound by margin balances and could not be fully realized thus resulted in negative PnL.

  


 **Block Data Reference**

Attacker addresses:

https://arbiscan.io/address/0x09ca80536f5aa6f04a8170D44aAf9fdfDD1e228d

https://arbiscan.io/address/0x2443506117e03136727E394F85B5b0797A3E0477_

  


Malicious Transaction:

https://arbiscan.io/tx/0xc31ade492c134388fef8fdd7669c9bb195c1426697c418d27d45ce9a837bc93d


Proof Links:
- [https://deri-protocol.medium.com/the-detailed-process-of-the-2022-10-28-attack-on-deri-protocol-7eb5c2f3900e](https://deri-protocol.medium.com/the-detailed-process-of-the-2022-10-28-attack-on-deri-protocol-7eb5c2f3900e)
- [ https://twitter.com/DeriProtocol/status/1586678284477026304]( https://twitter.com/DeriProtocol/status/1586678284477026304)


