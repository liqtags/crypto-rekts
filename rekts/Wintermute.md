# Wintermute
![Wintermute](/rektimages/Wintermute.png)
- Amount Lost: $160,000,000.00
- Funds Returned: $0.00
- Category: CeFi,Yield Aggregator
- Date: 2022-9-20

**Quick Summary**

Wintermute's DeFi operations have been exploited for $160m in total according to the company's CEO.

  


 **Details of the Exploit**

Wintermute is an algorithmic market maker that provides liquidity across CeFi and DeFi exchanges as well as over-the-counter deals. Wintermute's CEO announced on the morning of the 20th of September that its DeFi operations had been hacked, CeFi and OTC services have not been affected. The company claims to be solvent despite $160m in assets taken and further states that 90 different assets were affected. Most of the assets taken were worth under $2,5m and therefore the markets should not be shaken by major sell-offs.

It appears that Wintermute had suffered a brute force private key compromise. The company used Profanity's services for generating vanity addresses. The private keys were generated in such a way that through using enough computing power every possible combination could be tried through until the code was hacked.

Several EOA addresses and two smart contracts have been used to attack the platform. 

The attacker gained power over Wintermute's wallet and repeatedly used a privileged function to transfer funds from the Wintermute wallet to his malicious smart contracts which then transferred the funds to the attackers EOA address, where the assets are sitting at the moment.

  


 **Block Data Reference**

Attacker EOA address:

https://etherscan.io/address/0xe74b28c2eAe8679e3cCc3a94d5d0dE83CCB84705

Attacker smart contracts:

https://etherscan.io/address/0x00000000ae347930bd1e7b0f35588b92280f9e75

https://etherscan.io/address/0x0248f752802b2cfb4373cc0c3bc3964429385c26

  


Transfer transactions:

https://etherscan.io/tx/0xedd31e2a949b7957a786d44b071dbe1bc5abd5c57e269edb9ec2bf1af30e9ec4

https://etherscan.io/tx/0xc253450fc3e0e124224aef2936c13b371a86056e82e778113fc3ce8800bbe876


Proof Links:
- [https://www.coindesk.com/business/2022/09/20/crypto-market-maker-wintermute-hacked-for-160m-says-ceo/](https://www.coindesk.com/business/2022/09/20/crypto-market-maker-wintermute-hacked-for-160m-says-ceo/)
- [ https://twitter.com/EvgenyGaevoy/status/1572134271011225601]( https://twitter.com/EvgenyGaevoy/status/1572134271011225601)
- [ https://www.certik.com/resources/blog/uGiY0j3hwOzQOMcDPGoz9-wintermute-hack]( https://www.certik.com/resources/blog/uGiY0j3hwOzQOMcDPGoz9-wintermute-hack)


