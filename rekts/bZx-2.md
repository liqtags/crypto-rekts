# bZx
![bZx](/rektimages/bZx-2.png)
- Amount Lost: $665,840.00
- Funds Returned: $0.00
- Category: Other
- Date: 2020-2-18

The transaction behind the attack:  
https://etherscan.io/tx/0x762881b07feb63c436dee38edd4ff1f7a74c33091e534af56c9f7d49b5ecac15  
  
The attacker's address:  
https://etherscan.io/address/0xb8c6ad5fe7cb6cc72f2c4196dca11fbb272a8cbf  
  
The attacker:  
\- flash loaned 7,500 WETH from the bZx protocol  
  
\- with the flash loan, the attacker swapped 900 ETH in two batches for sUSD through Kyber. The first batch was sold for 540 ETH in KyberSwap that, after internal consulting of reserves, was routed the swap order to the KyberUniswap reserve (0x31e085afd48a1d6e51cc193153d625e8f0514c7f) and got 92,419 sUSD in return. The second batch was sold 18 times for 20 ETH each, also in Kyber that, after internal consulting of reserves, routed the swap orders to the Kyber-sUSD reserve (0x4cb01bd05e4652cbb9f312ae604f4549d2bf2c99) and got 63,584 sUSD in return. The sell-off of these two batches effectively drove the price of sUSD up to 0.00899 ETH (or 1ETH=111 sUSD). The manipulated price is around 2.5x higher when compared to the average ETH/sUSD market price. After the swap, the attacker acquired 92,419+63,584=156,003 sUSD tokens at his disposal  
  
\- turned to Synthetic Depot contract to acquire substantially more sUSD at market price. Note Synthetic Depot contract allows for depositing Ether for sUSD at a fair rate. The attacker sent 6,000 ETH and bought 943,837 sUSD back (with 2,482 ETH refunded back as there’s no enough sUSD to buy). Note this step is typically launched before the previous step. For whatever reason, this is not the case in this particular hack (and the ordering does not affect the final result as the pricing in Synthetic Depot is not affected by KyberSwap)  
  
\- the sUSD/ETH price was driven up and the attacker has >1M sUSD at his disposal. Note that the attacker takes the approach by capitalizing on the spiked price in a profitable Compound position in the first hack. Considering the possibly low liquidity of sUSD, the attacker this time takes the approach of first collateralizing the collected >1M sUSD back into bZx and then borrowing from it 6,796 ETH. As bZx relies on Kyber for the price feed, with the spiked sUSD/ETH price, the collection of >1M sUSD allows for the borrow of 6796 ETH. With the normal conversion rate of 1ETH=111 sUSD, the same amount of sUSD tokens can only buy 4,000 ETH, which indicates that this loan is now underwater with insufficient collateralization  
  
\- the attacker repaid the 7,500 ETH flash loan back to bZx with a profit of 2,378 ETH


Proof Links:
- [https://peckshield.medium.com/bzx-hack-ii-full-disclosure-with-detailed-profit-analysis-8126eecc1360](https://peckshield.medium.com/bzx-hack-ii-full-disclosure-with-detailed-profit-analysis-8126eecc1360)
- [ https://www.coindesk.com/defi-project-bzx-exploited-for-second-time-in-a-week-loses-630k-in-ether]( https://www.coindesk.com/defi-project-bzx-exploited-for-second-time-in-a-week-loses-630k-in-ether)


