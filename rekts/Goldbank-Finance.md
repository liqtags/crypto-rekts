# Goldbank Finance
![Goldbank Finance](/rektimages/Goldbank-Finance.png)
- Amount Lost: $75,239.00
- Funds Returned: $0.00
- Category: Token
- Date: 2023-6-11

**Quick Summary**

Goldbank Finance was exploited in an exit scam, with liquidity and token drain amounting to 75,239 $USD.

  


 **Details of the Exploit**

Goldbank Finance (GB) is a token trading on SushiSwap on the Arbitrum chain. The deployer removed liquidity from the pool, acquiring 27,414 $USD and 884,557 $GB. Another EOA address, suspected to be owned by the same deployer, altered the implementation of the UniTroller contract, sending 49,000,000 $GB tokens to the deployer. Consequently, the deployer drained a substantial amount of liquidity from the SushiSwap pool in a single transaction, receiving 47,825 $USD. The stolen amount was then moved through multiple addresses post-incident, resulting in a total loss of approximately 75,239 $USD.

  


 **Block Data Reference**

Deployer Address:

https://arbiscan.io/address/0xe5df114758a9beb76050754e35766191c0976a6a

  


Unitroller Admin Address:

https://arbiscan.io/address/0x946c72b432f1d0c35d9b2c9454905cb84cc0d188

  


Liquidity Removal Transaction:

https://arbiscan.io/tx/0xdaac092ff1d1d2c89ad97673c8ccab9c8bad16691c59b42df56a56d1369f8694

  


Liquidity Drain Transaction:

https://arbiscan.io/tx/0xfbd863d39f85d8a84326b14c00f4fc09302b6ad5e2a0e4cb39b34802dc56b492

  


Unitroller Malicious Implementation:

https://arbiscan.io/address/0xfa8221438b5dC055dA5F7EC9fC87132edd2835ae

  


Unitroller Address:

https://arbiscan.io/address/0x537A09Fd99Fc7eF737d297cDEeAB3b7f9602308c

  


Tokens Transfer Transaction:

https://arbiscan.io/tx/0xdd12c8ef4acb6233eb4a7625f473c0a41c15633712f497cd831952d6c3d623eb


Proof Links:
- [https://twitter.com/DeDotFiSecurity/status/1668274500775936004?s=20](https://twitter.com/DeDotFiSecurity/status/1668274500775936004?s=20)


