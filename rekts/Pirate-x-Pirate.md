# Pirate x Pirate
![Pirate x Pirate](/rektimages/Pirate-x-Pirate.png)
- Amount Lost: $78,000.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-3-9

**Quick Summary**

Pirate X staking contract was attacked resulting in the loss of 9,681,000 PXP tokens, which were later dumped into the market, netting the attacker a profit of about 212 BNB.

  


 **Details of the Exploit**

The attack on Pirate X's staking contract is believed to have been due to the leakage of the private key, as the attacker used a valid signed message to launch the attack. Users who deposited their PXP tokens into the contract had their tokens transferred to an EOA account (0x3b74a9cb5f1399b4a5a02559e67da37d450067b7). The contract would then call transferFrom to transfer the tokens back to the user upon withdrawal. The attacker provided a valid sign from the external signer (0x7435e0e4c4d10988e8821dc4853d1db2eceb176d) and withdrew 9,681,000 PXP tokens.

  


 **Block Data Reference**

The staking contract: 0x6912B19401913F1bd5020b3f59EE986c5792DA54

Attacker: 0x3b74a9cb5f1399b4a5a02559e67da37d450067b7 

External signer: 0x7435e0e4c4d10988e8821dc4853d1db2eceb176d.


Proof Links:
- [https://twitter.com/BlockSecTeam/status/1501474711599198211?s=20](https://twitter.com/BlockSecTeam/status/1501474711599198211?s=20)


