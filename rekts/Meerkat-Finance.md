# Meerkat Finance
![Meerkat Finance](/rektimages/Meerkat-Finance.png)
- Amount Lost: $30,883,780.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-3-4

**Quick Summary**

Meerkat Finance was allegedly rug-pulled by its team or an external attacker for the amount of $31 million through proxy upgradable smart contracts.

  


 **Details of the Exploit**

Meerkat Finance was a fork of the successful Alpaca Finance project. Essentially, Meerkat Finance was a lending and yield aggregation protocol offering its users yield through lending assets or pledging assets to the platform's vaults. The vaults would pursuit automated investment strategies.

This rekt case gained traction when the contract deployer invoked the _upgradeTo_ () function, setting new implementation to the BUSD Vault at:  
https://bscscan.com/tx/0xf19fa4bcff4adaebeddd28c851458ba0f01ffedd52b62df56ace94e7c8842553  
The contract deployer also invoked the _upgradeTo_ () function, setting new implementation to WBNB Vault at:  
https://bscscan.com/tx/0x063970f8625f250101a7da8abf914748cf8eaaaa9458041f1928501accfe5  
  
This altered the vault logic, introducing two new functions that were not included in the earlier implementations. This is where the real danger of proxy upgradable smart contracts lies. Code is king in DeFi and rather than trusting mediators users of DeFi can trust the code. However, when the code becomes changeable and upgradable by a centralized entity without governance by the token holder, the story changes.  
  
An external address, marked as Fake_Phishing 17, invoked _init_ () function to the Vaults through the proxy contract at:  
https://bscscan.com/tx/0xfcf48681e382e9f9cc1d6a64ff30487306f6b869924c6594075fcc86b3b21f5d  
https://bscscan.com/tx/0x5050d0f2f2d4d8ea76b04f25b1ee04b04d2b7beb6dafc6921672eaa448345027  
  
According to decompiled bytecode, this function sets the address on storage slot 0 to the address provided to the function. There’s no permission check, making this newly added function the backdoor into the vaults.  
  
The attacker called method _0x70fcb0a7_ on BUSD Vault to transfer out 13,968,039 BUSD at:  
https://bscscan.com/tx/0x1332fadcc5378b1cc90159e603b99e0b73ad992b1e6389e012af3872c8cae27d  
  
The attacker called method _0x70fcb0a7_ on WBNB Vault to transfer out 73,635 WBNB at:  
https://bscscan.com/tx/0xd8145dfe255a671428b9c082a006a145fe58d82175671e8bfbe02f4040ae8cd0

  


 **Block Data Reference**

BUSD Vault:

https://bscscan.com/address/0x7e0c621ea9f7afd5b86a50b0942eaee68b04a61c

BNB Vault:

https://bscscan.com/address/0x639f18c72b6a017bdd209c161d1617c9481a1e4d

External Hacker Address (Fake_Phishing 17):

https://bscscan.com/address/0x9542966f1114eaa5859201aa8d34358bfedbfa79


Proof Links:
- [https://rekt.news/meerkat-finance-bsc-rekt/](https://rekt.news/meerkat-finance-bsc-rekt/)
- [ https://www.theblockcrypto.com/linked/97082/rug-pull-defi-meerkat-31-million]( https://www.theblockcrypto.com/linked/97082/rug-pull-defi-meerkat-31-million)
- []()


