# Wild Credit
![Wild Credit](/rektimages/Wild-Credit.png)
- Amount Lost: $611,963.00
- Funds Returned: $611,963.00
- Category: Borrowing and Lending
- Date: 2021-5-27

The attacker's address:  
https://etherscan.io/address/0xb1af124c860f819bf8de7d4c459e5b31fecdb95e  
  
The transaction behind the attack:  
https://etherscan.io/tx/0xdbef3b393a64608756c284568217355f694a0e5c8edf80eac75ec087d642ce07  
  
The exploited contract:  
https://etherscan.io/address/0x7b3b69eab43c1aa677df04b4b65f0d169fcdc6ca  
  
Wild Credit team left initialize() function in the LPTokenMaster contract public and reusable, so anyone can become the owner of the LP token contract. The hacker took ownership of the contract, has minted tokens to themselves, and then used those tokens to withdraw real funds.  
  
The hacker was a whitehat and returned the funds to the contract deployer:  
https://etherscan.io/tx/0xb4fffa0e824034a10af2807f1504ac247ae1dd6f2bcfed8085989bbfda434542


Proof Links:
- [https://twitter.com/WildCredit/status/1397786796675649538](https://twitter.com/WildCredit/status/1397786796675649538)
- [ https://twitter.com/mudit__gupta/status/1397888546686398470]( https://twitter.com/mudit__gupta/status/1397888546686398470)


