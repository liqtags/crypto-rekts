# DAO Maker
![DAO Maker](/rektimages/DAO-Maker-2.png)
- Amount Lost: $4,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-9-4

The attacker's address:  
https://etherscan.io/address/0x2708cace7b42302af26f1ab896111d87faeff92f  
  
DAO Maker vesting smart contracts had vulnerability that allowed a hacker to take ownership of the contract and withdraw the tokens from it. Tokens of DeRace, Showcase, Ternoa, Coinspaid were affected. The attacker initialized the key parameters of init() and changed the owner at the same time.  
  
The attacker invoked _emergencyExit_ () function to withdraw tokens at:  
https://etherscan.io/tx/0xcb5be97496995d58da6f97491845040547b878e53a7b71f907a13408f3a54e5f  
https://etherscan.io/tx/0x4c273c2403aafd97e4b553f0e381cf1c63e5f2efebbe2ded7642a06f2b68c879  
https://etherscan.io/tx/0x1692a57f19b5e8e4bc6a372ac3c83c77cd4a1ea78414377ea66d3d59f4a7d2b7  
https://etherscan.io/tx/0xdd0176475165b83c702d49a876d4dc888b73477ad8833582c72aa6ca5e0bacc3  
  
The attacker sold tokens at:  
https://etherscan.io/tx/0xbf38346aacf261f5e169a87ed874c33c21efb060c4a393e2b1443a3ac5d6e3fd  
https://etherscan.io/tx/0x3436af2c84d67254a4b81adc350c91d1b98ae52b2ff84645d14d4245c2d08c27  
https://etherscan.io/tx/0xc586a6b94e09556abf46ae3aa8cffa8e46dfcb0c22bce0b024d5e01743ceba9e  
https://etherscan.io/tx/0x76163daf6cf0c815c02fb1a98f5c6283ee7a922cbad41218eb7a6452c91824c8


Proof Links:
- [https://medium.com/daomaker/removing-all-smart-contract-risk-tech-team-tokens-52c55961e986](https://medium.com/daomaker/removing-all-smart-contract-risk-tech-team-tokens-52c55961e986)
- [ https://slowmist.medium.com/intelligence-of-slowmist-zone-dao-makers-vesting-system-was-hacked-5825e4828969]( https://slowmist.medium.com/intelligence-of-slowmist-zone-dao-makers-vesting-system-was-hacked-5825e4828969)
- [ https://rekt.news/daomaker-rekt/]( https://rekt.news/daomaker-rekt/)


