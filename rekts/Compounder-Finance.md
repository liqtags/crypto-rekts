# Compounder Finance
![Compounder Finance](/rektimages/Compounder-Finance.png)
- Amount Lost: $12,326,985.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2020-12-1

**Quick Summary**

Contract deployer exploited StrategyController smart contract, transferring funds to his wallet and hiding traces using Tornado Cash mixer.

  


 **Details of the Exploit**

The contract deployer exploited the StrategyController smart contract by invoking the inCaseTokensGetStuck() function. This allowed him to transfer funds directly into his wallet. The exploit was carried out in several transactions. After acquiring the funds, the attacker used the Tornado Cash mixer to hide the traces of the stolen funds. This method of obscuring the origin of funds makes it difficult to track the attacker.

  


 **Block Data Reference**

Malicious Transactions:

https://etherscan.io/tx/0x57c61df91e46b191424bfdd9223f277457a07999b58420e3b540059aad3fc7fe

https://etherscan.io/tx/0x10d245e61e76c7bf44257985789463ed89f624a0d5ffc45cfa671b16a7113d77

https://etherscan.io/tx/0x0763afe207015ed7c1aa8858d2c092cf7b6a20397f2408bff20b044ef1901822

https://etherscan.io/tx/0xf94de5a083f16700f4d26ec8ca3e03dc01889a54f472bf630079c54a77f033e6

https://etherscan.io/tx/0x18e0efcaabe64299666fd78bb33dae2a4b25c6f11b469fc0498db714970cacfa

https://etherscan.io/tx/0x744c51b4544c76be384197a8c089271dfcbd207d67bad6d2f8907dd7d4d852e5

https://etherscan.io/tx/0x9c75f70670d94e6d37f60a585f9b57d13193998d64866f720489efbea4809056

  


Tornado Cash Mixer Transaction:

https://bloxy.info/txs/calls_from/0x079667f4f7a0b440ad35ebd780efd216751f0758?signature_id=11062&smart_contract_address_bin=0xa160cdab225685da1d56aa342ad8841c3b53f291


Proof Links:
- [https://twitter.com/CryptoCatVC/status/1333690462402732034](https://twitter.com/CryptoCatVC/status/1333690462402732034)
- [ https://twitter.com/defiyield_app/status/1333731633393004545]( https://twitter.com/defiyield_app/status/1333731633393004545)
- [ https://rekt.news/deathbed-confessions-c3pr/]( https://rekt.news/deathbed-confessions-c3pr/)


