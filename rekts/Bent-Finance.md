# Bent Finance
![Bent Finance](/rektimages/Bent-Finance.png)
- Amount Lost: $1,786,520.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-21

**Quick Summary**

Bent Finance became a victim to an insider's exploit. The exploiter extracted approx. $USD 1.75M in value from the project.  
  
 **Details of the Exploit**  
Bent Finance is a staking and farming platform that optimizes returns from the curve protocol.

The Bent Finance team was in the process of migrating its contracts to a multisig wallet hereby effectively addressing internal security issues. Only days before the migration a developer on the team hardcoded the maximum fees on the crv and mim pool contracts to 17%. The developer also introduced a malicious smart contract that enabled the deployer to hardcode users balances.  The exploiter proceeded to assign an enormous balance to his account, far exceeding the TVL of Bent Finance. Subsequently, the developer launched a new smart contract in order to cover his tracks. Through these mechanisms the dishonest deployer was pledged rewards in the billions by the smart contracts. 

All of the above mentioned proxy updates completely changed the functionality of the smart contracts and would not have been possible a couple of days later after the multisig migration would have concluded. The crooked deployer proceeded to withdraw 513k cvxcrv token and redirected them to a second address. With a third address, the deployer removed liquidity and transferred received theETH to the exploiter #2 address:  
https://etherscan.io/tx/0x0a91dfc9f752a921a4602961ed5bf7555205b21919f1f4aba37184320b1e2a25  
https://etherscan.io/tx/0x2bda5f873adb07ef4e98f0dcd736ed047a8b272178c5a4673489e03357963120

The second exploiter address washed the funds through Tornado.cash.

  


 **Block Data Reference**

The addresses, marked as the exploiters:  
#1: https://etherscan.io/address/0xd23cfffa066f81c7640e3f0dc8bb2958f7686d1f  
#2: https://etherscan.io/address/0x9e966a54082427d7ac56aeaee4baae7d11a6e468  
#3: https://etherscan.io/address/0x71b1ee098dbe801ce7d42a4bdb472ed164f1c21a

Bent Finance Crv Fi contract:

https://etherscan.io/address/0x270b6aff561284ef380cdd6d8b036f4981049a86

Transaction of 263k cvxcrv from exploiter address 1 to exploiter address 2:

https://etherscan.io/tx/0x11961c4df0b27bd7188d451dd18005dc8aff7ad4a80c7f7441b56495cae219c5

Transaction of 250k cvxcrv from exploiter address 1 to exploiter address 2:

https://etherscan.io/tx/0x52d4d5a9a83ff8ca6a7fd102954c4c5d2658043d9049abfc47cd8c37692b95be

Tornado.cash transactions:

https://etherscan.io/address/0x9e966a54082427d7ac56aeaee4baae7d11a6e468

Call _updateVersion()_ of Bent cvxCRV token through ProxyAdmin at:  
https://etherscan.io/tx/0xf711641ea9814d78780c8a51ad734ad44d58baf3f97256a3f5ec3200a29eadc7

Call _updateVersion_ () of Bent MIM token, executing the backdoored line at:  
https://etherscan.io/tx/0xd5e0d4ab279f6a0f8635307869471d7934cffa4086ec93d26e9e9c6a98ae9fef

Bent Finance deployer upgrades the implementation of Bent cvxCRV token through ProxyAdmin at:  
https://etherscan.io/tx/0xb37ffd779c26d1bf3105719662136af34090050abd962ab59e24d81cc7f63a07


Proof Links:
- [https://rekt.news/bent-finance/](https://rekt.news/bent-finance/)
- [ https://twitter.com/BlockSecTeam/status/1473188863136780288]( https://twitter.com/BlockSecTeam/status/1473188863136780288)


