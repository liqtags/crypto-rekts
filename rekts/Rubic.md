# Rubic
![Rubic](/rektimages/Rubic.png)
- Amount Lost: $1,420,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-25

**Quick Summary**

USDC balances of Rubic’s users have been drained. The current losses reached $1.42M.

 

 **Details of the Exploit**

All USDC approved to the RubicProxy contract got under the risk of being drained after the USDC address was added into the list of available routers in the RubicProxy contract.

Through the routerCallNative()  function, the attacker could call safeTransferFrom() on the USDC contract inputting user addresses, which have approved their USDC balances to be spent by RubicProxy, as the “from” parameter. 

 

 **Block Data Reference  **

The attacker address:

[https://etherscan.io/address/0x001b91c794dfeecf00124d3f9525dd32870b6ee9](https://etherscan.io/address/0x001b91c794dfeecf00124d3f9525dd32870b6ee9) 

 

The exploit transactions:

[https://etherscan.io/tx/0x9a97d85642f956ad7a6b852cf7bed6f9669e2c2815f3279855acf7f1328e7d46](https://etherscan.io/tx/0x9a97d85642f956ad7a6b852cf7bed6f9669e2c2815f3279855acf7f1328e7d46) 

[https://etherscan.io/tx/0x6551b933b984342fd353d4b522aee7db500900e208dc1337b0c1f17647e36e56](https://etherscan.io/tx/0x6551b933b984342fd353d4b522aee7db500900e208dc1337b0c1f17647e36e56) 

 

The “add available router ” transaction:

[https://etherscan.io/tx/0x30679e7b6b410fb78368f5fb6e4c203e44d81c66ae9014c797e40856be1bbe66](https://etherscan.io/tx/0x30679e7b6b410fb78368f5fb6e4c203e44d81c66ae9014c797e40856be1bbe66) 


Proof Links:
- [https://twitter.com/CryptoRubic/status/1606951013449097218](https://twitter.com/CryptoRubic/status/1606951013449097218)
- [ https://twitter.com/peckshield/status/1606937055761952770]( https://twitter.com/peckshield/status/1606937055761952770)


