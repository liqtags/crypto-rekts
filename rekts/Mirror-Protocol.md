# Mirror Protocol
![Mirror Protocol](/rektimages/Mirror-Protocol.png)
- Amount Lost: $90,000,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,Other
- Date: 2021-10-8

**Quick Summary**

Terra's Mirror Protocol was exploited for ~$90 million by a hacker. The attack went unnoticed for 7 months before a Terra community member called FatManTerra identified the exploit.

 **  
Details of the Exploit**

The Mirror Protocol was a synthetic assets protocol that allowed users to deposit USTC or LUNAC with a lockup period in order to mint synthetic stocks and commodities. The protocol allowed user to utilize both short and long strategies. The shorting functionality could only be accessed by locking funds for 14 days. The lock contract would then generate a position ID which was used in order to release the users funds if desired.

  


The attacker initially deposited 100,000 UST to the lock contract in this transaction:

https://finder.terra.money/classic/tx/29C9CFBBC9562100A5DB19D705E440CE24768D3BDE399507FA1C2EC2424413C4 in order to prepare the attack.

  


The attacker noticed that the lock contract had a vulnerability which allowed the attacker to unlock funds by using the same position ID over and over again as can be seen in this transaction: https://finder.terra.money/classic/tx/08DD2B70F6C2335D966342C20C1E495FD7A8872310B80BAF3450B942F79EBC1F, exploiting the protocol for approx. $90 million USTC in the process.

  


 **Block Data Reference**

Attacker address: https://finder.terra.money/mainnet/address/terra1200zm8crgjaj949ta8r7p6pay0qq638js4sdmh

  



Proof Links:
- [https://www.theblock.co/post/149342/a-90-million-defi-exploit-on-terra-went-unnot](https://www.theblock.co/post/149342/a-90-million-defi-exploit-on-terra-went-unnot)


