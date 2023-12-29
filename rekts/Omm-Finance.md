# Omm Finance
![Omm Finance](/rektimages/Omm-Finance.png)
- Amount Lost: $1,900,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-1-21

**Quick Summary**

On January 21 2023 Omm Protocol was exploited. The hacker withdrew about $1.9M in IUSDC, USDS, bnUSD, and sICX tokens. 

  


 **Details of the Exploit**

On January 21 a hacker exploited a vulnerability in Omm by deploying a harmful contract. The hacker carried out 18 malicious transactions and was able to steal IUSDC, USDS, and bnUSD collateral that did not belong to them. They then used the stolen USDS as collateral to borrow sICX.

  


The bug was located in the Redeem function, which accepts an address as the collateral to be redeemed. The external call enabled the injection of a faulty smart contract, allowing the hacker to redeem the collateral without any prior deposit.

  


The hacker utilized Balanced to exchange the majority of the funds, which led to a significant deviation from the target price of 1 USD for bnUSD and other stablecoins.

  


They also moved IUSDC from ICON to other blockchains, such as Ethereum and Polygon, via Orbit Bridge.

  


 **Block Data Reference**

Main exploit wallet: 

hxc35cffe7c582cb313820fa6838dd357027ad3d07

  


Addresses on Ethereum and Polygon that received USDC via Orbit Bridge:

0x00082ff22852c7d3eaa157abe343f9b8e64cfd85

0x7e4d6232c47789df03d5849675438605c6efa60e

0x3b074b585864884035409a091aafd1e3749e152a

0x49fedf6ff59c5f35ce53e6a31738cf84172eab55

0x517dfb8643363e3bbb034d6ce59b99ef13dd22d6

0xA28408FD24cA1BE5e666e30eEcA59Cf8cdeBa448


Proof Links:
- [https://twitter.com/ommfinance/status/1617327827216658432](https://twitter.com/ommfinance/status/1617327827216658432)
- [ https://forum.omm.finance/t/omm-exploit-postmortem-january-2023/266]( https://forum.omm.finance/t/omm-exploit-postmortem-january-2023/266)


