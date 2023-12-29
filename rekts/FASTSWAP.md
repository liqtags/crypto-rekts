# FASTSWAP
![FASTSWAP](/rektimages/FASTSWAP.png)
- Amount Lost: $290,738.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-8-14

The attacker:

https://bscscan.com/address/0xfd544b216bf23f4051281f13836c040feefd0921, as was stated by the project team in the tweet:  
https://archive.is/4MRMN  
  
 _tokenMigrate_ () function was called by the address which probably was saved to MasterChef in the _constructor_ () initialization into private variable _migrateAddress_. Since the caller of the _tokenMigrate_ () function was address 0x193D4D22A8610Da6A89b36a1C938778D268D15ef, he was able to invoke LP and token migrations multiple times at:  
https://explorer.bitquery.io/ru/bsc/txs/calls?contract=0xad4219cd9e26832269a49fe6d0edb3c40f64d701&method=99594431  
  
After, tokens were transferred to the external address multiple times, the example transaction:  
https://bscscan.com/tx/0x5bb2d2cef907dba0ea6de4b6ea3a3f1c26e57fd99d3dd68b50d6e94d5fb0f9e2  
  
Liquidity was removed multiple times, tokens were sold as well, the example transaction:  
https://bscscan.com/tx/0x830f9f79b3d43976ed204d095e03b2e9a9b048cdbff2f20a7fc03ac94cb144ba



