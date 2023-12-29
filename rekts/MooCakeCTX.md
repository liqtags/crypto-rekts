# MooCakeCTX
![MooCakeCTX](/rektimages/MooCakeCTX.png)
- Amount Lost: $122,960.00
- Funds Returned: $0.00
- Category: Other,Token
- Date: 2022-11-6

**Quick Summary**

MooCakeCTX was exploited via a flash loan attack. The attacker's profit reached 122,960 $USD.

  


 **Details of the Exploit**

MooCakeCTX is a yield protocol on the Binance Chain. The protocol supports $CAKE deposits for $mooCakeCTX. The attacker took 400,000 $BUSD as a flash loan and exploited the protocol's smart contract for 424 $BNB. The attacker's malicious smart contract bypassed isContract() function check by performing actions on the constructor and got rewards as $mooCakeCTX tokens after depositing $CAKE tokens. The flash loan was paid back after repeating previous actions multiple times and the exploiter took a profit of 424 $BNB. All the stolen funds were transferred to several EOA addresses in 4 transactions.

  


 **Block Data Reference**

Attacker address:

https://bscscan.com/address/0x35700c4a7bd65048f01d6675f09d15771c0facd5

  


Malicious contract:

https://bscscan.com/address/0x71ac864f9388ebd8e55a3cdbc501d79c3810467c

  


Malicious transaction:

https://bscscan.com/tx/0x03d363462519029cf9a544d44046cad0c7e64c5fb1f2adf5dd5438a9a0d2ec8e

  


Funds transfer transactions:

https://bscscan.com/tx/0x963d1ff2fbb277376fb8a878e0275b63d861c0479a83ed2a3cf57573439cad6a

https://bscscan.com/tx/0x602c2220e4fa84cae5db564e08569327eeeb5de46d51f8033d2315f62787ba45

https://bscscan.com/tx/0x44922e9682f461cc669e3e72e4b9ff6202a49016920566625af15519f39ec913

https://bscscan.com/tx/0x58096e41e89f795bb409eebf9c28a2ee8b7025b6f6823a448421bbab74cca119


Proof Links:
- [https://twitter.com/beosinalert/status/1589501207181393920?s=46&t=g2I2FsjQ-Zz0DYHhJL009A](https://twitter.com/beosinalert/status/1589501207181393920?s=46&t=g2I2FsjQ-Zz0DYHhJL009A)


