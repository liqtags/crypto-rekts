# Pickle Finance
![Pickle Finance](/rektimages/Pickle-Finance.png)
- Amount Lost: $19,700,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2020-11-21

**Quick Summary**

An attacker exploited Pickle Finance's ControllerV4 by deploying malicious smart contracts, leading to a loss of 19M DAI.

 **  
**

 **Details of the Exploit**

The attacker deployed two smart contracts with malicious logic, which were used to retrieve the amount available to withdraw from StrategyCmpdDaiV2. The ControllerV4.swapExactJarForJar() function was invoked, which doesn't check the Jars and calls them, withdrawing from StrategyCmpDAIV2. This transferred 19M DAI to pDAI. The attacker then called pDAI.earn() three times, leading to a Compound deposit and the contract receiving cDAI. Three more smart contracts with malicious logic were deployed and the ControllerV4.swapExactJarForJar() function was invoked again, leading to the withdrawal of cDAI and transferring them to ControllerV4. The funds were then transferred to the attacker's smart contract, which redeemed cDAI for DAI from Compound and transferred DAI to the attacker's EOA.

 **  
**

 **Block Data Reference**

  


The attacker's address:

https://etherscan.io/address/0x75aa95508f019997aeee7b721180c80085abe0f9

https://etherscan.io/address/0x02c8364546ec849e1726fb6cae5228702b111ee6

  


The transaction behind the attack:

https://etherscan.io/tx/0xe72d4e7ba9b5af0cf2a8cfb1e30fd9f388df0ab3da79790be842bfbed11087b0


Proof Links:
- [https://github.com/banteg/evil-jar/blob/master/readme.md](https://github.com/banteg/evil-jar/blob/master/readme.md)
- [ https://rekt.news/pickle-finance-rekt/]( https://rekt.news/pickle-finance-rekt/)
- [ https://www.coindesk.com/defi-protocol-pickle-finance-token-loses-almost-half-its-value-after-19-7m-hack]( https://www.coindesk.com/defi-protocol-pickle-finance-token-loses-almost-half-its-value-after-19-7m-hack)


