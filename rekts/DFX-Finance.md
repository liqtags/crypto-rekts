# DFX Finance
![DFX Finance](/rektimages/DFX-Finance.png)
- Amount Lost: $7,645,284.00
- Funds Returned: $204,800.00
- Category: Exchange (DEX)
- Date: 2022-11-10

**Quick Summary**

DFX Finance was exploited due to a flashloan vulnerability. The attacker siphoned off 4,445,279 $USD worth of assets, and an MEV bot was able to frontrun the hacker for the additional 3,200,000 $USD.

  


 **Details of the Exploit**

DFX Finance is a trading protocol providing flash loans. The attacker drained 4,445,279 $USD worth of assets in various tokens and transferred 2962 $ETH through Tornado Cash. 545,312 $USD worth of $CADC stays at the attacker's address, and 135,265 $USD worth of $TRYb remains at the malicious contract used for an attack. The malicious actor exploited a known smart contract vulnerability that allows passing the balance check after a flashloan and gives approval of tokens to the attacker. The MEV bot was able to frontrun the hacker during token transfers for an additional 3,200,000 $USD in $USDC, $NZDS, $CADC, and $GYEN tokens. The DFX team claims that they are contacting the MEV bot owners to return the lost funds.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x14c19962e4a899f29b3dd9ff52ebfb5e4cb9a067

  


Malicious contract:

https://etherscan.io/address/0x6cfa86a352339e766ff1ca119c8c40824f41f22d

  


MEV bot:

https://etherscan.io/address/0xfde0d1575ed8e06fbf36256bcdfa1f359281455a

  


Malicious transactions list:

https://etherscan.io/txs?a=0x6cfa86a352339e766ff1ca119c8c40824f41f22d


Proof Links:
- [https://www.theblock.co/post/185796/polychain-dfx-finance-hacked?utm_source=rss&utm_medium=rss](https://www.theblock.co/post/185796/polychain-dfx-finance-hacked?utm_source=rss&utm_medium=rss)
- [ https://twitter.com/DFXFinance/status/1590858727070273536]( https://twitter.com/DFXFinance/status/1590858727070273536)
- [ https://twitter.com/spreekaway/status/1590804841261305856?s=46&t=oKKN-0DnuU0JRLt8jtjwAg]( https://twitter.com/spreekaway/status/1590804841261305856?s=46&t=oKKN-0DnuU0JRLt8jtjwAg)
- [ https://twitter.com/DFXFinance/status/1593705258038935553?s=20&t=DGJwAI_DRC0jNC4UjkkP7Q]( https://twitter.com/DFXFinance/status/1593705258038935553?s=20&t=DGJwAI_DRC0jNC4UjkkP7Q)
- [ https://docs.google.com/spreadsheets/d/1MTaFBpNZe_YeRLhh2NGTLPy-lswcSTJ3aIvM-vFc4Ew/edit#gid=0]( https://docs.google.com/spreadsheets/d/1MTaFBpNZe_YeRLhh2NGTLPy-lswcSTJ3aIvM-vFc4Ew/edit#gid=0)


