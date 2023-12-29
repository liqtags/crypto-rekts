# Swaprum
![Swaprum](/rektimages/Swaprum.png)
- Amount Lost: $2,915,567.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-5-18

**Quick Summary**

Swaprum, an Arbitrum-based DEX project, experienced a rugpull by the deployer. The total funds lost reached 2,915,567 $USD.

  


 **Details of the Exploit**

Swaprum is a decentralized exchange (DEX) on the Arbitrum network with its token $SAPR. An investigation revealed that Swaprum was subjected to a rugpull by its own deployer who had privileged access to LPs in multiple pools and $SAPR token minting.

  


The exitscam consisted of two main parts: 

1) Liquidity removals on various pools such as USDT/WETH ($241k), USDT/USDC ($280k), ARB/WETH ($280k), ARB/USDC($126K), WOM/USDT($49K) and etc. 

2) Liquidity removal related to $SAPR token where initially 800k $SAPR were minted directly into scammer's wallet address followed by direct liquidity draining from SAPR/WETH pool for another 500K $SAPR tokens plus ~$94K USD worth of WETH.

Later the attacker deployed a malicious upgrade for the SAPR Controller Proxy contract which allowed to create additional 200M new $SAPR tokens out of thin air via two separate transactions.

Finally, all available liquidity in Swaprum's SAPR/WETH pool was drained using newly created tokens leaving it empty.

  


The total funds lost reached 2,915,567 $USD and were transferred to another EOA address in two transactions for 1,617.7 $ETH. Consequently, all the stolen funds were transferred through TornadoCash or bridged via Celer Network and Multichain Bridge.

  


 **Block Data Reference**

Scammer address:

https://arbiscan.io/address/0xf2744e1fe488748e6a550677670265f664d96627

  


Funds holder address:  
https://arbiscan.io/address/0xaaf8b44376f4ef3ed477eeeb3553b7623fef5e1c

  


Liquidity removal transaction examples:

https://arbiscan.io/tx/0x0ebc5f9108974f5518cee002ab7dc4cfed6affb8e5f83ad430bfb00431f0c3be 

https://arbiscan.io/tx/0xcb64a40d652ff8bfac2e08aa6425ace9c19f0eeb4a6e32f0c425f9f9ea747edf

https://arbiscan.io/tx/0x45b911b9048687e893a3794ef8ef1091469a10a870249b52bc36c9d2dcd081d0

https://arbiscan.io/tx/0x33020fdf7cc5f0c7e1f1a46243ff1c47da86cb2bfa644c227e7b7a100c74796a

https://arbiscan.io/tx/0x9d66bda06e8b5135c363f2d9f78f2d51139fa3f423e1646980a2eb11f33662b1 

SAPR mint transactions:  
https://arbiscan.io/tx/0x972dc40a445d2262a7fce87d390253d35b73255e9d2fa278afad27c2e0c6f541

https://arbiscan.io/tx/0x821b2e98bb5ab19b6b35e5abaceca3d263a17b07039bc169823d7cf27460168e

  


SAPR liquidity drain transaction example:  
https://arbiscan.io/tx/0x982cc3b27f40ebc4355d29be5eed97bd0be9d0a9fde9c110b25b69b874b33502

  


TornadoCash transfer example:

https://arbiscan.io/tx/0x8424b157b5200ad05a5c18e8aacf0e3087fe619ddee823aba428c6617aeb4eff


Proof Links:
- [https://twitter.com/DeDotFiSecurity/status/1659271879889231880](https://twitter.com/DeDotFiSecurity/status/1659271879889231880)


