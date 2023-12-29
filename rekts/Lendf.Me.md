# Lendf.Me
![Lendf.Me](/rektimages/Lendf.Me.png)
- Amount Lost: $25,236,849.00
- Funds Returned: $25,236,849.00
- Category: Borrowing and Lending
- Date: 2020-4-19

**Quick Summary**

Lendf.Me exploited due to a bug in the deposit function, allowing the attacker to manipulate their collateral amount and withdraw all available assets from multiple liquidity pools.

  


 **Details of the Exploit**

The attacker exploited a bug in the deposit function, supply(), in Lendf.Me. The function was hooked by embedding an extra withdraw() function, which allowed the attacker to increase their internal record of imBTC collateral amount without actually depositing the amount. The attacker first deposited a specific quantity of imBTC into Lendf.Me. However, in the second supply(), the attacker not only supplied 0.00000001 imBTC but also withdrew 290 imBTC within the hook by hijacking the transferFrom() function within doTransferIn(). As a result, 290 imBTC were deducted from the attacker's balance under the integrated withdraw(). When the execution returned to supply(), however, the balance was reset to 290 imBTC. This allowed the attacker to modify the internal record of the imBTC collateral amount in Lendf.Me. With a big enough collateral value, the attacker was thus able to borrow all available assets from multiple liquidity pools.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0xa9bf70a420d364e923c74448d9d817d3f2a77822

The transaction behind the attack:

https://etherscan.io/tx/0xae7d664bdfcc54220df4f18d339005c6faf6e62c9ca79c56387bc0389274363b

The withdrawal of the funds by the attacker:

https://etherscan.io/tx/0x9a5899d2151d84a9a8dccd1b1a03abbdf91ea83b1f78f3c631b858c20658c12d


Proof Links:
- [https://medium.com/dforcenet/a-summary-of-the-attack-on-lendf-me-on-april-19-2020-e2f1c5d96640](https://medium.com/dforcenet/a-summary-of-the-attack-on-lendf-me-on-april-19-2020-e2f1c5d96640)
- [ https://peckshield.medium.com/uniswap-lendf-me-hacks-root-cause-and-loss-analysis-50f3263dcc09]( https://peckshield.medium.com/uniswap-lendf-me-hacks-root-cause-and-loss-analysis-50f3263dcc09)


