# BNB42
![BNB42](/rektimages/BNB42.png)
- Amount Lost: $2,602,079.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-2-14

The address involved in the scam:  
https://bscscan.com/address/0x9b74fde50f3fcd3a02fafea6a187092630d6eb8f  
  
The address involved in the scam deployed the unverified contract which contained _withdraw_ () function that allows only the owner to withdraw the entire total BNB (eth.balance(this.address) wei) to the owner’s address.  
  
The contract deployer invoked withdraw() to transfer 6,445.42 BNB onto own address at:  
https://bscscan.com/tx/0x749215ebe457aa681194684401257fe8fb44daecb9f50a077b12c71e83cf9414  
  
Stolen funds were distributed to a bunch of external addresses and deposited into the Tornado Cash mixer.


Proof Links:
- [https://twitter.com/PeckShieldAlert/status/1493513392870473728](https://twitter.com/PeckShieldAlert/status/1493513392870473728)
- [ https://twitter.com/CertiKCommunity/status/1493614458144448513]( https://twitter.com/CertiKCommunity/status/1493614458144448513)


