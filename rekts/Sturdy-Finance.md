# Sturdy Finance
![Sturdy Finance](/rektimages/Sturdy-Finance.png)
- Amount Lost: $775,332.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2023-6-12

**Quick Summary**

Sturdy Finance, an Ethereum-based lending platform, fell victim to an oracle manipulation exploit, losing 775,332 $USD.

  


 **Details of the Exploit**

Sturdy Finance was exploited through an oracle price manipulation attack. In a read-only reentrancy attack, the perpetrator managed to exploit the SturdyOracle contract and manipulate its pricing. They executed a single withdrawal transaction from the 'Sturdy_eth interest bearing WETH' contract.

  


The total funds lost due to the exploit amounted to 880,850 $USD. However, the attacker's profit was 442 $ETH, equating to around 775,332 $USD, while the remaining funds served as the flashloan commission. The illicitly gained profits were later moved through TornadoCash in multiple transactions.

  


 **Block Data Reference**

Attacker Address:

https://etherscan.io/address/0x1E8419E724d51E87f78E222D935fbbdeb631a08B

  


Malicious Contract:

https://etherscan.io/address/0x0B09c86260C12294e3b967f0D523B4b2bcdFbeab

  


Malicious Transaction:

https://etherscan.io/tx/0xeb87ebc0a18aca7d2a9ffcabf61aa69c9e8d3c6efade9e2303f8857717fb9eb7

  


Example of Funds Transfer Transaction:

https://etherscan.io/tx/0x1702e647da897a35b59304bde5e62b4e6ad8d5148905b4627398bd30c42ee1a7


Proof Links:
- [https://twitter.com/peckshield/status/1668072853802037248](https://twitter.com/peckshield/status/1668072853802037248)
- [ https://twitter.com/SturdyFinance/status/1668080627030315009]( https://twitter.com/SturdyFinance/status/1668080627030315009)


