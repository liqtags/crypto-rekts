# Defrost Finance
![Defrost Finance](/rektimages/Defrost-Finance.png)
- Amount Lost: $12,000,000.00
- Funds Returned: $12,000,000.00
- Category: Stablecoin
- Date: 2022-12-23

**Quick Summary**

Defrost has been hacked with losses reaching $12M. The protocol’s V1 and V2 have been affected.

There are suspects the attack was an insider job.

  


 **Details of the Exploit**

On December 23th 2022, Defrost reported they had been exploited due to missing reentarncy lock in flashloan() and deposit() functions. As a result, the share price of LSWUSDC was manipilated and approximately $173K were gained by the attacker.

Later on, it was revealed that the protocol’s vaults have been exploited as well: a fake collateral token was added, and though calling the setOracleAddress() function, the price oracle was replaced with a malicious one leading to liquidations of user collaterals in Defrost’s vaults. The loss estimation is $12M.

  


The risk of user funds liquidations in case of replacing oracle to a malicious one was reported by Defiyield in its audit: 

https://defiyield.app/audit-database/defiyield/defrost_finance  

 

 **Block Data Reference**

The attacker address:

[https://snowtrace.io/address/0x7373dca267bdc623dfba228696c9d4e8234469f6](https://snowtrace.io/address/0x7373dca267bdc623dfba228696c9d4e8234469f6)

 

The exploit transaction:

[https://snowtrace.io/tx/0xc6fb8217e45870a93c25e2098f54f6e3b24674a3083c30664867de474bf0212d](https://snowtrace.io/tx/0xc6fb8217e45870a93c25e2098f54f6e3b24674a3083c30664867de474bf0212d) 

 

An example transaction of the oracle replacement: 

[https://snowtrace.io/tx/0x34eb46f498c418285323e6e146ae84ea836e49822fa254c865f59d650261c3dd](https://snowtrace.io/tx/0x34eb46f498c418285323e6e146ae84ea836e49822fa254c865f59d650261c3dd) 

 

 **UPD**

On December 26th, the Defrost team reported the stolen funds had been returned, and they are going to check onchain what users have been affected in order to send them their funds back. 


Proof Links:
- [https://twitter.com/PeckShieldAlert/status/1606276020276891650?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1606276020276891650%7Ctwgr%5E4575898ef4f70ea1616a69679701b17c45a2f36f%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcryptoslate.com%2Fdefrost-finance-says-it-has-recovered-lost-funds-worth-12-million-from-hacker%2F](https://twitter.com/PeckShieldAlert/status/1606276020276891650?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1606276020276891650%7Ctwgr%5E4575898ef4f70ea1616a69679701b17c45a2f36f%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcryptoslate.com%2Fdefrost-finance-says-it-has-recovered-lost-funds-worth-12-million-from-hacker%2F)
- [ https://twitter.com/peckshield/status/1606767457099993088]( https://twitter.com/peckshield/status/1606767457099993088)


