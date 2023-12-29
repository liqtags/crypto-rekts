# ElasticSwap
![ElasticSwap](/rektimages/ElasticSwap.png)
- Amount Lost: $850,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-13

**Quick Summary**

On the 13th of December, 2022, Elastic Swap was hacked on the Avalanche and Ethereum Chain using a calculation issue. The malicious actor stole worth around 850k USD.

  


 **Details of the Exploit**

The attack was possible in the reason of using two different logic of calculation in the exploited smart contracts. Functions addLiquidity and removeLiquidity have different logic of accounting. While the first one uses constant variables the second one is using dynamic pool balance calculation. This led to the possibility of price manipulation after the pool unbalancing.

  


 **Block Data Reference**

 **Avalanche:**

Attacker address:

https://snowtrace.io/address/0x3bdf01ed32f07e8e843163b5d478d4502f5743cd

https://snowtrace.io/address/0x25fde76a52d01c83e31d2d3d5e1d2011ff103c56

https://snowtrace.io/address/0xdd8429b85a92b35712659bd945462a41bfd60cbd

  


Exploit tx:

https://snowtrace.io/tx/0x782b2410fcc9449ead554a81f78184b6f9cca89f07ea346bc50cf11887cd9b18

  


 **Ethereum:**

Exploit tx:

https://etherscan.io/tx/0xc2d86035f20389088b4277de6f13ca3f8bb819381b95e58359a22d0ad6f5cbda

Front-run tx:

https://t.co/YGMaRQj6Lk


Proof Links:
- [https://twitter.com/BlockSecTeam/status/1602848642066366466](https://twitter.com/BlockSecTeam/status/1602848642066366466)
- [ https://blog.solidityscan.com/elasticswap-hack-analysis-erroneous-calculations-bug-8dac10fb1b98https://quillaudits.medium.com/decoding-elastic-swaps-850k-exploit-quillaudits-9ceb7fcd8d1a]( https://blog.solidityscan.com/elasticswap-hack-analysis-erroneous-calculations-bug-8dac10fb1b98https://quillaudits.medium.com/decoding-elastic-swaps-850k-exploit-quillaudits-9ceb7fcd8d1a)


