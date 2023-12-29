# ForceDAO
![ForceDAO](/rektimages/ForceDAO.png)
- Amount Lost: $367,000.00
- Funds Returned: $367,000.00
- Category: Other
- Date: 2021-4-4

ForceDAO was exploited by one white hat and four black hat hackers.  
  
The white hat hacker's address:  
https://etherscan.io/address/0xf88a427c5bf29acf58497c0088cbf7ca9836b7b2  
  
The black hat #1 hacker's address:  
https://etherscan.io/address/0x9d9c3695c54601929cd72d34a52935268eb9b00b  
  
The black hat #2 hacker's address:  
https://etherscan.io/address/0xe29a07002c7be4299b51a2892799cc4a372994dd  
  
The black hat #3 hacker's address:  
https://etherscan.io/address/0x0608576ea47b265f1f16b8b8383d0508f703a0cb  
  
The black hat #4 hacker's address:  
https://etherscan.io/address/0x00000b20f0f6a3a212aa6b85106709cd5941457c  
  
The root cause:  
1\. The exploited xFORCE vault is a fork of the xSUSHI contract, which assumes that a failed transfer will result in a reversion.  
  
2\. The token used in ForceDAO is an Aragon Minime token that returns false if a call to the _transferFrom()_ function fails.  
  
The ForceDAO hackers took advantage of this vulnerability: if a deposit into the xFORCE vault fails, the deposited tokens will remain in the sender’s wallet. However, on the vault’s side, the sender will receive xFORCE tokens in exchange because the code assumes that if it’s still running after the transfer, that the transfer went through successfully.  
  
Black hat #1:  
\- minted xFORCE:  
https://etherscan.io/tx/0xdf05020d5d3c3a975627ce29f24b4eb8ccb8807f9f9c9aa05e644c61fe5f0141  
  
\- withdrew FORCE, using minted xFORCE:  
https://etherscan.io/tx/0x3b60252b36d2de2930a64f360926bfcba44d12ff44719de3c6dd486b9dafe118  
  
\- sold FORCE:  
https://etherscan.io/tx/0x03c84e3f7d9c117260a49bab6bd9cb1b2d7e1cbc6d9362e74c10ef6d48a987e6  
  
Black hat #2:  
\- minted xFORCE:  
https://etherscan.io/tx/0x7df2fe63dfb43676a13146060d36ded98779092e0f7c9fd46caf18b791d4b9fd  
  
\- withdrew FORCE, using minted xFORCE:  
https://etherscan.io/tx/0xe7be5bf25b0ea9fad2fd51021f4a51e5099cf4c91c2ffef94547072fe25ca8d1  
  
\- sold FORCE in multiple transactions:  
https://etherscan.io/address/0xe29a07002c7be4299b51a2892799cc4a372994dd  
  
Black hat #3:  
\- minted xFORCE multiple times:  
https://etherscan.io/tx/0x37b44d5dbbe9c1dd75223e15977153234e8a4dbbbab2495cdcc531f44bf6e3d0  
https://etherscan.io/tx/0x6202403f9fc418fcc464d714753ef49893c174a3da714784251ce03898b34f00  
https://etherscan.io/tx/0x5a27ee4140741fce2dd21ae642a74e95bd3de0df17ba7ae5d9ffc475574135f8  
  
\- withdrew FORCE, using minted xFORCE:  
https://etherscan.io/tx/0x2616ae9fb59e2cbae848208daa3d0f63530b74a8a4e5c6099ee1b858fdc732a8  
  
\- sold FORCE in multiple transactions:  
https://etherscan.io/address/0x0608576ea47b265f1f16b8b8383d0508f703a0cb  
  
Black hat #4:  
\- withdrew FORCE, using minted xFORCE:  
https://etherscan.io/tx/0x8aedc3d1eaef0d63f026dec48d845dfcba2d74211998acb5d19929e4bc020317  
https://etherscan.io/tx/0xef10be2cbb33ff810cf07bd9195596556485f767744afbb93dfeb5717775ebb6  
  
\- minted xFORCE multiple times:  
https://etherscan.io/tx/0xef10be2cbb33ff810cf07bd9195596556485f767744afbb93dfeb5717775ebb6  
https://etherscan.io/tx/0xf8352e968503efbbd0ad24173c87d5d9b009adf74bdfdf5df4519be6e4911e39  
https://etherscan.io/tx/0xc4abacc3987280fcd97a4dad1459c7a811550589357a9c5ec36f6b783a898106  
  
\- sold FORCE in multiple transactions:  
https://etherscan.io/address/0x00000b20f0f6a3a212aa6b85106709cd5941457c  
  
\- later, funds were returned:  
https://etherscan.io/tx/0x4d535b8c68dd7f03e99a3a350d5df7ef0c6a3e0b2edd4f5601637711b960b793


Proof Links:
- [https://blog.forcedao.com/xforce-exploit-post-mortem-7fa9dcba2ac3](https://blog.forcedao.com/xforce-exploit-post-mortem-7fa9dcba2ac3)
- [ https://halborn.com/explained-the-forcedao-hack-april-2021/]( https://halborn.com/explained-the-forcedao-hack-april-2021/)


