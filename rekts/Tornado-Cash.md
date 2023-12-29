# Tornado Cash
![Tornado Cash](/rektimages/Tornado-Cash.png)
- Amount Lost: $1,049,513.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-5-20

**Quick Summary**

Tornado Cash Governance was exploited through a malicious proposal, and the attacker gained control of the governance.

  


 **Details of the Exploit**

Tornado Cash is a service that provides non-custodial anonymous transactions on EVM chains. The project's Governance was exploited via malicious proposal. On May 20th, 2023 Tornado Cash governance ceased to exist as an attacker granted themselves over 1.2 million fake votes through a malicious proposal. With full control of governance, they could withdraw all locked votes and drain tokens from the contract or brick the router. The attack was sophisticatedly designed by using various tricks like combining CREATE/CREATE2 to create a contract with different bytecode and hiding intent behind emergencyStop() named function while updating proposal logic to grant themselves fake votes. Once gaining control, the attacker drained various contracts and users staking assets as $TRON tokens. The stolen tokens were swapped for $ETH and 360 $ETH was transferred through TornadoCash, while 120.4 $ETH remains at the attacker's address along with 177,340 $USD worth $TORN tokens. Consequently, over 500,000 $TORN tokens were used by the attacker to propose the 21st proposal, which seemingly may return the protocol control back to the users. The total stolen amount reached 1,049,513 $USD, and maybe even more cause of locked $TORN tokens in the next proposal from the attacker. 

  


 **Block Data Reference**

Attacker's Funds Holder Address:

https://etherscan.io/address/0x092123663804f8801b9b086b03B98D706f77bD59

  


Malicious Proposal Executor Address:

https://etherscan.io/address/0x592340957eBC9e4Afb0E9Af221d06fDDDF789de9

  


Proposal Execution Transaction:

https://etherscan.io/tx/0x3274b6090685b842aca80b304a4dcee0f61ef8b6afee10b7c7533c32fb75486d

  


Selfdestruct Transaction:

https://etherscan.io/tx/0xd3a570af795405e141988c48527a595434665089117473bc0389e83091391adb

  


Vote Gain Transaction:

https://etherscan.io/tx/0xa7d20ccdbc2365578a106093e82cc9f6ec5d03043bb6a00114c0ad5d03620122

  


Malicious Proposal:

https://etherscan.io/address/0xC503893b3e3c0C6b909222b45f2a3a259a52752D

  


21st Proposal:

https://etherscan.io/address/0x1FAd009aD35689B5a9B91486148F2F32AFE31e23#code


Proof Links:
- [https://twitter.com/samczsun/status/1660012958787973121](https://twitter.com/samczsun/status/1660012958787973121)
- [ https://twitter.com/BlockSecTeam/status/1660214665429876740]( https://twitter.com/BlockSecTeam/status/1660214665429876740)


