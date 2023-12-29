# KyberSwap
![KyberSwap](/rektimages/KyberSwap.png)
- Amount Lost: $45,275,428.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-11-23

**Quick Summary**

KyberSwap DEX suffers a $45 million loss in cross-chain flash loan price manipulation attack.

  


 **Details of the Exploit**

On November 23, 2023, KyberSwap, a cross-chain DEX, was exploited in a flash loan attack that manipulated prices and ticks, leading to an approximate loss of $45 million across several chains. The attacker used a flash loan to deplete pools with low liquidity by executing swaps and strategic position changes. Multiple swap steps and cross-tick operations were initiated to induce double liquidity counting, effectively draining the pools. The attacker also sent an on-chain message, stating that negotiations would start once they were fully rested.

Losses across chains:

        \- Ethereum

            \- 7,624,223 USD worth of WETH, KNC, USDC, and more

        \- Arbitrum

            \- 20,378,076 USD worth of WETH, ARB, WBTC, DAI, and more

        \- Polygon

            \- 1,196,359 USD worth of WETH, WMATIC, WBTC, and more

        \- Base

            \- 325,085 USD worth WETH

        \- Optimism

            \- 15,738,093 USD worth of wstETH, cbETH, WETH, OP, and more

        \- Avalanche

            \- 23,592 USD worth of USDC and AVAX

  


 **Block Data Reference**

Ethereum:

\- Attacker: https://etherscan.io/address/0x50275E0B7261559cE1644014d4b78D4AA63BE836

\- Malicious Transaction: https://etherscan.io/tx/0x485e08dc2b6a4b3aeadcb89c3d18a37666dc7d9424961a2091d6b3696792f0f3

\- On-chain Message: https://etherscan.io/tx/0x7a8912583520304ce2364fa165dafe94461a91ab2dcf45dab942e296594dc40a

  


Arbitrum:

\- Funds Holders: 

https://arbiscan.io/address/0xc9b826bad20872eb29f9b1d8af4befe8460b50c6

https://arbiscan.io/address/0x84E66f86C28502C0fC8613e1D9CbBEd806F7Adb4

https://arbiscan.io/address/0x98d69d3ea5f7e03098400a5bedfbe49f2b0b88d3

\- Malicious Transaction: https://arbiscan.io/tx/0x567f0ba7741d097b6b1aaba68e8b75b9930f3cf946681cf9ad068aa34eb11c5b

\- Bridging Transaction: https://arbiscan.io/tx/0x8a7fc196e97b0aab375c27f11e44afdc4a1ea44d29d545d333df8c6f7e0789e4

  


Avalanche:

\- Funds Holders: https://snowtrace.io/address/0xc9b826bad20872eb29f9b1d8af4befe8460b50c6

\- Malicious Transaction: https://snowtrace.io/tx/0x96d90b23678b34e9ff324bdef7a18bf190289afff848a26882a1fe3110bf9714

  


Optimism:

\- Funds Holders: https://optimistic.etherscan.io/address/0xc9b826bad20872eb29f9b1d8af4befe8460b50c6

\- Malicious Transaction: https://optimistic.etherscan.io/tx/0x7f325cf1201422cf7ab6dd06d66136c55b399144f21b70f09a0c799782c5c874

  


Polygon:

\- Funds Holders: https://polygonscan.com/address/0xc9b826bad20872eb29f9b1d8af4befe8460b50c6

\- Malicious Transaction: https://polygonscan.com/tx/0xb58c81460ef0167f492fb4900e9da60cc6fa1117bd5b67b2100bb5b5e5df8b0c

  


Base:

\- Funds Holders: https://basescan.org/address/0xc9b826bad20872eb29f9b1d8af4befe8460b50c6

\- Malicious Transaction: https://basescan.org/tx/0x0a2957e7a2b45db525143d419137de854a741e7d2f61468b1dc3f83c9c27f9f7


Proof Links:
- [https://twitter.com/spreekaway/status/1727462694138024249](https://twitter.com/spreekaway/status/1727462694138024249)
- [ https://www.coindesk.com/tech/2023/11/23/kyberswap-dex-hacked-for-48-million-attacker-teases-negotiations/]( https://www.coindesk.com/tech/2023/11/23/kyberswap-dex-hacked-for-48-million-attacker-teases-negotiations/)


