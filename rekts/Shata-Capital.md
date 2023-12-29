# Shata Capital
![Shata Capital](/rektimages/Shata-Capital.png)
- Amount Lost: $5,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-2-24

**Quick Summary**

USDC vault owned by Shata Capital was exploited for about of 5M USD.

  


 **Details of the Exploit**

On February 24, 2023, an exploit was discovered in Shata Capital's EFVault contract, resulting in approximately $5.14 million in losses due to improper configuration after contract upgrade.

  


The attacker's address was 0xa0959536560776ef8627da14c6e8c91e2c743a0a and the attacked contract was 0x80cB73074A6965F60DF59BF8fA3CE398Ffa2702c.

  


The attacker initially deposited 0.1 Ether to the EFVault contract 27 days prior to the attack to get a number of shares.

  


The EFVault contract had been upgraded by proxy before the attack, and the key parameter of the new function redeem in the upgraded contract was directly assigned by reading the wrong value from the corresponding storage location of the agent contract before the upgrade.

  


This resulted in an excessive amount of user withdrawable assets calculated in the redeem function, allowing the hacker to exploit this vulnerability and call the redeem function twice, profiting $3.43 million and $1.71 million respectively.

  


The vulnerability occurred because the initialize function of the newly implemented contract could not be called again after the upgrade, making it impossible to initialize the new variables.

  


In addition, the data storage structure of the old version was not taken into account when adding new variables in the new contract, which resulted in the new contract still reading the data of the proxy contract slot of 0xcc when reading the assetDecimal variable.

  


Through querying the transactions, it was found that the value of maxDeposit can be set by calling the setMaxDeposit function, and the latest value of maxDeposit was set to 5000000000000.

  


The attacker has exchanged all funds to ETH and transferred to tornado.cash.

  


 **Block Data Reference**

Exploit TXs:

https://etherscan.io/tx/0x1fe5a53405d00ce2f3e15b214c7486c69cbc5bf165cf9596e86f797f62e81914

https://etherscan.io/tx/0x31565843d565ecab7ab65965d180e45a99d4718fa192c2f2221410f65ea03743

  


Exploiter:

https://etherscan.io/address/0xa0959536560776ef8627da14c6e8c91e2c743a0a

  


Attacker contract:

https://etherscan.io/address/0x80cB73074A6965F60DF59BF8fA3CE398Ffa2702c


Proof Links:
- [https://twitter.com/CertiKAlert/status/1630508983604633602?s=20](https://twitter.com/CertiKAlert/status/1630508983604633602?s=20)
- [ https://twitter.com/peckshield/status/1630490333716029440?lang=en]( https://twitter.com/peckshield/status/1630490333716029440?lang=en)
- [ https://medium.com/@Triathon/how-to-attack-shata-capital-contract-to-pirate-over-5-1-million-bd89660e9a71]( https://medium.com/@Triathon/how-to-attack-shata-capital-contract-to-pirate-over-5-1-million-bd89660e9a71)


