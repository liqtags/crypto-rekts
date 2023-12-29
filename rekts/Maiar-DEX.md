# Maiar DEX
![Maiar DEX](/rektimages/Maiar-DEX.png)
- Amount Lost: $113,000,000.00
- Funds Returned: $113,000,000.00
- Category: Exchange (DEX)
- Date: 2022-6-5

**Quick Summary**

Maiar DEX was the victim of an attack by hackers who found and exploited a vulnerability in order to empty the reserves of the protocol. Due to this vulnerability, when a $WEGLD contract called a Maiar contract, it allowed Maiar to perform a token transfer in the context of the $WEGLD contract, the calling party. Maiar DEX was successfully recovered by the Elrond team, and user funds were not affected

  


 **Details of the Exploit**

The Maiar DEX protocol was attacked by hackers who took advantage of a vulnerability in the WEGLD contract to steal funds from the protocol on the Elrond network. The attacker's accounts were created almost simultaneously and tokens in the amount of 1.959 $EGLD were sent to each of them from Binance Hot Wallet:

  


Block Data Reference

1) https://explorer.elrond.com/transactions/ba7bcea55911973556c0c855a912c868e76a658792b62a6688c16a14c98a0102

2) https://explorer.elrond.com/transactions/27935d8bceaee5b179bddb1dcd9683a3c227055c8ac70b4bd5f3a40a2b5f6dd1

3) https://explorer.elrond.com/transactions/73f39d3edf0cf5f0893fa3a8175f614329960572e2843f6a21f60b5e1bf778f5

  


After the accounts were created and smart contracts as well, they called the withdraw() function and received a total of 1,650,000 $EGLD. The most important here is the wrat_egls_callback() function. This function enables the wrapping and unwrapping of the $EGLD token.

  


In the transaction below, it can be noticed that as the new smart contract sends a small amount of $EGLD to the wrapEgId() method and this method sends $WEDLD to the wrap_edId_callback() method of the new contract:

https://explorer.elrond.com/transactions/848b5a96bd95d3537f2bb8cfc5c1ebc5ec580e72214dd75c85be718ae0bbf3fb#4159433916247dbdbfbbf31d8a4cc8ce14a3a86e5a5f7beb1cddcf5abc59b83e

  


Deploying the wrap_egId_callback() method, was found a call of the managedExecuteOnDestContextByCaller() method, which allows attacker to "ask" the victim's contract to send funds to any other address that the attacker indicates, which happened during the attack on Maiar DEX. The Elrond team paused the work of Maiar DEX, they also froze stablecoins so that the hacker would not be able to withdraw funds through the bridge to another network. Having connections with other major exchanges, they handed over a blacklist with addresses so that the fraudster would not be able to withdraw funds. The executeOnDestContextByCaller() function was removed to avoid a repeat attack. Then the team began to restore the liquidity pool by returning all funds and restoring the price of the token, based on the price indicated by Binance.

  


Block Data Reference

Attacker addresses:

1) https://explorer.elrond.com/accounts/erd1cura2qq8skel5fsxrpxyysjkaw6durengtkencrezkw78y6y2zhscf854j

2) https://explorer.elrond.com/accounts/erd1yrf9qeuqkcjeh5c4xn628mags7cse4r9ra2p2ggmlgfqq3l3v6pqxfu950

3) https://explorer.elrond.com/accounts/erd16syfkds2faezhqa7pn5n8fyjkst70l5qefpmc0r960467snlgycq4ww0rt

  


Contract addresses:

1) https://explorer.elrond.com/accounts/erd1qqqqqqqqqqqqqpgq85hhnppjcdamledp3usgkm3lm832jekw2zhsajjztn

2) https://explorer.elrond.com/accounts/erd1qqqqqqqqqqqqqpgqqucnpav4dguh4zf6nvd48l68k2nxhyu0v6pqqntgfs

3) https://explorer.elrond.com/accounts/erd1qqqqqqqqqqqqqpgqll7yerx6v67p0s8va0h09dgv7x30nlergycqt2qzmp

  


Contract deployment transaction by the attacker address (erd1...854j): https://explorer.elrond.com/transactions/9404479926078441d8fd8844ec4787c4c35c554628abdc7605c8084f49299352 

Contract deployment transaction by the attacker address (erd1...u950): https://explorer.elrond.com/transactions/39c7aebfe5ebbe4bcc285ef5cc99869486705afa4ce94071c5aafc6124864fb7

Contract deployment transaction by the attacker address (erd1...ww0rt): https://explorer.elrond.com/accounts/erd1qqqqqqqqqqqqqpgqll7yerx6v67p0s8va0h09dgv7x30nlergycqt2qzmp

  


Transactions of theft of funds from the Maiar DEX:

400k EGLD: https://explorer.elrond.com/transactions/8b8c332577e5b8bdd4e13450ea92b7c6b0ca15399f1f0bb38fc215cfc3ddb490

450k EGLD: https://explorer.elrond.com/transactions/39998ab5c929fa67e95d0c64081697fc4207235dbfeaaff10fb2704a6c7716b6

800k EGLD: https://explorer.elrond.com/transactions/41effd8536376f3a2edba7074c02776edae94bb5b464485ac414847202eebbe2

  


Recovered funds were send to one of Elrond addresses: https://explorer.elrond.com/accounts/erd1pml9k2tsqsnvtmmalglt2su0sn3cguvr8e8jq0gy69zw2ldcej2qapml9a


Proof Links:
- [https://www.bitdegree.org/crypto/news/maiar-dex-loses-113-million-worth-of-egld-after-going-offline](https://www.bitdegree.org/crypto/news/maiar-dex-loses-113-million-worth-of-egld-after-going-offline)
- [ https://elrond.com/blog/incident-and-recovery-report/]( https://elrond.com/blog/incident-and-recovery-report/)
- [ https://cryptotodayinfo.com/%F0%9F%9A%ABelrond-hacked-%E2%A4%B5%EF%B8%8Fegld-to-5-in-seconds-%E2%8F%AF%EF%B8%8Fexchange-paused-%F0%9F%94%9Cwhere-will-it-all-end/]( https://cryptotodayinfo.com/%F0%9F%9A%ABelrond-hacked-%E2%A4%B5%EF%B8%8Fegld-to-5-in-seconds-%E2%8F%AF%EF%B8%8Fexchange-paused-%F0%9F%94%9Cwhere-will-it-all-end/)


