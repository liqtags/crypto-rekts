# Lodestar Finance
![Lodestar Finance](/rektimages/Lodestar-Finance.png)
- Amount Lost: $5,800,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-12-10

**Quick Summary**

Lodestar protocol was exploited via price feed oracle vulnerability. plvGLP price was manipulated which led to the protocol liquidity draining.

  


 **Details of the Exploit**

Lodestar Finance is a borrowing and lending protocol, based on the Compound fork, initially built and launched on the Arbitrum network. Lodestar aims to bring the critical DeFi primitive of decentralized money markets to Arbitrum communities. The protocol was exploited by manipulating the plvGLP oracle price using flashloans to create a large plvGLP collateral position. The attacker increased the plvGLP/GLP rate and created the ability to change the price immediately, which was then compounded through the loops and led to significant borrowing ability. The main vulnerability that allowed such exploit flow was in GLPOracle price logic. 

  


 **Block Data Reference**

Attacker contract:

https://arbiscan.io/address/0x7596ACadf6c93f01b877F5A44b49407ffFC53508

  


Attacker  address:

https://arbiscan.io/address/0xc29d94386ff784006ff8461c170d1953cc9e2b5c

  


Exploit TX:

https://arbiscan.io/tx/0xc523c6307b025ebd9aef155ba792d1ba18d5d83f97c7a846f267d3d9a3004e8c


Proof Links:
- [https://twitter.com/LodestarFinance/status/1601686921566375936](https://twitter.com/LodestarFinance/status/1601686921566375936)
- [ https://twitter.com/BowTiedPickle/status/1601657332227657728]( https://twitter.com/BowTiedPickle/status/1601657332227657728)
- [ https://twitter.com/CertiKAlert/status/1601855328366346242]( https://twitter.com/CertiKAlert/status/1601855328366346242)


