# Paribus
![Paribus](/rektimages/Paribus.png)
- Amount Lost: $69,696.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2023-4-11

**Quick Summary**

Paribus was exploited due to a reentrancy issue, resulting in the loss of 69,696 $USD worth of $ETH.

  


 **Details of the Exploit**

Paribus is a cross-chain lending and borrowing protocol. The protocol suffered an exploit on the Arbitrum layer-two chain. The root cause was a well-known reentrancy vulnerability from an old version of CompoundV2 that Paribus had forked. The attacker deployed two malicious unverified contracts and used this vulnerability to withdraw funds multiple times before updating their balance on-chain. As a result, they were able to drain 35.2 $ETH which is currently worth 69,696 $USD at the time of writing.

All stolen assets were transferred through Stargate Bridge in two transactions.

  


 **Block Data Reference**

Attacker address:

https://arbiscan.io/address/0x014abff04e5c441b2ceaa62d843bbc5ae49e5504

  


Malicious transaction:

https://arbiscan.io/tx/0x0e29dcf4e9b211a811caf00fc8294024867bffe4ab2819cc1625d2e9d62390af

  


Malicious contracts:

https://arbiscan.io/address/0xcd31e27f0a811de7139938b1972b475697f8c50b

https://arbiscan.io/address/0xec05281d0345f5142acd197bdbc6c4e1fc29dfe7


Proof Links:
- [https://twitter.com/peckshield/status/1645742296904929280?s=20](https://twitter.com/peckshield/status/1645742296904929280?s=20)


