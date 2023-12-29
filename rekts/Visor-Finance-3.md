# Visor Finance
![Visor Finance](/rektimages/Visor-Finance-3.png)
- Amount Lost: $529,929.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-21

The attacker:  
https://etherscan.io/address/0x8efab89b497b887cdaa2fb08ff71e4b3827774b2  
  
The transaction behind the attack:  
https://etherscan.io/tx/0x69272d8c84d67d1da2f6425b339192fa472898dce936f24818fda415c1c1ff3f  
  
Exploited contract:  
https://etherscan.io/address/0xc9f27a50f82571c1c8423a42970613b8dbda14ef#code  
  
The problem:  
  
Deposit function calls delegatedTransferERC20 function on any contract from parameter "from" without any restrictions, this function call opens ability for reenter target contract. After calling delegatedTransferERC20 function deposit was called a second time. This lead to minting double share amount. In addition, there is no check for the "from" parameter, so the called contract can do nothing, and the function can be called with any value for visrDeposit parameter.  
  
Minted share tokens were withdrawn and exchanged for VISAR tokens. Then the attacker sold them in liquidity pair on Uniswap and deposited them into Tornado Cash mixer:  
https://etherscan.io/address/0x8efab89b497b887cdaa2fb08ff71e4b3827774b2#tokentxns  
  
https://bloxy.info/txs/calls_from/0x8efab89b497b887cdaa2fb08ff71e4b3827774b2?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://twitter.com/VisorFinance/status/1473306777131405314](https://twitter.com/VisorFinance/status/1473306777131405314)
- [ https://twitter.com/peckshield/status/1473315405498576901]( https://twitter.com/peckshield/status/1473315405498576901)
- [ https://twitter.com/BlockSecTeam/status/1473322134973730819]( https://twitter.com/BlockSecTeam/status/1473322134973730819)


