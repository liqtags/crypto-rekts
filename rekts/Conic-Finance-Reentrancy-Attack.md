# Conic Finance
![Conic Finance](/rektimages/Conic-Finance-Reentrancy-Attack.png)
- Amount Lost: $3,254,850.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-7-21

**Quick Summary**

Conic Finance on Ethereum was exploited due to a reentrancy issue, resulting in a loss of 3,254,850 $USD.

  


 **Details of the Exploit**

Conic Finance is a protocol for liquidity providers on Curve pools. The project fell victim to a reentrancy attack due to a wrong assumption about the address returned by the Curve Meta Registry for ETH in Curve V2 pools. As a result, 1,724 $ETH equivalent to approximately 3,254,850 $USD were stolen and transferred to another EOA, where they currently remain.

  


Interestingly, there was an unsuccessful attack attempt 10 minutes before the successful attack. A transaction was marked as read-only reentrancy. Conic has reached out to the exploiter via a transaction sent from the official Conic Multisig address.

  


 **Block Data Reference**

Attacker Address:

https://etherscan.io/address/0x8D67db0b205E32A5Dd96145F022Fa18Aae7DC8Aa

  


Funds Holder Address:

https://etherscan.io/address/0x3d32c5a2e592c7b17e16bddc87eab75f33ae3010

  


Malicious Transaction:

https://etherscan.io/tx/0x8b74995d1d61d3d7547575649136b8765acb22882960f0636941c44ec7bbe146

  


Unsuccessful Attack Attempt:  
https://etherscan.io/tx/0x97a8315e942dd180fb90a17b92f7dabd6e8a2e5b9fd5e4a95ee4049ff33d2f16


Proof Links:
- [https://twitter.com/ConicFinance/status/1682385596700844032](https://twitter.com/ConicFinance/status/1682385596700844032)
- [ https://twitter.com/BlockSecTeam/status/1682346827939717120]( https://twitter.com/BlockSecTeam/status/1682346827939717120)


