# Punk Protocol
![Punk Protocol](/rektimages/Punk-Protocol.png)
- Amount Lost: $8,900,000.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2021-8-10

**Quick Summary**

Punk Protocol suffered a loss due to a missing Modifier in the initialize() function of the CompoundModel code, allowing an attacker to manipulate the function and withdraw assets directly to their wallet.

  


 **Details of the Exploit**

The attacker exploited a vulnerability in the initialize() function of the CompoundModel code, which lacked an "initializer" Modifier. This allowed the attacker to manipulate the function, despite it being connected to an unknown contract. The attacker then updated the contract address and called withdrawToForge(), sending the assets controlled by the CompoundModel directly to their malicious contract and into their wallet. The stolen funds were then swapped on ETH and deposited into the Tornado Cash mixer. A white-hat hacker managed to front run the attack and returned $5 million to the Punk Protocol deployer's address.

  


 **Block Data Reference**

  


The attacker's address:

https://etherscan.io/address/0x1d5a56402425c1099497c1ad715a6b56aaccb72b

  


The attacker's smart contract:

https://etherscan.io/address/0x1695ce70da4521cb94dea036e6ebcf1e8a073ee6

  


The white-hat hacker address:

https://etherscan.io/address/0x3aa27ab297a3a753f79c5497569ba2dacc2bc35a

  


white-hat hacker smart contract:

https://etherscan.io/address/0x00000000b2ff98680adaf8a3e382176bbfc34c8f

  


Transaction of the attack:

https://etherscan.io/txs?a=0x1d5a56402425c1099497c1ad715a6b56aaccb72b

  


Transaction of the returned funds:

https://etherscan.io/tx/0x008dd92f8bcfcee400aed26d13495fbfc8351f9b21289792fc2bb9e771668147

https://etherscan.io/tx/0xace7c07695ec1bbf917486c3c81ee7de79c04e0309d4f6a149688463e6f83247


Proof Links:
- [https://medium.com/punkprotocol/punk-finance-fair-launch-incident-report-984d9e340eb?source=social.tw&_branch_match_id=948322436900511955](https://medium.com/punkprotocol/punk-finance-fair-launch-incident-report-984d9e340eb?source=social.tw&_branch_match_id=948322436900511955)
- [ https://rekt.news/punkprotocol-rekt/]( https://rekt.news/punkprotocol-rekt/)


