# ChainSwap
![ChainSwap](/rektimages/ChainSwap.png)
- Amount Lost: $4,400,000.00
- Funds Returned: $0.00
- Category: Bridge
- Date: 2021-7-11

The attacker's address:  
https://etherscan.io/address/0xEda5066780dE29D00dfb54581A707ef6F52D8113  
  
On the Ethereum network, each token to be bridged has its own proxy Factory contract. The attacker was able to exploit the contract, minting tokens directly into different addresses, before reaccumulating them into the wallet from which the transactions were initially sent.  
  
The attacker:  
\- called _receive_ () function to the Factory minting contract  
  
\- dodged the sloppy auth check system using a new address as signature each tx  
  
\- paid 0.005 ETH _chargeFee_  
  
\- set to parameter to the desired address, which receives the minted volume  
  
\- repeated x times.  
  
Using the NFT platform WilderWorld as an example, this is one of 40 repeated transactions, each of which produced 500,000 $WILD tokens.  
  
These 20M WILD were subsequently sold for 650 WBNB, or little more than $200,000 USD, using PancakeSwap, essentially emptying the WILD/WBNB pool.  
  
The example transaction:  
https://bscscan.com/tx/0x83b4adaf73ad34c5c53aa9b805579ed74bc1391c5297201e6457cde709dff723  
  
Projects which got harmed:  
\- Wilder Worlds  
\- Antimatter  
\- Optionroom  
\- Umbrella Blank  
\- Nord  
\- Razor  
\- Peri  
\- Unido  
\- Oro  
\- Vortex  
\- Blank  
\- Unifarm


Proof Links:
- [https://chain-swap.medium.com/chainswap-exploit-11-july-2021-post-mortem-6e4e346e5a32](https://chain-swap.medium.com/chainswap-exploit-11-july-2021-post-mortem-6e4e346e5a32)
- [ https://www.rekt.news/chainswap-rekt/]( https://www.rekt.news/chainswap-rekt/)


