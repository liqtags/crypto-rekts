# Chibi Finance
![Chibi Finance](/rektimages/Chibi-Finance.png)
- Amount Lost: $1,052,646.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2023-6-27

**Quick Summary**

The Chibi Finance project on the Arbitrum network was hit by a rugpull, resulting in a loss of 1,052,646 $USD.

  


 **Details of the Exploit**

Chibi Finance is an Arbitrum-based yield farming protocol. On June 27, 2023, a malicious transaction with draining assets from three contracts took place. A scammer used a privileged function setSettings() to set a malicious contract as a Governance contract. They then withdrew funds from three smart contracts: StrategyAave, StrategySushiSwap, and StrategyGHA in a single transaction. Several assets were stolen, including 4.2 $WBTC, 256,012 $USDC, 94.6 $WETH, 115,049 $USDT, and SLP tokens as LP tokens for ARB/WETH pool. The stolen funds were valued at 1,052,646 $USD. All the funds were swapped for $WETH and then bridged using Multichain and Stargate. The project's website shut down and the Twitter account was deleted shortly after an incident.

  


 **Block Data Reference**

Scammer Address:

https://arbiscan.io/address/0x80c1ca8f002744a3b22ac5ba6ffc4dc0deda58e3

  


Deployer Address:

https://arbiscan.io/address/0xf0b6dcb0ddf0ae0648022bd9feb4a881d32acd25

  


Malicious Transaction:

https://arbiscan.io/tx/0x3cb65210b01a643cc34945f70e9109084c68a5ba595346ee48aef7607b85db95

  


Funds Bridging Transactions:

https://arbiscan.io/tx/0x5fad3397f1dd707b38478aabfe7af9abc390f16e12d7d4c0babb813993782707

https://arbiscan.io/tx/0xe7a9c8254a04d67677be50306df51b0cb851603c716f236d748cb3c93cd4f73c

  


Malicious Contract:

https://arbiscan.io/address/0xb61222189b240be3da072898eda7db58b00fd6ee


Proof Links:
- [https://twitter.com/peckshieldalert/status/1673615238758006786](https://twitter.com/peckshieldalert/status/1673615238758006786)


