# Cheese Bank
![Cheese Bank](/rektimages/Cheese-Bank.png)
- Amount Lost: $3,300,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2020-11-6

Addresses, related to the flash loan attack:  
The attacker - 0x882d72aaae187f54e85c7a0cb19dfec5316cd9aa  
Smart contract with the malicious logic - 0x9e0259437804c7bf175421a451bc80611a0b93c3  
  
Transaction behind the attack:  
https://etherscan.io/tx/0x600a869aa3a259158310a233b815ff67ca41eab8961a49918c2031297a02f1cc  
  
The attacker:  
\- took a flash loan of 21k ETH from dYdX  
  
\- swapped 50 ETH to 107k CHEESE at UniswapV2  
  
\- added 107k CHEESE and corresponding 78 ETH into the liquidity pool at UniswapV2 and got UNI_V2 LP tokens back  
  
\- minted sUSD_V2 tokens with all LP tokens got from Step 3. This allowed the exploit contract to use those LP tokens as collateral for borrowing crypto assets from Cheese Bank  
  
\- raised the CHEESE price at UniswapV2 by swapping 20k ETH to 288k CHEESE, making the UNI_V2 LP tokens more valuable as collaterals Cheese Bank. This is the crucial step in this incident since the Cheese Bank uses the amount of WETH in a liquidity pool to estimate the price of the corresponding LP token. The manipulated UNI_V2-CHEESE-ETH pool (with 20k+ WETH) allowed the attacker to drain all the USDC, USDT, and DAI withheld by Cheese Bank by legit _borrow_ () calls  
  
\- refreshed the price feeds of Cheese Bank. The attacker intentionally invoked the _CheesePriceOracle::refresh_ () function to refresh the price of the UNI_V2-CHEESE-ETH LP token which is derived from the amount of WETH in the liquidity pool and the ETH price derived from the UNI_V2-USDT-ETH pool. Specifically, the _CheesePriceOracle::fetchLPAnhorPrice_ () function gets the _wEthBalance_ of UNI_V2-CHEESE-ETH contract. With the passed in _ethPrice_ , the _totalValue_ is derived by _  wEthBalance x 2 x ethPrice_. Therefore, the unit price of the UNI_V2-CHEESE-ETH LP token is computed by _totalValue / totalSupply of LP tokens_. It means if the attacker could somehow increase the amount of WETH in a pool (e.g., _addLiquidity_ () with flash loan ether), the price of the LP token would be increased  
  
\- drained the USDC, USDT, DAI withheld by Cheese Bank by _borrow_ () calls. Besides the 2M USDC, 1.23M USDT and 87k DAI are borrowed from Cheese Bank. The exact balance of USDC/USDT/DAI is borrowed by the exploit contract  
  
\- swapped 288k CHEESE back to 19.98k ETH at UniswapV2  
  
\- swapped 58k USDC to 132 ETH at UniswapV2  
  
\- collected assets into https://etherscan.io/address/02b7165d0916e373f0235056a7e6fccdb82d2255  
  
\- repaid 21k ETH flashloan to dYdX.


Proof Links:
- [https://cheesebank2020.medium.com/cheese-bank-detailed-statement-a765372dd84f](https://cheesebank2020.medium.com/cheese-bank-detailed-statement-a765372dd84f)
- [ https://peckshield.medium.com/cheese-bank-incident-root-cause-analysis-d076bf87a1e7]( https://peckshield.medium.com/cheese-bank-incident-root-cause-analysis-d076bf87a1e7)


