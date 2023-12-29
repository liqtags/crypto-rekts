# Fortress Loans
![Fortress Loans](/rektimages/Fortress-Loans.png)
- Amount Lost: $2,976,004.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-5-8

**Quick Summary**

Fortress Loans was attacked due to oracle vulnerability. An attacker was able to manipulate the project's oracle which allowed them to borrow differrent number of tokens for the amount of ~$3m (~1k ETH and 400k DAI).

  


 **Details of the Exploit**

Fortress Protocol is a decentralized marketplace for Lenders and Borrowers with Borderless Stablecoins. Fortress Loans became a victim of attacker that manipulate with the price oracle, which made possible to get about $3m and launder them through the TornadoCache.

  


Attack flow:

Attacker created unverified smart-contract (https://bscscan.com/tx/0x4800928c95db2fc877f8ba3e5a41e208231dc97812b0174e75e26cca38af5039) which was later used to send a series of transactions (https://bscscan.com/tx/0x13d19809b19ac512da6d110764caee75e2157ea62cb70937c8d9471afcb061bf).  


A series of transactions allowed them to propose Fortress Governor Alfa contract with a malicious proposal, for which they themselves voted to set the FTS extremely valuable. The attacker then borrowed a huge amount of tokens that exchanged for ETH and DAI. Then all stollen funds were transferred across the bridge to the Ethereum network and laundered via TornadoCache.

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Attacker address on BSC: https://bscscan.com/address/0xA6AF2872176320015f8ddB2ba013B38Cb35d22Ad 

Attacker address on ETH. Here all the stolen funds were laundered through TornadoCache: https://etherscan.io/address/0xA6AF2872176320015f8ddB2ba013B38Cb35d22Ad

  


Bridging transaction from BSC to ETH:

BSC: https://bscscan.com/tx/0x36fd458defec69875a1908a464c09f59899abaf09350059ce7f75b9c1a7e9eea

ETH: https://etherscan.io/tx/0xcf852b0231e2c5a2361cbd71cb0288bc6a0e460925e1efe9054f7d4f5b543af5

  


Attacker's smart-contract (BSC): https://bscscan.com/address/0xcd337b920678cf35143322ab31ab8977c3463a45

  


Attack transaction: https://bscscan.com/tx/0x13d19809b19ac512da6d110764caee75e2157ea62cb70937c8d9471afcb061bf


Proof Links:
- [https://www.certik.com/resources/blog/k6eZOpnK5Kdde7RfHBZgw-fortress-loans-exploit](https://www.certik.com/resources/blog/k6eZOpnK5Kdde7RfHBZgw-fortress-loans-exploit)


