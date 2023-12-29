# Warp Finance
![Warp Finance](/rektimages/Warp-Finance.png)
- Amount Lost: $7,800,000.00
- Funds Returned: $5,800,000.00
- Category: Borrowing and Lending
- Date: 2020-12-18

**Quick Summary**

Exploitation of WarpFinance via flash loans resulted in a loss of approximately $7.8 million.

  


 **Details of the Exploit**

The attacker initiated the exploit by taking four different flash loans of 2.9M DAI + 344.8K WETH from dYdX and UniswapV2. They then deposited the dYdX flash loan into the UniswapV2 pair (WETH-DAI), minting 94.349K LP tokens in return. These tokens were transferred to WarpVaultLP as collateral. The attacker then swapped 341K WETH for 47.6M DAI via UniswapV2, causing DAI to become very expensive and doubling the LP token price. With the inflated LP token price and collateral value, the attacker was able to borrow 3.86M DAI and 3.9M USDC from WarpFinance, totaling about $7.8 million. The attacker then returned the flash loans to dYdX and UniswapV2.

  


 **Block Data Reference**

Smart contract used in the attack:

https://etherscan.io/address/0xdf8bee861227ffc5eea819c332a1c170ae3dbacb

  


Transactions involved in the attack:

https://ethtx.info/mainnet/0x8bb8dc5c7c830bac85fa48acad2505e9300a91c3ff239c9517d0cae33b595090

https://etherscan.io/tx/0x8bb8dc5c7c830bac85fa48acad2505e9300a91c3ff239c9517d0cae33b595090


Proof Links:
- [https://warpfinance.medium.com/warp-finance-exploit-summary-recovery-of-funds-5b8fe4a11898](https://warpfinance.medium.com/warp-finance-exploit-summary-recovery-of-funds-5b8fe4a11898)


