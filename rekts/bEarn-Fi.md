# bEarn Fi
![bEarn Fi](/rektimages/bEarn-Fi.png)
- Amount Lost: $11,000,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-5-16

**Quick Summary**

BvaultsBank was exploited through a flash loan attack, resulting in a loss of 8,016,006.09 BUSD.

  


 **Details of the Exploit**

The attacker initiated the exploit by borrowing a flash loan of 7,804,239.11 BUSD from CREAM. This was deposited into BvaultsBank and sent to the associated BvaultsStrategy strategy, then to Alpaca Vault for yield. The Alpaca Vault minted 7,598,066.58 ibBUSD back to BvaultsStrategy. The attacker then farmed with the received ibBUSD via the Alpaca FairLaunch. The attacker withdrew the BUSD from BvaultsBank, which was interpreted as withdrawing ibBUSD, equivalent to 8,016,006.09 BUSD. The attacker repeated these steps to accumulate credit and finally drained the pool. The flash loan was returned with 7,806,580.38 BUSD.

  


 **Block Data Reference**

The attacker's address:

https://bscscan.com/address/0x47f341d896b08daacb344d9021f955247e50d089

The transaction behind the attack:

https://bscscan.com/tx/0x603b2bbe2a7d0877b22531735ff686a7caad866f6c0435c37b7b49e4bfd9a36c


Proof Links:
- [https://rekt.news/bearn-rekt/](https://rekt.news/bearn-rekt/)
- [ https://peckshield.medium.com/bearn-fi-incident-inconsistent-asset-denomination-between-vault-strategy-9b24b68ab1c0]( https://peckshield.medium.com/bearn-fi-incident-inconsistent-asset-denomination-between-vault-strategy-9b24b68ab1c0)
- [ https://bearn-defi.medium.com/bvaults-busd-alpaca-strategy-exploit-post-mortem-and-bearn-s-compensation-plan-b0b38c3b5540]( https://bearn-defi.medium.com/bvaults-busd-alpaca-strategy-exploit-post-mortem-and-bearn-s-compensation-plan-b0b38c3b5540)


