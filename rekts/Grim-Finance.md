# Grim Finance
![Grim Finance](/rektimages/Grim-Finance.png)
- Amount Lost: $40,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-19

**Quick Summary**

Grim Finance's GrimBoostVault was exploited due to a reentrancy bug, allowing the attacker to mint large amounts of GB tokens and withdraw more SPIRIT-LP tokens than they deposited.

  


 **Details of the Exploit**

The attacker initiated the exploit by taking a flash loan from the Balancer vault in WBTC and WFTM tokens. They then added liquidity on SpiritSwap and minted LP tokens. The attacker exploited a reentrancy bug in the depositor () function in GrimBoostVault, using a malicious contract as the token parameter. This allowed them to mint a large amount of GB tokens and withdraw more SPIRIT-LP tokens than they deposited. The attacker then removed liquidity, gaining more XXX and YYY tokens, and repaid the flash loan. The stolen funds were then bridged to Polygon, BSC, and Ethereum.

  


 **Block Data Reference**

The attacker's address:

https://ftmscan.com/address/0xdefc385d7038f391eb0063c2f7c238cfb55b206c

  


The transaction behind the attack:

https://ftmscan.com/tx/0x19315e5b150d0a83e797203bb9c957ec1fa8a6f404f4f761d970cb29a74a5dd6

  


Affected vault:

https://ftmscan.com/address/0x660184ce8af80e0b1e5a1172a16168b15f4136bf#code

  


The attacker's addresses on other chains:

https://etherscan.io/address/0xdefc385d7038f391eb0063c2f7c238cfb55b206c

https://polygonscan.com/address/0xdefc385d7038f391eb0063c2f7c238cfb55b206c

https://bscscan.com/address/0xdefc385d7038f391eb0063c2f7c238cfb55b206c


Proof Links:
- [https://twitter.com/financegrim/status/1472357770846519312](https://twitter.com/financegrim/status/1472357770846519312)
- [ https://twitter.com/k3mmio/status/1472315936166219777]( https://twitter.com/k3mmio/status/1472315936166219777)
- [ https://twitter.com/peckshield/status/1472328354942849024]( https://twitter.com/peckshield/status/1472328354942849024)


