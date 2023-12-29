# Pinecone Finance
![Pinecone Finance](/rektimages/Pinecone-Finance.png)
- Amount Lost: $200,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2021-8-18

The attackers' addresses:  
https://bscscan.com/address/0x472a2c88c1a5f794eb80706e587d4a120d9be255  
https://bscscan.com/address/0x430ad7e178d3e00145f35c041c7f486d7e8a4c7e  
https://bscscan.com/address/0xfc6682db7e9f57882e8b18ebc9adc7a19f770494  
  
The transaction behind the attack:  
https://bscscan.com/tx/0xe23ffa079edd975b5bd48503757040b7aa60e63d66972419fd56f4404c6d4da1  
  
The root cause is a false deposit bug in the staking logic of Pinecone finance. In particular, the affected vault counts as valid deposits even no tokens are actually transferred in. The hacker has no sufficient PCT balance but stakes 200K PCTs to the vault. However, the tx still succeeds and credits the hacker with 200K valid PCTs staked:  
https://bscscan.com/tx/0x10236426cbe9a6380b7990150013125a623784ed1002fe3e34d07ff89ffa2619  
  
Overall, three hackers gathered 3.5 million PCTs, which were converted into 516.83 BNB (~$200,000).


Proof Links:
- [https://medium.com/@PineconeFinance/post-mortem-of-pct-staking-vault-attack-714e1171e121](https://medium.com/@PineconeFinance/post-mortem-of-pct-staking-vault-attack-714e1171e121)


