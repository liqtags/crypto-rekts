# Platypus Finance
![Platypus Finance](/rektimages/Platypus-Finance.png)
- Amount Lost: $8,500,887.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-2-16

**Quick Summary**

Platypus Finance protocol was exploited via flash loan attack for 8,500,887 $USD. The attacker managed to bridge the part of the stolen amount.

  


 **Details of the Exploit**

Platypus Finance is an AMM that provides stableswap opportunities. The attacker exploited multiple asset contracts of the protocol, using a malicious smart contract with unverified source code. 8,500,887 $USD worth of assets in stablecoins such as nearly 4,400,000 $USDC, 2,700,000 $USDT, 687,000 $BUSD, and 691,000 $DAI were stolen. The attacker used the USP solvency check mechanism's weakness and took 44,000,000 $USDC as a flash loan and performed malicious actions. This amount was used to swap for 44,000,000 Platypus LP-USD, and then to mint 41,700,000 $USP tokens for free. The $USP tokens then were swapped for various stablecoins. It's said on the project's official Twitter that they are working with third parties such as Binance, Tether, and Circle to freeze the funds, and at the moment, $USDT was frozen. The malicious actor managed to bridge 2,403,165 $USDC through Gnosis Proxy.

  


 **Block Data Reference**

Malicious transaction:

https://snowtrace.io/tx/0x1266a937c2ccd970e5d7929021eed3ec593a95c68a99b4920c2efa226679b430

  


Attacker's address:

https://snowtrace.io/address/0xeff003d64046a6f521ba31f39405cb720e953958

  


Malicious contract:

https://snowtrace.io/address/0x67afdd6489d40a01dae65f709367e1b1d18a5322

  


Transfer transactions:

https://snowtrace.io/tx/0x5e3eb070c772631d599367521b886793e13cf0bc150bd588357c589395d2d5c3

https://snowtrace.io/tx/0x76ceab91aef320d0556029861dc1dde423d100e2a85f7ca4891a924efce4ed5a


Proof Links:
- [https://cryptoslate.com/platypus-finance-hacked-for-9m-on-avalanche/](https://cryptoslate.com/platypus-finance-hacked-for-9m-on-avalanche/)
- [ https://twitter.com/Platypusdefi/status/1626396538611310592]( https://twitter.com/Platypusdefi/status/1626396538611310592)


