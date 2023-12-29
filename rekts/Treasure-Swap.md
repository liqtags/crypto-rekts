# Treasure Swap
![Treasure Swap](/rektimages/Treasure-Swap.png)
- Amount Lost: $1,100,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-6-10

**Quick Summary**

The Treasure Swap project has been exploited by hackers. Using the vulnerability, the hacker needed only 1 wei to exchange all the $WETH tokens in the transaction pool.

 **  
Details of the Exploit**

Treasure Swap is a donation protocol driven by the community to build a sustainable DAO.

The hacker noticed a vulnerability in the Treasure Swap contract, where in the swap _ _ function the check for the **k** -value of the constant formula **k = a * b** , which determines the price of the token (A) in the token (B), was skipped. The hacker noticed this vulnerability, deployed his malicious contracts on the network with which he began to steal the $WETH reserves from the protocol.

Example transactions of the exploit:

1) https://bscscan.com/tx/0x13285cc0397d529d81b70e1736c81b73c585532d6290803f0f371e2f9beba0c3

2) https://bscscan.com/tx/0x90a8e176537782ac64c672b0140133974873e92eafef835bdf2d6f2fd180c92d

3) https://bscscan.com/tx/0x0b13710aebdc2fa7655a511655cac84ae9ae8a93a778d7628fd7f0b21afc219c

All stolen $BNB are still held on the hacker's wallet.

  


 **Block Data Reference**

Hacker address: https://bscscan.com/address/0x0FaCB17eFCb6cA6Ff66f272DE6B306DE9fb5931D

  


Vulnerable contract addresses: 

1) https://bscscan.com/address/0xe26e436084348edc0d5c7244903dd2cd2c560f88

2) https://bscscan.com/address/0x96f6eb307dcb0225474adf7ed3af58d079a65ec9

  


Malicious contract addresses:

1) https://bscscan.com/address/0xd53826f2c10b116990507d35f7b9fe4461651fba

2) https://bscscan.com/address/0x5baa2e6b84c2bd1871e147983bc57fa90bdce376

3) https://bscscan.com/address/0xd14c71b8f1b9576e0560273c764e289f593c2016



