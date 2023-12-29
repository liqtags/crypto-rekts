# Safe Dollar
![Safe Dollar](/rektimages/Safe-Dollar.png)
- Amount Lost: $95,392.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-6-20

The attacker's address:  
https://polygonscan.com/address/0x8a0a1eb0bae23e4e95608e3aad7fa25b0d907c6c  
  
The attack transaction:  
https://polygonscan.com/tx/0x76c722c7bd90f6db0ad28692f86336007626e938ba7b1fcae98e9b404e66b210  
  
The re-entrance attack on the Token Locker smart contract was performed, Safe Dollar share tokens were affected.  
  
The contract itself does not have an issue with standard ERC20, but since the PLX token is ERC777 standard, there will be _tokenReceived_ () callback event every time method _transfer_ () triggered. The attacking smart contract deployed by the hacker has included the _unlockAll_ () trigger repeatedly (40 times) in the event, so he was able to unlock more than the amount he locked in before.  
  
The attacker withdrew 9,959.26 SDS, then sold for 95,392 USDC after bridging all to Ethereum.


Proof Links:
- [https://safedollar.medium.com/safedollar-postmortem-analysis-96c8cfb4c2a3](https://safedollar.medium.com/safedollar-postmortem-analysis-96c8cfb4c2a3)
- [ https://polydex.medium.com/plx-locker-smart-contract-incident-post-mortem-75342124a3e8]( https://polydex.medium.com/plx-locker-smart-contract-incident-post-mortem-75342124a3e8)


