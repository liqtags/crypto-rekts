# Alpha Finance Lab
![Alpha Finance Lab](/rektimages/Alpha-Finance-Lab-2.png)
- Amount Lost: $170,704.00
- Funds Returned: $170,704.00
- Category: Yield Aggregator
- Date: 2021-10-23

Alpha Finance team received a user report regarding abnormal position value loss in Alpha Homora V2 on Ethereum after the position was opened. Looking at the transaction details, the slippage control values correctly reflected the 1% tolerance, but the LP value still did not conform.  
  
The problem: a Miner Extractable Value (MEV) bot inspected the transaction, bundled the transactions such that the bot could make financial profits, and sent these transactions privately to a particular group of miners who then mined these transactions.

  


The Uniswap V2 Router contract has implicit assumptions that are not clearly stated on the contract level. Hence, without stating these assumptions, slippage control for some trades on Uniswap V2 may not be checked and may not be taken into account at all in certain scenarios.

  


These implicit assumptions on Uniswap V2 resulted in 20 addresses on Alpha Homora V2 being impacted and lost a total of 40.93 ETH to miners who extracted this value.  
  
The list of affected addresses:  
0xFb8b6a0bE6353C254C3F576A268e69655c29E159

0xD50f649a2c9fD7AE88C223DA80e985D71DE45593

0xA64e4dCB1Ed06A9658EC85Bb5BF66D6dEfdd6982

0x20f9ddFA193D0fe2f73d8b7D749B1355eF019887

0xA6e3475e2d4A9937b61be131407598ed188b54f3

0x6A07Ea36da7850cc89BE2523eB9423fBE7237061

0x6Ce8B65dD4eb013FfFCf44C5B400D6b431f5c584

0xD4ad5d62dCe1A8Bf661777a5c1dF79BD12Ac8F1D

0x62BfDF7699972cd2811424644Fcd6281B2178DAd

0x5C7c6d069ba232718f37C27A9549b547C359E31C

0x7bdfE11c4981Dd4c33E1aa62457B8773253791b3

0x5908029c5851c01185Be6D8d42888C76950C6895

0x203a67b09429d1BAA2c56Eb4C57634E498F07819

0xB5A9621B0397Bfc5B45896CaE5998b6111bcDCe6

0xEC0E5e386f0c4be9220E0347330603b4f163F83f

0x711cd20bF6b436ced327A8C65A14491aA04c2ca1

0x460637bF4BbCE6Bbb28D4e0a620c070c697d936a

0xCFd2224BB2c479d1463ac9Db416c3D23BEdE8097

0x10A1ddb397051D4cfA7daBe04C865b823008008E

0xBBCcf6CaB5b3AEC26b0CbC6095b5b6DDBacfd59a  
  
All affected addresses were compensated.


Proof Links:
- [https://blog.alphafinance.io/mev-bots-uniswap-implicit-assumptions/](https://blog.alphafinance.io/mev-bots-uniswap-implicit-assumptions/)


