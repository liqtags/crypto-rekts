# Spartan Protocol
![Spartan Protocol](/rektimages/Spartan-Protocol.png)
- Amount Lost: $30,500,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-5-2

**Quick Summary**

Spartan Protocol was exploited due to a flawed liquidity share calculation in the protocol, allowing the attacker to drain funds from the pool.

  


 **Details of the Exploit**

The attacker initiated the exploit by taking a flash loan of 10K WBNB. They then repeatedly swapped WBNB for SPARTA, inflated the asset balance in the pool, and burned pool tokens to withdraw liquidity. This process was repeated multiple times, draining substantial funds from the pool. The attacker then returned the flash loan with a fee of 260 WBNB. The stolen funds were swapped to BTCB or BETH using 1inch and Spartan, and then to Anyswap versions using Nerve. The attacker was able to withdraw part of the profit through Anyswap.

  


Stolen funds:

\- 2,643,882.074112804607308497 SPARTA

\- 21,555.69728926154636986 WBNB

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/address/0x3b6e77722e2bbe97c1cfa337b42c0939aeb83671

The transaction behind the attack:

https://bscscan.com/tx/0xb64ae25b0d836c25d115a9368319902c972a0215bd108ae17b1b9617dfb93af8


Proof Links:
- [https://spartanprotocol.medium.com/today-spartan-protocol-was-subject-to-an-exploit-targeting-the-liquidity-pools-8589b2069cef](https://spartanprotocol.medium.com/today-spartan-protocol-was-subject-to-an-exploit-targeting-the-liquidity-pools-8589b2069cef)
- [ https://rekt.news/spartan-rekt/]( https://rekt.news/spartan-rekt/)
- [ https://peckshield-94632.medium.com/the-spartan-incident-root-cause-analysis-b14135d3415f]( https://peckshield-94632.medium.com/the-spartan-incident-root-cause-analysis-b14135d3415f)
- [ https://twitter.com/FrankResearcher/status/1388848787632754690?s=20]( https://twitter.com/FrankResearcher/status/1388848787632754690?s=20)


