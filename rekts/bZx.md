# bZx
![bZx](/rektimages/bZx.png)
- Amount Lost: $355,880.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,Exchange (DEX)
- Date: 2020-2-15

The transaction behind the attack:  
https://etherscan.io/tx/0xb5c8bd9430b6cc87a0e2fe110ece6bf527fa4f170a4bc8cd032f768fc5219838  
  
The attacker's address:  
https://etherscan.io/address/0x148426fdc4c8a51b96b4bed827907b5fa6491ad0  
  
The attacker:  
\- flash loaned 10,000 ETH from the dYdX exchange  
  
\- with the borrowed flash loan, the attacker deposited 5,500 ETH into Compound as collateral to borrow 112 WBTC  
  
\- Deposited 1300 ETH and called bZx margin trading function, i.e., mintWithEther (that cascadingly invokes marginTradeFromDeposit). The margin trading function leveraged KyberSwap to swap the borrowed 5637.623762 ETH for 51.345576 WBTC in return. Notice that it is 5x borrow to short ETH. The swap essentially drove up the conversion rate of 1 WBTC to around 109.8 WETH, roughly triple the normal conversion rate (~38.5 WETH/WBTC)  
  
\- with the spiked WBTC price on Uniswap, the attacker sold the Compound-borrowed 112 WBTC back for WETH on Uniswap. This dump step leads to the net of 6871.4127388702245 ETH in return with the overall conversation rate of 1WBTC=61.4 WETH  
  
\- With the netted 6871.4127388702245 ETH from the dumped 112 WBTC, the attacker repaid the flash loan 10000.000000000011ETH back to dYdX.


Proof Links:
- [https://bzx.network/blog/postmortem-ethdenver](https://bzx.network/blog/postmortem-ethdenver)
- [ https://peckshield.medium.com/bzx-hack-full-disclosure-with-detailed-profit-analysis-e6b1fa9b18fc]( https://peckshield.medium.com/bzx-hack-full-disclosure-with-detailed-profit-analysis-e6b1fa9b18fc)


