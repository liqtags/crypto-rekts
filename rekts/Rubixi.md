# Rubixi
![Rubixi](/rektimages/Rubixi.png)
- Amount Lost: $6,622.00
- Funds Returned: $0.00
- Category: Other
- Date: 2016-3-14

**Quick Summary**

Rubixi contract had a security issue, which allowed anyone to become a contract owner and withdrew fees.

  


 **Details of the Exploit**

Rubixi was a project on the Ethereum chain designed to collect funds and had a privileged function to collect fees. The contract itself had a logic issue, which allowed anyone to become a contract owner and withdraw fees for themselves. The constructor of the contract was named wrong and become a regular function. After becoming a contract owner, anyone can call the unprotected function collectAllFees() to withdraw fees. The contract currently has only 4 $ETH, which is stuck and can't be withdrawn. 

  


 **Block Data Reference**

Deployment transaction:

https://etherscan.io/tx/0x4496b64234e97bb7ed008d09938fb9e94ecf3461cbd89a5eabda356a098f8ec3

  


Contract deployer:

https://etherscan.io/address/0xdd68da49b2a0c46eb508bd4f18044b5c6268ad60

  


Owner change example:

https://etherscan.io/tx/0x9385dca4891753f8ba5817964e5321849b5c7172f5a669aee144344d0610684c

  


Withdrawal example:

https://etherscan.io/tx/0x580222b06bad8c57c83c6edc89afac196f3e571026041e75625bb60cbe7dd472


Proof Links:
- [https://hackenproof.com/vulnerabilities/5bd1ac7a75fa7418019cf8e1](https://hackenproof.com/vulnerabilities/5bd1ac7a75fa7418019cf8e1)


