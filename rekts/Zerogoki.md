# Zerogoki
![Zerogoki](/rektimages/Zerogoki.png)
- Amount Lost: $670,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-8-8

Zerogoki was attacked by way of compromising the price oracle. The attacker provided a price oracle signed by legitimate private keys, which contained a crafted number of tokens to be swapped. However, the reason why the attacker could construct a valid signature is unknown.  
  
The attacker's address:  
https://etherscan.io/address/0xaef46df5efe3173f17b878f3345cf6e79c30680d  
  
The transaction behind the attack:  
https://etherscan.io/tx/0x81e5f7158b7ef59f45864e34375bd52bb8227f51ef970fe07ec2abf1d421acf8  
  
In the attack transaction, the attacker constructed a message that contained valid signatures and passed a crafted ns parameter (which contains a large number of zUSD). As a result, the attacker used 300 REI to swap 700k zUSD.  
  
Three addresses that are collated with the signatures are:

0x0d93A21b4A971dF713CfC057e43F5D230E76261C

0x3054e19707447800f0666ba274a249fc9a67aa4a

0x4448993f493b1d8d9ed51f22f1d30b9b4377dfd2


Proof Links:
- [https://blocksecteam.medium.com/the-analysis-of-the-zerogoki-attack-da4e0807b184](https://blocksecteam.medium.com/the-analysis-of-the-zerogoki-attack-da4e0807b184)


