# Array Finance
![Array Finance](/rektimages/Array-Finance.png)
- Amount Lost: $516,391.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-7-19

The attacker:  
https://etherscan.io/address/0x13370353f69665f36eb0a708f828c50dc23604af  
  
The transaction behind the attack:  
https://etherscan.io/tx/0xa17bbc7c9ab17aa88fdb5de83b41de982845e9c9c072efff6709dd29febf0daa  
  
The attacker:  
\- flash loaned DAI, USDC, WETH, WBTC on Aave  
  
\- invoked the _buy()_ function of Array Finance. The attacker gained 430 ARRAY tokens minted by Array Finance using 45.91 WETH  
  
\- invoked the _joinPool()_ function of a closed source contract (Array Collater - 0xa800cda5f3416a6fb64ef93d84d6298a685d190d) five times  
  
\- deposited 676,410.58 DAI + 679,080.46 USDC + 901.82 WETH + 20 WBTC + 20 renBTC and gained 726.38 aBPT tokens minted by Array Collater  
  
\- invoked the _sell()_ function to burn 430 ARRAY tokens and got 77.17 aBPT tokens  
  
\- invoked the _exitPool()_ function of the Array Collater  
  
\- burned 804.55 aBPT tokens obtained in previous steps and obtained 748,271.55 DAI + 751,225.08 USDC + 997.62 WETH + 22.63 WBTC + 22.74 renBTC  
  
\- repaid the flash loan.  
  
The attacker exploited the vulnerability: the price mechanism of the Array Finance depends on the _totalSupply_ of the aBPT token, which is manipulatable.



