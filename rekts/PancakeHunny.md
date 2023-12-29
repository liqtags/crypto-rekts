# PancakeHunny
![PancakeHunny](/rektimages/PancakeHunny.png)
- Amount Lost: $112,187.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-6-3

The attacker's address:  
https://bscscan.com/address/0x0ef50be29c82ecf2158ec1886dc6692a2b0db411  
  
The attacker:  
\- WBNB was swapped to CAKE at PancakeSwap

\- sent CAKE to the HUNNY Minter contract

\- staked on CAKE-BNB Hive in PancakeHunny

\- HUNNY Minter was “tricked” to mint more HUNNY tokens, namely:  
using all the wallet balance to make HUNNYBNB LP, and then uses it to calculate the profit hunnyBnbAmount, which can be easily tampered with by just sending the tokens to the minter contract  
  
\- the attacker then un-staked from CAKE-BNB Hive to receive the HUNNY tokens from the Minter  
  
\- the attacker then sold the HUNNY tokens on PancakeSwap  
  
Stolen funds were transferred to the external address and deposited to the Binance exchange wallet at:  
https://bscscan.com/tx/0xcc88d376224077f60ff7bcce62c6f077f14d0679d5fdd5bfde5934070a1b8324  
https://bscscan.com/tx/0xba23b86d685aa04e8bb949fd5dc56710e68660f277364e27e2e113ffae62a215  
https://bscscan.com/tx/0x4c93ae86c739cf76b7505846fb9c108d8852ccab94b26433f18f4fda5279dac8  
https://bscscan.com/tx/0xe8f8d0e388bc099a9ccee842759c4fdb2cac2ea3142c28d29e65407678dc3fab


Proof Links:
- [https://medium.com/pancakehunny/pancakehunny-preliminary-incident-report-6da18bc3c0e6](https://medium.com/pancakehunny/pancakehunny-preliminary-incident-report-6da18bc3c0e6)
- [ https://medium.com/pancakehunny/pancakehunny-post-mortem-analysis-de78967401d8]( https://medium.com/pancakehunny/pancakehunny-post-mortem-analysis-de78967401d8)
- [ https://watchpug.medium.com/pancakehunny-performance-fee-minting-attack-analysis-e347d12bfdde]( https://watchpug.medium.com/pancakehunny-performance-fee-minting-attack-analysis-e347d12bfdde)


