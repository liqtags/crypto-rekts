# Akropolis
![Akropolis](/rektimages/Akropolis.png)
- Amount Lost: $2,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2020-11-12

The attacker created a token contract with the malicious logic, which called deposit again (reentrancy):  
https://etherscan.io/address/0xe2307837524db8961c4541f943598654240bd62f  
  
The attacker:  
\- created a fake token  
  
\- deposited the fake token  
  
\- got a callback to the fake token, deposited 25k DAI  
  
\- got credited for 25k DAI of deposits  
  
\- got credited for 25k DAI of deposits  
  
\- withdrew 50k DAI  
  
The attacker address:  
https://etherscan.io/address/0xe2307837524db8961c4541f943598654240bd62f  
  
The stolen funds were transferred to some external wallet:  
https://etherscan.io/tx/0xf15623567231c67df2b8bcc5540236fbda2c3ac11ecbec427048f11b582cb869


Proof Links:
- [https://rekt.news/akropolis-rekt/](https://rekt.news/akropolis-rekt/)
- [ https://www.theblockcrypto.com/linked/84490/defi-project-akropolis-exploited-for-over-2-million]( https://www.theblockcrypto.com/linked/84490/defi-project-akropolis-exploited-for-over-2-million)


