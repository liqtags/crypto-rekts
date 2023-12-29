# SynLev
![SynLev](/rektimages/SynLev.png)
- Amount Lost: $277,897.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-3-13

The _removeLiquidity_ () function makes a call of the external function _getSharePrice_ () in vaultHelper contract:  
https://etherscan.io/address/0xe0d6b68403d32dd659e452db880393df15fa00f2#code  
  
vaultHelper is a proxy contract with EOA owner - 0xa2e316cbfa81640ce509ab487867a136b75c83c4  
  
The owner could set any address as price aggregator in vaultHelper calling _proposeVaultPriceAggregator_ ()  
  
A new aggregator (unverified contract) was provided in the transaction:  
https://etherscan.io/tx/0xc888619c64524f8b682952a0feb6c92ad73d7c90f9660aa3de9caad1467107a6  
  
This hidden aggregator set the share price to 0.  
  
After this, the contract deployer easily withdrew all vault balance with zero share price which can be found in the event log: https://etherscan.io/tx/0x216db3cacda35f01035d3d081935859c9ad71a8f5fa11edddcef785c721f0951#eventlog  
  
The contract deployer added liquidity into the contracts multiple times:  
https://bloxy.info/txs/references_address/0xa2e316cbfa81640ce509ab487867a136b75c83c4?argument=account&signature_id=1315743  
https://bloxy.info/txs/calls_from/0xa2e316cbfa81640ce509ab487867a136b75c83c4?signature_id=1315634&smart_contract_address_bin=0xff40827ee1c4eb6052044101e1c6e28dbe1440e3  
  
The contract deployer invoked the _removeLiquidity_ () function into the vault contract to withdraw 541.27 and 20.41 ETH onto his wallet at:  
https://etherscan.io/tx/0x216db3cacda35f01035d3d081935859c9ad71a8f5fa11edddcef785c721f0951  
https://etherscan.io/tx/0x5131d9996790863c9ec9c3d035abd8c6e0692f0c8acf87a51bb40c664f97fce4  
  
The contract deployer invoked the _ethremove_ () function into the synSales contract to withdraw 152.09 ETH onto his wallet at:  
https://etherscan.io/tx/0xec4ba66c551375041a541e42870955b3d1a33b73ecd95dac38d3bfaf01e1602d  
  
The contract deployer invoked the _removeLiquidity_ () function into the other vault contract to withdraw 104.41 ETH onto his wallet at:  
https://etherscan.io/tx/0x6afe1ec90254accfe7aa2edf6c6df8e258f578413abd9936cbe8a97347509d8d  
  
The contract deployer invoked the _removeLiquidity_ () function into the other vault contract to withdraw 10.59 ETH onto his wallet at:  
https://etherscan.io/tx/0x5c7644f772021efaa974cb06caa66bbdd7ef687080a409d0fb72132935764e51  
  
The contract deployer invoked the _removeLiquidity_ () function into the other vault contract to withdraw 24.26 ETH onto his wallet at:  
https://etherscan.io/tx/0xe4c8cc92d987d7501bfc5e406b337834f88cd2c5d95dc1aca52b535423800397


Proof Links:
- [https://www.cryptonary.com/synlev-price-crashes-by-over-80-in-24-hours-as-developers-left/ https://twitter.com/jurad0x/status/1370656949927223300](https://www.cryptonary.com/synlev-price-crashes-by-over-80-in-24-hours-as-developers-left/ https://twitter.com/jurad0x/status/1370656949927223300)


