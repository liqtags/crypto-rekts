# Merlin Labs
![Merlin Labs](/rektimages/Merlin-Labs.png)
- Amount Lost: $680,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-5-26

The attacker:  
https://bscscan.com/address/0x400fa7edd10d480f034113f5e81bc1bb78c162fa  
  
The transaction behind the attack:  
https://bscscan.com/tx/0x8e20a1118a669d03b66c5eca2d937646bd855a998afb1e94b94ff6303456ff97  
  
The attacker:  
\- added a small sum of deposit to the LINK-BNB Vault at:  
https://bscscan.com/tx/0x3ce0be64e6daae35c8c5155d38148a2af3eaf8a9b26d5a8c4d7337dc86f475ac  
  
\- sent 180 CAKE to the LINK-BNB Vault contract (leads to the hack)  
  
\- called _getReward_ () with the deposit of LINK-BNB Vault from the first step  
  
\- with a large amount of CAKE token in the wallet balance of the vault contract (sent by the hacker in step 2), it returns a large amount of profit. As a result, the system minted 100 MERL as a reward to the hacker  
  
\- repeated 36 times, received 49K of MERL token in total  
  
\- swapped MERLIN token into 240 ETH and transferred out of BSC using Anyswap.  
  
The attack was performed using a similar way as Bunny and Autoshark exploits.


Proof Links:
- [https://watchpug.medium.com/merlin-lab-performance-fee-minting-incident-analysis-12571b591eb3](https://watchpug.medium.com/merlin-lab-performance-fee-minting-incident-analysis-12571b591eb3)
- [ https://rekt.news/merlinlabs-rekt/]( https://rekt.news/merlinlabs-rekt/)


