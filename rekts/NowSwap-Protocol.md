# NowSwap Protocol
![NowSwap Protocol](/rektimages/NowSwap-Protocol.png)
- Amount Lost: $1,142,357.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-9-15

The attacker's address:  
https://etherscan.io/address/0x5676e585bf16387bc159fd4f82416434cda5f1a3  
  
The transaction behind the exploit:  
https://etherscan.io/tx/0xf3158a7ea59586c5570f5532c22e2582ee9adba2408eabe61622595197c50713  
  
NowSwap hack was made possible by an error when updating the smart contract’s code.  The original code of the contract contained a value, K, of 1,000 in three different places.  The update to the code changed this value in two places but not the third.  
  
This third location was a check of the value of K, but it only checked for a value 1/10 of the actual value.  This enabled the attacker to swap 1 wei for 98% of the value stored in the contract.  
  
Stolen funds were deposited into Tornado Cash mixer:  
https://bloxy.info/txs/calls_from/0x5676e585bf16387bc159fd4f82416434cda5f1a3?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://twitter.com/nowswap_org/status/1438329668042584069](https://twitter.com/nowswap_org/status/1438329668042584069)
- [ https://halborn.com/explained-the-nowswap-protocol-hack-september-2021/]( https://halborn.com/explained-the-nowswap-protocol-hack-september-2021/)
- [ https://twitter.com/PuPuThrashing/status/1438058002817323009]( https://twitter.com/PuPuThrashing/status/1438058002817323009)


