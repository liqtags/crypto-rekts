# Starstream / Agora
![Starstream / Agora](/rektimages/Starstream---Agora.png)
- Amount Lost: $15,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-4-7

**Quick Summary**

The Starstream project was exploited on 532M $STARS tokens, which were then placed on Agora DeFi, where assets including $METIS, $WETH and $MUSDC were borrowed. Total losses amounted to ~$15M.

  


 **Details of the Exploit**

Starstream is a suite of products for providing yield aggregation and yield generation on the Metis L2 rollup.

The attacker used the external function _execute()_ , the Distributortreasury contract, which allowed sending $STARS tokens to the attacker's address. The attacker then deposited the stolen $STARS tokens in Agora DeFi loan contracts and leveraged assets, including $METIS, $WETH, and $MUSDC. The attacker used an Exchange Proxy to move the funds to the Ethereum blockchain before sending funds to Tornado.cash. In total the attacker sent 900 $ETH to Tornado.cash. The attacker then returned 120 $ETH back to METIS network via the Metis Andromeda Bridge.

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Attacker addresses:

ETH: https://etherscan.io/address/0xffd90c77eaba8c9f24580a2e0088c0c940ac9c48

METIS: https://andromeda-explorer.metis.io/address/0xFFD90C77eaBa8c9F24580a2E0088C0C940ac9C48/transactions

  


0x Exchange proxy transaction: https://etherscan.io/tx/0xd72b46cf015e43df4be3d1daa1685fa2ec7158dcfd121f57b6dc2279a358858d

  


Tornado.cash deposit example transactions:

https://etherscan.io/tx/0x4f112e1077ec4199b1f73420f3573d6f07b095cb9fa53e4d951cc3a04f28125d

https://etherscan.io/tx/0x80a3aad3b5a10317fec1d3e3d0ededb6095e50843a8ebe961461724167bf15d0

 https://etherscan.io/tx/0x596cdfe19961b50975b0aac8776be65d5cb92fca6ef31d9bee541acf1226aca6


Proof Links:
- [https://www.certik.com/resources/blog/2y4vFvoFyzSHTwvQdiwHgm-starstream-algora-incident](https://www.certik.com/resources/blog/2y4vFvoFyzSHTwvQdiwHgm-starstream-algora-incident)
- [ https://agora-defi.notion.site/Starstream-Hack-and-Agora-Exploit-Post-Mortem-6eee291ee01f40ab979c1a59d6a1bee4]( https://agora-defi.notion.site/Starstream-Hack-and-Agora-Exploit-Post-Mortem-6eee291ee01f40ab979c1a59d6a1bee4)


