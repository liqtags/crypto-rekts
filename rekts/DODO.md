# DODO
![DODO](/rektimages/DODO.png)
- Amount Lost: $3,800,000.00
- Funds Returned: $3,100,000.00
- Category: Exchange (DEX)
- Date: 2021-3-9

The exploits targeted several DODO V2 Crowdpools, namely the WSZO, WCRES, ETHA, and FUSI pool.  
  
The DODO V2 Crowdpooling smart contract has a bug that allows the _init_ () function to be called multiple times. This means that an exploiter can perform an attack with the following steps:  
  
1\. Exploiter creates a counterfeit token and initializes the smart contract with it by calling the _init_ () function.  
2\. Exploiter calls the _sync_ () function and sets the “reserve” variable, which represents the token balance, to 0.  
3\. Exploiter calls _init_ () again to re-initialize - this time with a “real” token (i.e. tokens in DODO’s pools)

Exploiter uses a flash loan to transfer all real tokens from the pools and bypass the flash loan check.  
  
The exploiter 1:  
\- interacted with a centralized exchange  
  
\- withdrew 0.46597 ETH from Binance: https://etherscan.io/tx/0x970b32a8c81dd3fc47fa118621726fc418ec3526c4379470a4000ed7b448360f  
  
\- executed, in quick succession, 7 BUSD withdrawal transactions (see the link for one example), possibly involving the Binance Bridge: https://etherscan.io/tx/0x300de107cbca466abe121112848daaf7f5f0d15625d54773dd0bbbff4e276e93  
  
\- transferred 67,416 BUSD to 0xa305fab8bda7e1638235b054889b3217441dd645 twice: https://etherscan.io/tx/0x306d08f3d8af85dfdea7a6edb336d7504e8ecc7c609e4b940d188ba68e11cab5 https://etherscan.io/tx/0x56dbf6421c6e6bd779ab0c12fd49e1f7714dd85023aa74abae1940f8d88669cf  
  
\- transferred 59,245.324743 USDT to 0xa305fab8bda7e1638235b054889b3217441dd645 twice: https://etherscan.io/tx/0xbee2f507b2f4b4321927a9762dac757df12fe1ba2d6f85314273b9ea542a5c13 https://cn.etherscan.com/tx/0xaf80cf58c88f0e0f2f44e3902e4c7cd2c17122511fbc6c2d9b2cd43fbc4199b9  
  
\- executed two exploits against DODO smart contracts. The first one was against the DODO-USDT test contract, and funds were transferred to 0xa305fab8bda7e1638235b054889b3217441dd645: https://etherscan.io/address/0x328410f276d4fe83fc78fa56ad32d9821a5e5c1c#tokentxns  
  
\- second one was against the WCRES-USDT contract, and funds were transferred to 0x56178a0d5f301baf6cf3e1cd53d9863437345bf9: https://cn.etherscan.com/address/0x910fd17b9bfc42a6eea822912f036ef5a080be8a#tokentxns  
  
The exploiter 2:  
  
\- executed 3 exploits against DODO contracts:  
  
1\. ETHA-USDT: https://etherscan.io/tx/0x0b062361e16a2ea0942cc1b4462b6584208c8c864609ff73aaa640aaa2d92428

2\. WSZO-USDT: https://etherscan.io/tx/0xff9b3b2cb09d149762fcffc56ef71362bec1ef6a7d68727155c2d68f395ac1e  
  
3\. vETH-WETH, with 93,148 gwei: https://etherscan.io/tx/0x561f7ccb27b9928df33fa97c2fb99ea3750593e908f9f0f8baf22ec7ca0c5c4a


Proof Links:
- [https://dodoexhelp.zendesk.com/hc/en-us/articles/900004851126-Important-update-regarding-recent-events-on-DODO](https://dodoexhelp.zendesk.com/hc/en-us/articles/900004851126-Important-update-regarding-recent-events-on-DODO)
- [ https://rekt.news/au-dodo-rekt/]( https://rekt.news/au-dodo-rekt/)


