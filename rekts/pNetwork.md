# pNetwork
![pNetwork](/rektimages/pNetwork.png)
- Amount Lost: $12,700,000.00
- Funds Returned: $0.00
- Category: Bridge
- Date: 2021-9-19

**Quick Summary**

pBTC-on-BSC cross-chain bridge was exploited, resulting in the theft of 277 BTC.

  


 **Details of the Exploit**

The attacker targeted multiple pTokens bridges, but only the pBTC-on-BSC cross-chain bridge was affected. The attacker was funded with BNB from a Binance exchange wallet to cover gas fees for the deployment of contracts with malicious logic. These smart contracts created a series of event logs, including both legitimate and faulty peg-out requests. Due to a bug in the Rust code section responsible for extracting these log events, both types of logs were extracted and incorrectly processed, leading to the exploit. As a result, 277 BTC were stolen from the pBTC-on-BSC collateral.

  


 **Block Data Reference**

Attacker Address:

https://bscscan.com/address/0x2bf5693dd3a5cea1139c4510fdce120cf042c934

  


First Exploit Transaction:

https://bscscan.com/tx/0x0eb55e02bce39ec1d2d2e911eca7dcca54e74841b53412c078185e43c5a2a551

  


Funding Transaction from Binance:

https://bscscan.com/tx/0x23db0ee27e10517dea0659a743fd6df92d482ad6796851c71127e5049e7bbd88

  


BTC Addresses of the Attacker:

https://pastebin.com/raw/bAquZVws


Proof Links:
- [https://medium.com/pnetwork/pnetwork-post-mortem-pbtc-on-bsc-exploit-170890c58d5f](https://medium.com/pnetwork/pnetwork-post-mortem-pbtc-on-bsc-exploit-170890c58d5f)
- [ https://finance.yahoo.com/finance/news/bitcoin-hack-pnetwork-cryptocurrency-latest-110155143.html]( https://finance.yahoo.com/finance/news/bitcoin-hack-pnetwork-cryptocurrency-latest-110155143.html)
- [ https://cointelegraph.com/news/latest-defi-hack-targeting-bsc-sees-12-7m-in-bitcoin-stolen-from-pnetwork]( https://cointelegraph.com/news/latest-defi-hack-targeting-bsc-sees-12-7m-in-bitcoin-stolen-from-pnetwork)


