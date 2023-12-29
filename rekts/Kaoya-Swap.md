# Kaoya Swap
![Kaoya Swap](/rektimages/Kaoya-Swap.png)
- Amount Lost: $118,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-8-24

**Quick Summary**

On August 24th, 2022, KaoyaSwap, a decentralized transaction protocol built on the Binance Smart Chain, was attacked due to a bug in the swapExactTokensForETHSupportingFeeOnTransferTokens function. The vulnerability allowed the attacker to steal approximately $118,000 worth of 37,294 BUSD and 271.2 wBNB.

  


 **Details of the Exploit**

The bug was found in the swapExactTokensForETHSupportingFeeOnTransferTokens function, which was used to swap Fee-On-Transfer-Tokens. These tokens charge a fee for every transfer() or transferFrom(), causing the receiver to get less than the sent amount. The function miscalculated the amount to be transferred to the user when the last pair appeared multiple times in the swap path, allowing the attacker to steal funds.

  


The Attack Process:

The attacker designed a swap path that included two self-constructed tokens, resulting in the tokenA and wBNB pair being included twice in the swap path. The attacker borrowed a flash loan of 1800 wBNB and added liquidity to newly constructed token pairs. After the swap and removing liquidity, the attacker profited around 271 wBNB and 37,295 BUSD.

  


After the Exploit:

KaoyaSwap has yet to release an official statement. BlockSec identified several addresses that profited from the attack.

  


 **Block Data Reference**

Exploit tx:

https://bscscan.com/tx/0xc8db3b620656408a5004844703aa92d895eb3527da057153f0b09f0b58208d74

  


Involved addresses:

https://etherscan.io/address/0x8df3dd42bd51dd637580be6f15f651608b749ca1

https://etherscan.io/address/0x236b6150d7cc095d923fc0463977b71e84c891e5

https://etherscan.io/address/0xb77e7ee8e131d7425112df0f0f3c10e1c2208589

https://etherscan.io/address/0xe946bc154baa243b48fcf156977910bbb236df09

https://etherscan.io/address/0x50fc7d751cdde692682a04f59c2c9be2530b4d28


Proof Links:
- [https://medium.com/quillhash/kaoyaswap-logic-exploit-analysis-quillaudits-7c6c1575926a](https://medium.com/quillhash/kaoyaswap-logic-exploit-analysis-quillaudits-7c6c1575926a)


