# Ola.finance
![Ola.finance](/rektimages/Ola.finance.png)
- Amount Lost: $3,600,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-3-31

The attacker's address:  
https://explorer.fuse.io/address/0x371D7C9e4464576D45f11b27Cf88578983D63d75/transactions  
  
The example transaction behind the exploit:  
https://explorer.fuse.io/tx/0x1b3e06b6b310886dfd90a5df8ddbaf515750eda7126cf5f69874e92761b1dc90/token-transfers  
  
The hack is made possible by the incompatibility between the Compound fork and ERC677/ERC777-based tokens, which have the built-in callback functions exploited to allow for reentry in _doTransferOut_ () function and draining of the loan pool.  
  
The attacker was initially funded by Tornado in Ethereum:  
https://etherscan.io/tx/0x98c46fc95b196ca35b2acb2e02bb9b6901df6a9a2e356629e9cbb42017a24efb  
  
After the exploit execution, funds were delivered back into Ethereum and transferred to the following wallet:  
https://etherscan.io/address/0xbcdb800d77ccaac6597830b026d6af78a1118f42


Proof Links:
- [https://twitter.com/ola_finance/status/1509431464521256961](https://twitter.com/ola_finance/status/1509431464521256961)
- [ https://twitter.com/peckshield/status/1509431646818234369]( https://twitter.com/peckshield/status/1509431646818234369)


