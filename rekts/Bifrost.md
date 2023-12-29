# Bifrost
![Bifrost](/rektimages/Bifrost.png)
- Amount Lost: $2,248,328.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-7-8

**Quick Summary**

Bitcoin wallet Bifrost was attacked by hackers.  
During the attack, the key of the server issuing the address was revealed, and the attacker was able to self-sign his own deposit address. Since the attacker could generate a valid signature on the deposit address, the BiFi platform recognized the attacker's $BTC transfer as a $BTC deposit in Bifrost. As a result, the attacker was able to borrow 1,852 $ETH with fake deposit.

  


 **Details of the Exploit**

Bifrost is a web3 derivatives protocol that provides decentralized cross-chain liquidity for staked assets. During the attack, the server key of the address issuing server was revealed, which is why the attacker was able to independently sign his own deposit address. In this transaction, the attacker signs the address: https://etherscan.io/tx/0x1a507140573d10fed06a9052a58b46621a1fbfad2d4a54fd0f5db40e1788a29d

Since the attacker managed to generate a valid signature on the deposit address, BiFi recognized the attacker's $BTC transfer as a deposit, so attacker sends 321.7 $BTC as a "deposit": https://www.blockchain.com/btc/tx/dd0bf6ab976f2090dd48cf6223a50e3c6c8a616e5c28dfc9448f81f1b7e99346

The relayer detected the deposit and transmitted the verified deposit history to BiFi. Then the relayer minted $BiBTC as a $BTC collateral for the attacker.  
Transaction of deposit detection: https://etherscan.io/tx/0x5c0460f529a003d11911f21f8a8decb15aeaf07e9682a0d6e15aeb1cd5c39e69  
Transaction of deposit confirmation with minting $BiBTC: https://etherscan.io/tx/0x2e4422dd80350bd57cca6707a69473da20282c6b318c48a642e690e691a0c15f

The attacker then called the _borrow()_ function to take 1.8k $ETH:  
https://etherscan.io/tx/0x4b5d66871af64da0fd5ac448474235079ae0cb93db70366eed2808ca56dfcf76

which were subsequently withdrawn via Tornado.cash.

  


 **Block Data Reference**

Attacker address on ETH: https://etherscan.io/address/0x282971deD7D0B8C5b0358EbEbe3B2bC6A24a6b10

Attacker address on Bitcoin: https://www.blockchain.com/btc/address/bc1qmgh7w47myz7kt7x34zqlr5azck7u8j8ewg3u2j

Attacker public keyhash: 0xDa2fe757Db20Bd65F8D1a881F1D3a2C5BdC3c8F9


Proof Links:
- [https://bifrost.medium.com/post-mortem-bifi-btc-illegal-address-registration-c21ce3ba9fc8](https://bifrost.medium.com/post-mortem-bifi-btc-illegal-address-registration-c21ce3ba9fc8)


