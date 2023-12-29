# Eco DeFi
![Eco DeFi](/rektimages/Eco-DeFi.png)
- Amount Lost: $794,041.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-12-28

The attacker:  
\- swapped 0.02 WBNB to 12.368 XRP  
  
\- deposited 12.368 XRP to the pool 0xc406  
https://bscscan.com/address/0xc4068f463d9cb722b936e0194847ab3a86de4dab  
  
\- minted 60,975,194,844 eXRP share tokens  
  
\- set admin ( _newAdmin_ ()) in Unitroller contract (0x6f5edd47b34ceb6506c85c15108b12b3c2cf919e) to the malicious contract (0x8043bfe3793597f6e74cebe495b471c27f80a179)  
  
\- new owner called _setPriceOracle_ () and changed oracle address from 0xf074b445e3b5858eea1e58fe5fe716ae33b69528 to malicious one  
0x8043bfe3793597f6e74cebe495b471c27f80a179  
  
\- wrong oracle data allowed withdrawing all assets from the pool:  
69,940.838139881955983638 ($69,530.01) (BSC-US...)  
57,211.335292168881759699 ($57,182.27)  (USDC)  
46,906.146588682998823308 ($46,845.31)  (BUSD)  
335,725.42257116669113152 ($286,829.58)  (VAI)  
13.280051065798373675 ($51,503.49)  (ETH)  
0.581669136989633591 ($28,460.35)  (BTCB)  
244.082029656114025206 ($133,271.00)  (WBNB)  
268.860558650762202142  (SOL)  
3,279.711492555105148787 ($52,392.89)  (XVS)  
5,614.98460021139519757 ($69,977.67)  (Cake)  
99,994,616.089438012  (JOJO)  
  
Stolen funds are held at the following address:  
https://bscscan.com/address/0x68926c8595b211bd8effd9ffee7355426cdd4ce8


Proof Links:
- [https://twitter.com/peckshield/status/1475805663544877058](https://twitter.com/peckshield/status/1475805663544877058)


