# Alpha Finance Lab
![Alpha Finance Lab](/rektimages/Alpha-Finance-Lab.png)
- Amount Lost: $37,500,000.00
- Funds Returned: $3,700,000.00
- Category: Other
- Date: 2021-2-13

**Quick Summary**

An attacker exploited a bug in Cream's Iron Bank, resulting in a loss of 13,244.63 WETH, 3.6M USDC, 5.6M USDT, and 4.26M DAI.

  


 **Details of the Exploit**

The attacker manipulated the system by swapping ETH for UNI, supplying ETH + UNI to the Uniswap pool, and swapping ETH for sUSD on Uniswap. They then deposited sUSD to Cream’s Iron Bank, borrowed 1000e18 sUSD, deposited UNI-WETH LP to WERC20, and used it as collateral. The attacker then repaid the sUSD, leaving a repay share of 1 less than the total share. This resulted in the attacker's EOA having 1 minisUSD debt and 1 debt share. They then borrowed 19709787742196 minisUSD and transferred it to their EOA, repeating this process 16 times, each time doubling the borrowed amount. The attacker then flash loaned from Aave, swapped USDC for sUSD, and deposited it to Cream to have enough liquidity to borrow using the custom spell. They continued doubling the sUSD borrow and swapped sUSD for USDC on Curve. They then borrowed 13,244.63 WETH + 3.6M USDC + 5.6M USDT + 4.26M DAI, supplied the stablecoins to Aave, and supplied aDAI, aUSDT, aUSDC to Curve a3Crv pool.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0x2b528a28451e9853f51616f3b0f6d82af8bea6ae#tokentxns

The transactions behind the attack:

https://etherscan.io/tx/0x4441eefe434fbef9d9b3acb169e35eb7b3958763b74c5617b39034decd4dd3ad

https://etherscan.io/tx/0xcc57ac77dc3953de7832162ea4cd925970e064ead3f6861ee40076aca8e7e571

https://etherscan.io/tx/0xf31ee9d9e83db3592601b854fe4f8b872cecd0ea2a3247c475eea8062a20dd41

https://etherscan.io/tx/0x98f623af655f1e27e1c04ffe0bc8c9bbdb35d39999913bedfe712d4058c67c0e

https://etherscan.io/tx/0x2e387620bb31c067efc878346742637d650843210596e770d4e2d601de5409e3

https://etherscan.io/tx/0x64de824a7aa339ff41b1487194ca634a9ce35a32c65f4e78eb3893cc183532a4

https://etherscan.io/tx/0x7eb2436eedd39c8865fcc1e51ae4a245e89765f4c64a13200c623f676b3912f9

https://etherscan.io/tx/0xd7a91172c3fd09acb75a9447189e1178ae70517698f249b84062681f43f0e26e

https://etherscan.io/tx/0xacec6ddb7db4baa66c0fb6289c25a833d93d2d9eb4fbe9a8d8495e5bfa24ba57

https://etherscan.io/tx/0x745ddedf268f60ea4a038991d46b33b7a1d4e5a9ff2767cdba2d3af69f43eb1b

https://etherscan.io/tx/0xc60bc6ab561af2a19ebc9e57b44b21774e489bb07f75cb367d69841b372fe896


Proof Links:
- [https://rekt.news/alpha-finance-rekt/](https://rekt.news/alpha-finance-rekt/)
- [ https://blog.alphafinance.io/alpha-homora-v2-post-mortem/]( https://blog.alphafinance.io/alpha-homora-v2-post-mortem/)


