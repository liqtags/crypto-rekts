# Uniswap
![Uniswap](/rektimages/Uniswap.png)
- Amount Lost: $8,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-7-11

**Quick Summary**

A Uniswap liquidity provider was subjected to a phishing attack, which incurred losses of $8M. _Uniswaps smart contracts were not involved in any shape or form in this phishing attack.  _

  


 **Details of the Exploit**

The victim received a fake airdrop of a lp token from the attacker disguised as a transaction coming directly from Uniswap. The attacker manipulated the trade log in order to make "Uniswap" appear as the sender of the transaction on blockscan.

The attacker set up a fake airdrop claim website upfront. When the victim tried to claim the airdrop on the phishing website, approvals were given to the attacker that enabled the hacker to gain control over the funds of the victims wallet.

The hacker exited a WBTC/USDC liquidity pool position the victim had established on Uniswap and exchanged assets for $ETH, which were withdrawn through Tornado.cash.

  


 **Uniswap was not the target of this attack, nor were any of Uniswaps smart contracts affected in this exploit.**

  


 **Block Data Reference**

The fake airdrop token address: https://etherscan.io/address/0xcf39b7793512f03f2893c16459fd72e65d2ed00c

Creator of the malicious fake airdrop tokens address: https://etherscan.io/address/0x24a4b33bfa8e32b3456f95381de429c11c2c6fd6

Hacker wallet address: https://etherscan.io/address/0x09b5027ef3a3b7332ee90321e558bad9c4447afa

Callling multicall for swapping $WBTC and $USDC to $ETH transaction: https://etherscan.io/tx/0x49efa8a111019e6117721042bc92de0b462ee6fa8a46e775c3f688614f02ce2d


Proof Links:
- [https://en.cryptonomist.ch/2022/07/13/4000-eth-stolen-uniswap-v3/?amp=1](https://en.cryptonomist.ch/2022/07/13/4000-eth-stolen-uniswap-v3/?amp=1)
- [ https://www.theblock.co/post/157021/uniswap-liquidity-provider-hacked-for-8-million-in-phishing-attack]( https://www.theblock.co/post/157021/uniswap-liquidity-provider-hacked-for-8-million-in-phishing-attack)
- [ https://cointelegraph.com/news/more-than-4-7m-stolen-in-uniswap-fake-token-phishing-attack]( https://cointelegraph.com/news/more-than-4-7m-stolen-in-uniswap-fake-token-phishing-attack)
- [ https://decrypt.co/104916/hackers-nab-8m-ethereum-uniswap-phishing-attack]( https://decrypt.co/104916/hackers-nab-8m-ethereum-uniswap-phishing-attack)
- [ https://beincrypto.com/uniswap-8m-ethereum-massive-phishing-attack/]( https://beincrypto.com/uniswap-8m-ethereum-massive-phishing-attack/)


