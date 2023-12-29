# Snowflake
![Snowflake](/rektimages/Snowflake.png)
- Amount Lost: $468,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-12-30

**Quick Summary**

Snowflake finance was rug pulled. An EOA address was able to remove liquidity from the Snowflake pools for a total of 468,000 $USD due to the backdoor functionality in the protocol. 

  


 **Details of the Exploit**

The Snowflake Exchange protocol is a single-side AMM (decentralized exchange) designed for

exchanging stable cryptocurrencies (USDT, USDC, DAI).

All protocols contracts are built using a Proxy upgradability pattern. In that case, the project admin has the ability to change implementation anytime. All project liquidity pools have a privileged caller with the role of "pool". Currently, the pool has unverified implementation and exactly this contract was used for the rug pull. 

  


 **Block Data Reference**

Scammer addresess:

https://bscscan.com/address/0x198C258B3BeE99CED4E1e3CECfCAE3D5eD481Db6

https://polygonscan.com/address/0x37fb3B6F911F9d2AAd643e2Bc275eC6AC7781A28

https://bscscan.com/address/0x74016af21F6A0bCe08fBc8bca5f352d705125b18#tokentxns

https://bscscan.com/address/0x37fb3b6f911f9d2aad643e2bc275ec6ac7781a28#tokentxns

  


  


Liquidity drain transactions:

https://bscscan.com/tx/0x3f4510867ecf743b6e6674ec570d1750ac77f35b4c621bb74c63b88dbd4615a9

https://bscscan.com/tx/0x538498d63c342db94d0014403b4d4d30afaf659578a8b7099eefa7f1bb7c0b95

https://bscscan.com/tx/0xd8efdc86e8791b15a13b9e79ebf6d0776f978d36cf6e98cb40ac357906bed511

https://bscscan.com/tx/0xab6bad65be1bc2d25b6f22e52c84899aa3dc8af2b72843097da874d4784bb0c8


Proof Links:
- [https://twitter.com/PeckShieldAlert/status/1608670176022761476?cxt=HHwWiMDQqZDAktMsAAAA](https://twitter.com/PeckShieldAlert/status/1608670176022761476?cxt=HHwWiMDQqZDAktMsAAAA)


