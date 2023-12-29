# KLAYswap
![KLAYswap](/rektimages/KLAYswap.png)
- Amount Lost: $1,900,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-2-3

**Quick Summary**

Exploiters have stolen $1.9m from South Korean cryptocurrency platform KLAYswap using a Border Gateway Protocol (BGP).

  


 **Details of the Exploit**

According to reports, the attackers used a Border Gateway Protocol (BGP) hijack to manipulate the network flow and configure it in a way that allowed users connected to KLAYswap to download malicious code from the server sent by the attackers instead of the normal software development kit file or KakaoTalk.

  


When a token-related function was executed through the KLAYswap UI on February 3, the researchers found that a malicious external attack occurred due to the infection of SDK files from external sites, which did not originate from KLAYswap's own front-end source code. Instead, the user's normal Kakao SDK JavaScript file request was connected to a third-party server built by the attacker, which was not a Kakao server, that led to an incident in which malicious code files were downloaded.

  


The malicious JavaScript allowed the attackers to intercept funds as a user-initiated transaction. Over a two-hour period, the hackers stole cryptocurrency totaling 2.2 billion won (about $1.9 million) from 407 abnormal transactions from 325 customer wallets.

  


The attackers changed all transaction requests of users to either directly send or approve the user's token to their contract and load it on the KLAYswap site. By changing the Kakao SDK script, the malicious code was created in the form of interfering with the operation of the existing KLAYswap code and allowing its own code to be executed. If a transaction occurred with corrupted logic, the user's assets were approved for use or the assets were transferred directly to the attacker's address.

  


KLAYswap developers say they blocked all functions of KLAYswap and performed an emergency check to prevent further damage after the incident was identified. They also restricted the operation of Klaytn minter, a blockchain platform in the bridge, to prevent the transfer of stolen assets to other exchange platforms through the Orbit Bridge.

  


South Korean cybersecurity firm S2W analyzed the attack and found that the malicious code was distributed only to users who accessed it through KLAYswap by checking the referrer value of the HTTP header when connecting. Other users received a server-side error.

  


  



Proof Links:
- [https://www.bankinfosecurity.asia/crypto-exchange-klayswap-loses-19m-after-bgp-hijack-a-18518](https://www.bankinfosecurity.asia/crypto-exchange-klayswap-loses-19m-after-bgp-hijack-a-18518)
- [ https://medium.com/klayswap/klayswap-incident-report-feb-03-2022-70ff124aed6b]( https://medium.com/klayswap/klayswap-incident-report-feb-03-2022-70ff124aed6b)


