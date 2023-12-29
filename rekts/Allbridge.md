# Allbridge
![Allbridge](/rektimages/Allbridge.png)
- Amount Lost: $570,000.00
- Funds Returned: $465,000.00
- Category: Bridge
- Date: 2023-4-1

**Quick Summary**  

On April 1, 2023, a flash loan attack was executed on Allbridge's pool in BSC networks, leading to a loss of around $570K due to a flawed pricing calculation logic.

  


 **Details of the Exploit**  

The attacker obtained a flash loan of $7.5M BUSD from PancakeSwap and swapped $2M BUSD for $2M BSC-USD into the pool. They then moved $5M BUSD into another pool, exchanged it for its BSC-USD equivalent, and converted the $5M BSC-USD to its $BUSD equivalent. The attacker then transferred the funds to Allbridge's bridge contract, resulting in substantial profits. By switching the pool balance, the liquidity pool balance was destroyed, and the pool's liquidity was reduced to $40,000 in balance BUSD. The attacker used $40,000 of BUSD to exchange $790,000 of BSC-USD from Bridge due to broken logic, and finally leveraged Tornado cash to transfer $570,000 in BUSD to their wallet address.

  


 **Block Data Reference**

Exploit tx:

https://bscscan.com/tx/0x7ff1364c3b3b296b411965339ed956da5d17058f3164425ce800d64f1aef8210

Attackers:

https://bscscan.com/address/0x2b3cff12c02625518deb0af14684999fb6e3e360

https://bscscan.com/address/0xc578d755cd56255d3ff6e92e1b6371ba945e3984


Proof Links:
- [https://twitter.com/peckshield/status/1642356701100916736?s=46&t=DefKAWsE5N91p9nzDiwo6A](https://twitter.com/peckshield/status/1642356701100916736?s=46&t=DefKAWsE5N91p9nzDiwo6A)
- [ https://twitter.com/AnciliaInc/status/1642334803478581248?s=20]( https://twitter.com/AnciliaInc/status/1642334803478581248?s=20)


