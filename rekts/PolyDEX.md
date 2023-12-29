# PolyDEX
![PolyDEX](/rektimages/PolyDEX.png)
- Amount Lost: $511,144.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-6-20

The attacker's address:  
https://polygonscan.com/address/0x8a0a1eb0bae23e4e95608e3aad7fa25b0d907c6c  
  
The transaction behind the attack:  
https://polygonscan.com/tx/0x6b3f057683083d7f0a25e4d3898ca68308cfe2335878143466f84b3003ebe3a2  
  
The attacker performed the re-entrance attack on the Token Locker smart contract. The contract itself does not have an issue with standard ERC20, but since the PLX token is ERC777 standard, there will be _tokenReceived_ () callback event every time method _transfer_ () triggered. The attacking smart contract deployed by the hacker has included the _unlockAll_ () trigger repeatedly (40 times) in the event, so he was able to unlock more than the amount he locked in before.  
  
The attacker:  
\- locked 15,711,384 PLX in the Locker, received 15,711,384 fPLX

\- unlocked all 15,711,384 fPLX from the Locker, received 1,184,289 PLX

\- in the _tokenReceived_ () called _unlockAll_ () function

\- repeated previous step 40 times.  
  
Stolen tokens were sold on USDC, which then were bridged on Ethereum:  
https://polygonscan.com/tx/0xe02124b1a2fa3c4d7f0bad162f06c96688f5911951010063ac7f65ef4b6bd1ad


Proof Links:
- [https://polydex.medium.com/plx-locker-smart-contract-incident-post-mortem-75342124a3e8](https://polydex.medium.com/plx-locker-smart-contract-incident-post-mortem-75342124a3e8)


