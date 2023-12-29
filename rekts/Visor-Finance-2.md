# Visor Finance
![Visor Finance](/rektimages/Visor-Finance-2.png)
- Amount Lost: $972,616.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-11-26

The attacker's address 1:  
https://etherscan.io/address/0x89640eb6c8d72606d6a0fff45415bff0ab0e3ae1  
  
The attacker's address 2:  
https://etherscan.io/address/0xf434edf6b19e7310a7bea05ad3df6c086fd3a98e  
  
The transactions behind the flash loan attack (exploiter 1):  
https://etherscan.io/tx/0x5c9ac39ca05e51147d60156f085e650370a1e930f9f615f758fecb31deafb6ab  
https://etherscan.io/tx/0xc2104896231ed5ad66e880f046d9973a0b85e28d5534f3e7213bbb41e83f7316  
https://etherscan.io/tx/0x07f39ed1cb3c2e1426236344d3d35dd7d79ce6cddb3a9ed17885ae9eef099639  
https://etherscan.io/tx/0x2f49b4365b688211812ec9fd0c9ac3969a6a49b99d1df75edebd3adbed0d8f55  
https://etherscan.io/tx/0xca68269685524d3818c98cb588c00a215fcc8a15c739c0a4468e078b3f3f3a7a  
  
Stolen funds (91 ETH) were deposited into Tornado cash mixer at:  
https://bloxy.info/txs/calls_from/0x89640eb6c8d72606d6a0fff45415bff0ab0e3ae1?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967  
  
The transactions behind the flash loan attack (exploiter 2):  
https://etherscan.io/tx/0x4208ef772b9ecb7a0494510101525e765240568d3788bab555942d344b984f67  
https://etherscan.io/tx/0x6e5be7b85df2913ba8e807de9350d69969134d3f73391e620db267a9d0f8f461  
https://etherscan.io/tx/0x42c91595b1b1ec782f99069cd0c5a31fccdf2244c49b8493a2ddf70141ab5fb8  
  
Stolen funds (124 ETH) were deposited into Tornado cash mixer at:  
https://bloxy.info/txs/calls_from/0xf434edf6b19e7310a7bea05ad3df6c086fd3a98e?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967  
  
The exploit was executed according to the following scheme:  
  
1\. Take a flash loan of asset X.  
  
2\. Swap X for Y to pump the price of Y, dump the price of X.  
  
3\. Deposit Y into XY Visor Pool to get outsized shares based on the manipulated value of Y.  
  
4\. Withdraw shares to get the equal ratio of XY back from Visor.  
  
5\. Rebalance the pool, and pay back the flash loan.



