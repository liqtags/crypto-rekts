# Impossible Finance
![Impossible Finance](/rektimages/Impossible-Finance.png)
- Amount Lost: $660,657.00
- Funds Returned: $0.00
- Category: Other
- Date: 2021-6-21

The attacker's address:  
https://bscscan.com/address/0x8e0d334a77614a7ce089c9246e9b1d7c7172ef02  
  
The transactions behind the attack:  
https://explorer.bitquery.io/bsc/txs/calls?internal=false&contract=0xc7ca5478a41d58e73f0487b0f4084b6120aa11e6&method=641ccd83  
  
The attacker:  
\- borrowed 233.3 BNB of flash loan from PancakeSwap  
  
\- swapped 65,140 IF tokens  
  
\- created a fake token called AAA (BBB)  
https://bscscan.com/token/0x9892dd7a51a09c970e2a925e3baf2107bc8dac74  
  
\- created LP with the fake token and IF token  
  
\- swapped 32,570 IF into 221,898 BUSD and another 32,570 IF into 221,898 BUSD using IF router through the FAKE token LP  
  
\- repeated the steps from 3 to 5  
  
\- sold 556,384 BUSD for 1,731 BNB, repaid the flash loan.  
  
Stolen funds were bridged into Ethereum mainnet onto this address:  
https://etherscan.io/address/0x8e0d334a77614a7ce089c9246e9b1d7c7172ef02  
  
The further destination is unknown.  
  
There are transactions where the Impossible Finance hacker is transferring BNB tokens, which were used to perform a flash loan into the Impossible Finance deployer's address at:  
https://bscscan.com/tx/0x05d962a8ade674c3a6f18149e65091ef32503464ad9c5136aea5b921cedcb244  
https://bscscan.com/tx/0x487403ee90840224117ed94b61ff9838b246dc479f75df1fdc36cb02e76edbb1  
  
In addition:  
\- Impossible Finance exploiter into 0x6b3 (849.2 BNB):  
https://bscscan.com/tx/0x7104c2c188776b1ee86313b71c90f5e258ab4524056b7607e7baec2903235eff  
  
- 0x6b3 into Eleven Finance deployer (849 BNB):  
https://bscscan.com/tx/0xb70cb9da942fa6765ce2341da4f4860277d063e6aa99058d4b6da86a876ee4f1  
  
The further funds' flow as follows:  
1\. Deployer into Gnosis Safe Proxy:  
https://bscscan.com/tx/0x48ccb426dcb0b2e14d835de8a6fdb73a415d2f332739cceeb5ef3ad28c01e644  
https://bscscan.com/tx/0x1384c22d07c276b99c2c7e1c6b4821388bf723a65650639eb40a6e021fd245ec  
  
2\. Gnosis Safe Proxy into 0x22b (1,000 BNB):  
https://bscscan.com/tx/0xfdb6fec85e0c6c0f0cc9831542de8afc74346ccfe7f27b06691266bf65a56c96  
  
2.1 Gnosis Safe Proxy into 0x1Cc (521 BNB):  
https://bscscan.com/tx/0x63d7b8fd426da9bf46b0fb16979e2bdeeae9d9e20d47bd87cf6a698311412e80 (Still on the balance)  
  
3\. 0x22b into 0x736 (900 BNB):  
https://bscscan.com/tx/0xdb8860fccf53dcef0dfd6542d54d07c62bd180d965549cdadad074e8c2bc4941  
  
3.1 0x736 into Disperse (674.35 BNB):  
https://bscscan.com/tx/0xf912b616f005ae248d84c2a46b978b31aa225efafb0e6908b62bf2b30608c010  
https://bscscan.com/tx/0xe705db37965d575fe9ead379a11d9ded5e82d9d68096d8b5b733389217b57776  
  
3.2 0x736 added liquidity into pair WBNB / IF (225 BNB):  
https://bscscan.com/tx/0xedcd98a1098084f4222e62f6e9d8966a25693457c8f653778e00d40ce5e98833  
https://bscscan.com/tx/0x3c8de03c3c50289cfb11a4b26e43b0a5253fd5eb780745facfe5b0d8239b772c  
https://bscscan.com/tx/0xb9389fce6167e9176080f04b29c1e437fc506bd0651fef47fac1a634c0864f57  
  
4\. 0x22b into 0x1Cc (451 BNB):  
https://bscscan.com/tx/0xc2484e4eb7eca9b62d29f79a9bd9f5cfb7a7ad93a68afd2e771f21f8340fe5fd  
https://bscscan.com/tx/0xf984147f40fcd5bb61af40771824889a1768cd2c648d678fb1d96ef63a7298c0  
  
4.1 0x1Cc into Binance How wallet (450.99 BNB):  
https://bscscan.com/tx/0xf3cef2128facecdf9b6a9d0c2af57b35a323e565e28d299c97f9a717b9a4ebc3


Proof Links:
- [https://medium.com/impossiblefinance/impossible-finance-v2-swap-jun-21st-postmortem-94e4b59ad490](https://medium.com/impossiblefinance/impossible-finance-v2-swap-jun-21st-postmortem-94e4b59ad490)
- [ https://watchpug.medium.com/impossible-finance-exploit-root-cause-analysis-ba0ed7c151e4]( https://watchpug.medium.com/impossible-finance-exploit-root-cause-analysis-ba0ed7c151e4)


