# MAD
![MAD](/rektimages/MAD.png)
- Amount Lost: $122,354.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-6-29

**Quick Summary**

The $MAD token was stolen by a hacker who noticed a vulnerability in the contract that held most of the assets. The hacker withdrew the profit through Tornado.cash.

  


 **Details of the Exploit**

Token $MAD had been stolen from the token storage due to the lack of specific verification, as a result, anyone could pick up tokens, knowing how to interact with the function. The contract is unverified, so the function looks like "0x9763a894". The hacker stole the tokens, and called _selfdestruct_ in this transaction: https://bscscan.com/tx/0xbaf42be5ad9a6b259fa7bf6219f3672e5afda267219dddabd82d31b82808ab59

Then, using another contract, he took the tokens from all the addresses where the tokens from the previous transaction were sent and swapped them to $BSC-USD via PancakeSwap: https://bscscan.com/tx/0xbaf42be5ad9a6b259fa7bf6219f3672e5afda267219dddabd82d31b82808ab59.

Which were subsequently sent to the main address from which the money was withdrawn via Tornado.cash:

https://bscscan.com/tx/0x39ddbe914af0abd9f4f1429f5aa47561e1da8223ada43100755c3ea6d6114def

  


 **Block Data Reference**

Token creator address: https://bscscan.com/address/0x963fc5af34b5dfac05491620122ed12f3634a2ec

Token contract: https://bscscan.com/address/0x525c8e9c8240a55014bc55cbe8908eadadb02094

Vulnerable storage contract: https://bscscan.com/address/0x19b9c6984a6B545407d83C8Ec421D7D00695BaD8

  


Attacker addresses: https://bscscan.com/address/0x957e949afa38011947a76d871c66f13af11eae93

Attacker contract addresses: 

1) https://bscscan.com/address/0xe6016d18c0cf515f4cda8b38907617bd370e6819

2) https://bscscan.com/address/0x2002c47eca93e3873ea1fa4f797bb6ca9c0d7f28


Proof Links:
- [https://dexscreener.com/bsc/0x1515937e02c7a84b11dfdc22219c754ae415c297](https://dexscreener.com/bsc/0x1515937e02c7a84b11dfdc22219c754ae415c297)


