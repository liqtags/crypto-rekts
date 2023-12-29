# Beanstalk
![Beanstalk](/rektimages/Beanstalk.png)
- Amount Lost: $181,000,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2022-4-18

**Quick Summary**  

A flash loan attack was occurred on Beanstalk Governance resulting in a theft of $77M.

  


 **Details of the Exploit**

The attacker was initially funded through Synapse bridge at:  
https://etherscan.io/tx/0x1fb73ec5ed8c25b9ca7c9c3c465ab4bbca8554927094f939d96600271475e101  
  
Since the $BEAN contract’s governance actions have 1 day of delay, the attacker prepared the governance proposal in advance. Proposal #18 takes the whole contract’s value, while Proposal #19 transfers $250k to the Ukraine donation address. BIP18 is the name of this Ukraine proposal (instead of BIP19)  
  
BIP18 proposal transaction:  
https://etherscan.io/tx/0x3cb358d40647e178ee5be25c2e16726b90ff2c17d34b64e013d8cf1c2c358967  
  
The attacker’s contract that was used to perform a flash loan:  
https://etherscan.io/address/0x1c5dcdd006ea78a7e4783f9e6021c32935a10fb4  
  
The transaction behind the flash loan:  
https://etherscan.io/tx/0xcd314668aaa9bbfebaf1a0bd2b6553d01dd58899c508d4729fa7311dc5d33ad7  
  
The flash loan was used to get:  
\- 350m DAI, 500m USDC and 150m USDT from Aave;  
\- 32m BEAN from Uniswap;  
\- 11.6M LUSD from SushiSwap.  
  
These tokens were used to supplement the liquidity in Curve pools with BEAN for governance voting.  
  
At first, the attacker minted 3CRV using DAI, USDC, and USDT. After, he generated the token BEAN3CRV-f using BEANS. This was followed by a deposit of 32 million $BEAN tokens and 25 million $LUSD into yet another contract to create a new token named BEAN3LUSD-f.  
  
BEAN3CRV-f and BEAN3LUSD-f may be transformed straight into Seeds (a special type of asset called which acts like voting power in the system), providing the attacker with sufficient voting power. In reality, the attacker was able to manage more than 70% of the total number of Seeds thanks to the flash loan and $BEAN  
  
The BIP18 triggers the execution of the designed code with the governance privilege to drain the pool fund:  
https://etherscan.io/tx/0x68cdec0ac76454c3b0f7af0b8a3895db00adf6daaf3b50a99716858c4fa54c  
  
During the attack transaction, 250,000 USDC was donated to the Ukraine Crypto Donation address.  
  
$181 million was drained from Beanstalk, but the attacker only kept $76M, which were swapped on Ether and deposited into Tornado Cash mixer in a bunch of transactions:  
https://bloxy.info/txs/transfers_from/0x1c5dcdd006ea78a7e4783f9e6021c32935a10fb4?currency_id=1


Proof Links:
- [https://bean.money/blog/beanstalk-governance-exploit](https://bean.money/blog/beanstalk-governance-exploit)
- [ https://blog.defiyield.app/beanstalk-losses-181-million-the-governance-attack-using-a-flash-loan-7459174dfa8e]( https://blog.defiyield.app/beanstalk-losses-181-million-the-governance-attack-using-a-flash-loan-7459174dfa8e)
- [ https://rekt.news/beanstalk-rekt/]( https://rekt.news/beanstalk-rekt/)
- [ https://twitter.com/peckshield/status/1515680335769456640]( https://twitter.com/peckshield/status/1515680335769456640)
- [ https://twitter.com/kelvinfichter/status/1515735674703470595]( https://twitter.com/kelvinfichter/status/1515735674703470595)


