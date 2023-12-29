# DARK DEFI
![DARK DEFI](/rektimages/DARK-DEFI.png)
- Amount Lost: $26,543.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-2-20

**Quick Summary**

Investors of the DARK DEFI project essentially got rekt by two mechanisms the contract deployer introduced which resulted in a centralization issue where one independent wallet was holding more than 5% of the total $DARK token supply. 

  


 **Details of the Exploit**

A look at  DARK DEFI's source code would have pointed investors directly to the fact that the contract owner could disable the transfer function, which restricted users in selling their tokens. This fact also became known to the community later on when alerts surfaced that users were not able to sell their token. In short, the contract deployer added initial liquidity at:  
https://etherscan.io/tx/0xc4bc0b94d780f5c33feef9d6adf0f2d77130d9a374987fe106431343564c29ea  
The LP tokens were locked and transferred to the vesting smart contract:  
https://etherscan.io/tx/0x69a6c3d991e8ce3e05097b4855d8f0673ed58f283101066b7e80ea829b3f5693  
The contract deployer als used a hidden minting functionality under the _approveAndCall_ () function to generate new tokens onto this external wallet at:  
https://etherscan.io/tx/0x32243fbbece007f7d9a10f13ee2c47d5ddd1876781535af6de8fbb5b6df6fe47  
https://etherscan.io/tx/0x7d6ccdbabe7f5a04998b20d10054658392d8dd8f09064b0c355275a6b6625b8e

Through this excessive minting, this external wallet became the top holder of the $DARK token and proceeded to dump the token in several transactions on the Uniswap exchange:  
https://etherscan.io/tx/0x3e7fb02a83a7de08c0ba90500506c1689a3efb0300806738143deb018203d9a6  
https://etherscan.io/tx/0x63987426312764999e209308e1c9881482ba60dfdf7248350f4ee7a77096139f  
https://etherscan.io/tx/0xddb8bc288dc0704dca9897b446098d5f6e94511cf774303261d8889c55fa3d9c

  


 **Block Data Reference**

DARK DEFI token deployer (scammer):

https://etherscan.io/address/0xfa5a97ce3badaeb5f7ca6e406e42e70319a67b4a

  


Scammer Address B:

https://etherscan.io/address/0x93ec7f43330585bb3c81f3cce2b7a9f3e6bad66f

  


More example Transaction:  
https://etherscan.io/tx/0xef5c9b6d155193549fb417a4dc35f2d364501d91bfa0523d23e7b1017651e76f  
https://etherscan.io/tx/0xc63eeb6f792e732e248ba0ba747956d485ae5bca6f89f70068b4615f3bbbfaa2



