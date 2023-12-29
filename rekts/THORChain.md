# THORChain
![THORChain](/rektimages/THORChain.png)
- Amount Lost: $8,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-7-22

**Quick Summary**

Thorchain Bifrost component was exploited through the ETH Router contract, resulting in the loss of various tokens including 966.62 ALCX, 20,866,664.53 XRUNE, 1,672,794.010 USDC, 56,104 SUSHI, 6.91 YFI, and 990,137.46 USDT.

  


 **Details of the Exploit**

The attacker created a fake router and emitted a deposit event by sending ETH. They then passed returnVaultAssets() with a small amount of ETH, but the router was defined as an Asgard vault. On the Thorchain Router, it forwarded ETH to the fake Asgard. This action created a fake deposit event with a malicious memo. Thorchain Bifrost interpreted this as a normal deposit and refunded to the attacker due to a bad memo definition.

 **  
**

 **Block Data Reference**

  


The attacker's address:

https://etherscan.io/address/0xd95e6eab231b9f3afa24c31c7050bd84c2982072#tokentxns

  


The transaction behind the attack:

https://etherscan.io/tx/0x9db403ad39d3fe78de378af0b49f03d244326662f7fee230db87d12a624f564b

  


Other relevant addresses:

Router: https://etherscan.io/address/0xc145990e84155416144c532e31f89b840ca8c2ce

Vault: https://etherscan.io/address/0xf56cba49337a624e94042e325ad6bc864436e370

Attack contract: https://etherscan.io/address/0x700196e226283671a3de6704ebcdb37a76658805

Attack wallet (spawned from Tornado Cash): https://etherscan.io/address/0x8c1944fac705ef172f21f905b5523ae260f76d62


Proof Links:
- [https://medium.com/thorchain/post-mortem-eth-router-exploits-1-2-and-premature-return-to-trading-incident-2908928c5fb](https://medium.com/thorchain/post-mortem-eth-router-exploits-1-2-and-premature-return-to-trading-incident-2908928c5fb)
- [ https://www.rekt.news/thorchain-rekt2/]( https://www.rekt.news/thorchain-rekt2/)


