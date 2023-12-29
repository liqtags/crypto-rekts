# SashimiSwap
![SashimiSwap](/rektimages/SashimiSwap.png)
- Amount Lost: $316,800.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-12-30

The attacker's address:  
https://etherscan.io/address/0xa8189407a37001260975b9da61a81c3bd9f55908  
  
The transactions behind the attack :  
https://etherscan.io/tx/0x713c2ce2cb424eb746083c25b7e48c368bb64f587c2d77b5c474a307a79bf069  
https://bscscan.com/tx/0xdf719d2535be32e302c1670a7453bdf648101a43b412e44d9e7e3e3754cc3387  
https://hecoinfo.com/tx/0xecde0b3821a8d250810db91d7ef82acced1eaf28324807bdbdfd755537366438  
  
The attacker used a bug in the calculations that are different from Uniswap. Due to fact that all tokens sit in one contract, he escalated it by:  
\- adding two fake tokens  
\- adding liquidity between both tokens and WETH/fake token  
\- swapping between UNI/WETH/fake tokens  
\- removing liquidity  
  
Total funds were stolen:  
\- 80 ETH (Ethereum)  
\- 10,000 DAI (Ethereum)  
\- 45,000 USDT (HECO)  
  
Stolen funds were deposited into Tornado Cash mixer:  
https://bloxy.info/txs/calls_from/0xa8189407a37001260975b9da61a81c3bd9f55908?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://sashimisashimi5.medium.com/statement-on-hackers-attack-322ab6a5c31d](https://sashimisashimi5.medium.com/statement-on-hackers-attack-322ab6a5c31d)
- [ https://twitter.com/BlockSecTeam/status/1476516736422019082]( https://twitter.com/BlockSecTeam/status/1476516736422019082)


