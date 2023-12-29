# THORChain
![THORChain](/rektimages/THORChain.png)
- Amount Lost: $4,364,612.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-7-15

THORChain Exploiter 1 Address: https://etherscan.io/address/0x4b713980d60b4994e0aa298a66805ec0d35ebc5a  
  
THORChain Exploiter 2 Wallet: https://etherscan.io/address/0x3a196410a0f5facd08fd7880a4b8551cd085c031  
  
Contract attacker address:  
https://etherscan.io/address/0x4a33862042d004d3fc45e284e1aafa05b48e3c9c  
  
According to ThorChain’s preliminary incident report, the bug was located within the ETH Bifrost (bridge) code:  
https://gitlab.com/thorchain/thornode/-/blob/develop/bifrost/pkg/chainclients/ethereum/ethereum_block_scanner.go#L794  
  


The code contains an over-ride loop, designed only for use in _vaultTransferEvent_ transactions, which the hacker was able to manipulate. The hacker was able to wrap the router with their own contract, allowing them to access this over-ride.  
  
The attacker drained liquidity in various coins:

\- 2,500 ETH

\- 57,975.33 SUSHI

\- 8.7365 YFI

\- 171,912.96 DODO

\- 514.519 ALCX

\- 1,167,216.739 KYL

\- 13.30 AAVE  
  
Ether were sent to the external address:  
https://etherscan.io/address/0xace2d948fc7ea3bc49eee5526786d66d19bc470e 


Proof Links:
- [https://thearchitect.notion.site/THORChain-Incident-07-15-7d205f91924e44a5b6499b6df5f6c210](https://thearchitect.notion.site/THORChain-Incident-07-15-7d205f91924e44a5b6499b6df5f6c210)
- [ https://www.rekt.news/thorchain-rekt/]( https://www.rekt.news/thorchain-rekt/)


