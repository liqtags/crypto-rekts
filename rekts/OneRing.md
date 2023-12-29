# OneRing
![OneRing](/rektimages/OneRing.png)
- Amount Lost: $1,508,300.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-3-21

The attacker's wallet:  
https://ftmscan.com/address/0x12efed3512ea7b76f79bcde4a387216c7bce905e  
  
The exploit contract:  
https://ftmscan.com/address/0x6a6d593ed7458b8213fa71f1adc4a9e5fd0b5a58  
  
The transaction behind the attack:  
https://ftmscan.com/tx/0xca8dd33850e29cf138c8382e17a19e77d7331b57c7a8451648788bbb26a70145  
  
The attack was enabled via a flash loan-assisted price manipulation of the LP tokens, which resulted in a greater quantity of OShare tokens being removed from the protocol.  
  
After the contract deployment, the hacker borrowed $80m USDC utilizing Solidly flash loans to boost the price of our underlying LP tokens in a single block, changing the price of OShare and driving a huge number of OShare tokens out of the protocol.  
  
Stolen funds were bridged to Ethereum and deposited into Tornado Cash mixer:  
https://etherscan.io/address/0x12efed3512ea7b76f79bcde4a387216c7bce905e


Proof Links:
- [https://medium.com/oneringfinance/onering-finance-exploit-post-mortem-after-oshare-hack-602a529db99b](https://medium.com/oneringfinance/onering-finance-exploit-post-mortem-after-oshare-hack-602a529db99b)
- [ https://twitter.com/peckshield/status/1506090607059431427]( https://twitter.com/peckshield/status/1506090607059431427)


