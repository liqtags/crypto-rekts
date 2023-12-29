# Earning Farm
![Earning Farm](/rektimages/Earning-Farm.png)
- Amount Lost: $1,365,750.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-10-14

**Quick Summary**

Earning Farm was exploited via Flash Loan Attack resulted in a loss of 1,365,750 $USD worth of $ETH

  


 **Details of the Exploit**

Earning Farm is a Yield Aggregator running on the Ethereum chain. The project suffered from a Flash Loan Attack and lost roughly 750 $ETH in total. The attacker was able to receive 268 $ETH while the rest of the stolen funds were siphoned by MEV Bot. The attacker deployed a malicious smart contract with unverified source code, and exploited EFLeverVault contract's logic issue. Security check for a callback initiator was missing in the affected contract, which allowed the attacker to drain the vault contract's $ETH. All the stolen funds were transferred through TornadoCash.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0xdf31f4c8dc9548eb4c416af26dc396a25fde4d5f

  


Malicious transaction:

https://etherscan.io/tx/0x160c5950a01b88953648ba90ec0a29b0c5383e055d35a7835d905c53a3dda01e

  


Malicious contract:

https://etherscan.io/address/0x140cca423081ed0366765f18fc9f5ed299699388


Proof Links:
- [https://u.today/earningfarm-yield-platform-under-attack-details](https://u.today/earningfarm-yield-platform-under-attack-details)
- [ https://twitter.com/danielvf/status/1580936010556661761]( https://twitter.com/danielvf/status/1580936010556661761)
- [ https://twitter.com/Supremacy_CA/status/1581012823701786624]( https://twitter.com/Supremacy_CA/status/1581012823701786624)


