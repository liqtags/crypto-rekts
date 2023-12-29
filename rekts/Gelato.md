# Gelato
![Gelato](/rektimages/Gelato.png)
- Amount Lost: $0.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-12-12

The transaction behind the exploit:  
https://etherscan.io/tx/0x90a5d10ca9092a82464fd87efb1a7ed06c0d0420fde0cbb20af6e7ec9046c303  
  
The bug in GUniRouter02 within the rebalanceAndAddLiquidity() function was able to be exploited to transfer funds from users' wallets who have previously approved GUniRouter02 for spending their tokens.  
  
Tokens, which were mostly affected: DAI, USDC, FEI, agEUR, FRAX, WETH, ENS, ETH2x-FLI, G-UNI DAI/USDC, and POP.  
  
The root issue: rebalanceAndAddLiquidity() can be invoked with custom _swapAction and _swapDatas parameters. Given the fact that users have given infinite allowances for the router contract, the possible exploiter could drain users' funds from their wallets.  
  
The project team executed a successful whitehat hack which secured around $26M of user funds.


Proof Links:
- [https://twitter.com/gelatonetwork/status/1469813838916866050](https://twitter.com/gelatonetwork/status/1469813838916866050)
- [ https://twitter.com/peckshield/status/1469816376923942912]( https://twitter.com/peckshield/status/1469816376923942912)


