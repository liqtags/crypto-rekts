# GenomesDAO
![GenomesDAO](/rektimages/GenomesDAO.png)
- Amount Lost: $43,269.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-8-6

**Quick Summary**

GenomesDao was attacked. Three smart contracts were attacked and the amount that was stolen by the hacker is approximately $43k.

 **  
Details of the Exploit**

GenomesDAO is a DAO focused on secure, private and verifiable monetization of genomic data using DeFi. 

There was a vulnerability in the contract due to which an hacker can repeatedly invoke "victim" contracts. The hacker first created fake LP tokens and using the initialization function, he was able to install a real LP contract token on a fake one.  
The hacker then supplied a fake token using the shake function to get the LP tokens of the contract. Then the hacker uses the initialization function to return to the original LP-token and revokes the real LP of the contract using the output function.  
Thus, the hacker was able to take a profit of about $43k.

  


 **Block Data Reference**

Victim addresses:

1) https://polygonscan.com/address/0x3606cFa43f53098BC00b3FCFF3A333F6947F3c92

2) https://polygonscan.com/address/0x28fc73E9D9f158E7DC57A4E81aa0175d6847f714

3) https://polygonscan.com/address/0x48D1CcB09f771788F59c8aAAB613936eDfA267b7

  


Attacker address: https://polygonscan.com/address/0x43ec1d163cc4c15b574f86d8203c3b0f3ebed7a3

  


Attacker smart contract addresses:

1) https://polygonscan.com/address/0x8e10c9493501a828304d77630b6f862bbf50c052

2) (Token) https://polygonscan.com/address/0x9aa63491bb927f024d37b0e6017137f7f03da3c6

  


Transactions:

Swap $AnyMATIC to blockchain $MATIC: https://polygonscan.com/tx/0x074f3076ea2c16ef34b15114e751dcdc044ee2e9a26d762a2e96bf97a4509311


Proof Links:
- [https://en.0xzx.com/security-agency-brief-analysis-of-genomesdao-hack/](https://en.0xzx.com/security-agency-brief-analysis-of-genomesdao-hack/)
- [ https://www.aliens.com/livenews/latest/brief-analysis-of-genomesdao-hack-by-security-agency]( https://www.aliens.com/livenews/latest/brief-analysis-of-genomesdao-hack-by-security-agency)


