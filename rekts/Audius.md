# Audius
![Audius](/rektimages/Audius.png)
- Amount Lost: $1,086,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-7-23

**Quick Summary**

The Audius Platform got exploited by an attacker who passed a malicious proposal and voted it through by  himself. The attacker gained 18m $AUDIO token worth $6m USD but ultimately dumped the tokens in a single transaction for $1m USD.

  


 **Details of the Exploit**

Audius is a decentralized music streaming and sharing platform that aims to empower content creators.The attacker realized an exploitable vulnerability in Audius governance, staking and delegation contracts. Due to an inconsistent storage layout between contracts, the attacker was able to re-initialize the governance contracts and redirect the ownership of the community treasury to his wallet through the malicious proposal #85.

https://etherscan.io/tx/0x4227bca8ed4b8915c7eec0e14ad3748a88c4371d4176e716e8007249b9980dc9

The attacker proceeded and dumped the ill-gotten 18,5m $AUDIO token with a massive slippage of approx. 80% on Uniswap for $1m worth of $WETH instead of potentially $6m worth of $WETH that a slower approach might have yielded 

https://etherscan.io/tx/0x82fc23992c7433fffad0e28a1b8d11211dc4377de83e88088d79f24f4a3f28b3.

The attacker immediately started to launder the ill-gotten funds through Tornado.Cash https://etherscan.io/address/0xa0c7bd318d69424603cbf91e9969870f21b8ab4c.

  


The vulnerabilities have been patched by the team and the project has resumed to its operations.

  


  


  


 **Block Data Reference**

Attackers Addresses:

https://etherscan.io/address/0xa0c7bd318d69424603cbf91e9969870f21b8ab4c

Attacker smart contract used for draining the community treasury

https://etherscan.io/address/0xbdbb5945f252bc3466a319cdcc3ee8056bf2e569

  


Audius Community Treasury

https://etherscan.io/address/0x4deca517d6817b6510798b7328f2314d3003abac


Proof Links:
- [https://blog.audius.co/article/audius-governance-takeover-post-mortem-7-23-22](https://blog.audius.co/article/audius-governance-takeover-post-mortem-7-23-22)
- [ https://cointelegraph.com/news/hacker-drains-1-08m-from-audius-following-passing-of-malicious-proposal]( https://cointelegraph.com/news/hacker-drains-1-08m-from-audius-following-passing-of-malicious-proposal)
- [ https://cryptonews.com/news/decentralized-music-platform-audius-identifies-source-of-usd-6m-exploit-says-it-applied-a-patch.htm]( https://cryptonews.com/news/decentralized-music-platform-audius-identifies-source-of-usd-6m-exploit-says-it-applied-a-patch.htm)
- [ https://news.coincu.com/111560-audius-was-hacked-by-a-6-million-exploit/]( https://news.coincu.com/111560-audius-was-hacked-by-a-6-million-exploit/)


