# Shido Global
![Shido Global](/rektimages/Shido-Global.png)
- Amount Lost: $235,462.00
- Funds Returned: $0.00
- Category: Other
- Date: 2023-6-23

**Quick Summary**

Shido Global was exploited due to a smart contract configuration error, resulting in a loss of 235,458 $USD.

  


 **Details of the Exploit**

Shido Global, a Cosmos-based blockchain with EVM compatibility, was exploited due to a configuration error in the lock and claim mechanism, as well as the price difference between their old and new token pools in PancakeSwap. The attacker initially took a flash loan of 40 $BNB and swapped it to obtain a large amount of Shido tokens. Then, the attacker exploited a flaw in the ShidoLock contract that allowed them to convert v1 tokens to v2 tokens at a large scale. Finally, the exploiter swapped these tokens for 1,016 WBNB, repaid the flash loan, and made away with a profit of roughly 977 $BNB which is worth $235,458 USD. The stolen funds were transferred through Celer Bridge. 

  


 **Block Data Reference**

Attacker Address: 

https://bscscan.com/address/0x69810917928b80636178b1bb011c746efe61770d

  


Malicious Contract Address: 

https://bscscan.com/address/0xcdb3d057ca0cfdf630baf3f90e9045ddeb9ea4cc

  


Malicious Transaction: 

https://bscscan.com/tx/0x72f8dd2bcfe2c9fbf0d933678170417802ac8a0d8995ff9a56bfbabe3aa712d6

  


Bridging Transactions:

https://bscscan.com/tx/0x2de117d308f7f001bf3dad70cce6347c8cf26f254d7ee68cbf14370bc8c8c99f

https://bscscan.com/tx/0x2a1b7601f4a5960cca232e3d1abdca89a34b02948b79b59ac07f18edaacc69bb


Proof Links:
- [https://twitter.com/ShidoGlobal/status/1672436377735004162](https://twitter.com/ShidoGlobal/status/1672436377735004162)
- [ https://neptunemutual.com/blog/taking-a-closer-look-at-shido-exploit/]( https://neptunemutual.com/blog/taking-a-closer-look-at-shido-exploit/)
- [ https://twitter.com/AnciliaInc/status/1672382613473083393]( https://twitter.com/AnciliaInc/status/1672382613473083393)


