# Elron Token
![Elron Token](/rektimages/Elron-Token.png)
- Amount Lost: $122,000.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-7-15

**Quick Summary**

The Forest Elron Token project has been rugpulled by its own team. They created a pair between ELR/USDT tokens, where the initial deposit was 300k $USDT and 300k $ELR, and after a while they dumped the token taking a profit of 122k.

  


 **Details of the Exploit**

[](https://www.youtube.com/watch?v=U4xMcd_1mKY)

The token creator deployed the $ELR where the creator is given the minter role, and also transfers ownership to his address: https://bscscan.com/tx/0x1438a06f58cf1e1e19b5bac24f9dd540a914a8562985865b8248247e60b6fc19#eventlog

Also analyzing the code, it was noticed that total supply was minted to this address: https://bscscan.com/address/0xF0C13C7b330145c903cCB98F3ccd54D9C9D44708

300k tokens were sent from mulitisig's wallet to another address, where 300k $USDT was also sent to create an ELR/USDT pair with a ratio of 1 to 1:

1) The sending path of 300k $ELR from Multisig:

    1.1) https://bscscan.com/tx/0xe1c01d6403fb21990686a7abe686302b61ec2f4e949d8da95ebed21e2e95c936

    1.2) https://bscscan.com/tx/0x01837b52e7ff69254c874c9531923b17a3a6bfa68827022da401316f17852678

2) Receiving 300k $USDT from Binance Hot Wallet 6: https://bscscan.com/tx/0x2864bc927bfe113643e5562fefc0d564effb738b330fbc6fef43d1d0e7972df9

3) Transferring 300k $USDT to lp creator: https://bscscan.com/tx/0xc5b9b5a5f2c53355d4d1d9bfbc9e5935092516c6bce3e10681db8d0742de05df

4) Add liquidity transaction: https://bscscan.com/tx/0xefaed2cab8c814734e6cfbfafcc023f9c433b2d27f9fe021cdca804a525f5f5c

Multisig wallet sent 1M $ELR tokens to the address of the token creator: https://bscscan.com/tx/0xecc3fbdfc214505555b7998d73bd17e26b88e9fcffc109450ddd63f8459774ef

After some time, unusual behavior was noticed from the address of the token creator, he started sending a bunch of transactions for 13,899 $ELR to the scammer address (B), here is an example of transactions:

1) https://bscscan.com/tx/0x5d05ae17a1e4e3a0b540de422f7cd269ca2d6894d6dc778830b8ee1eb8b9b1a7

2) https://bscscan.com/tx/0xc2b840a031db580e6f16f281ff2bb277039923767031d5a59206379906bf018f

3) https://bscscan.com/tx/0xb86955fe35d44641e63c36a02bd52a6d1118e4edd10c8caf66af81c8efa8f1e2

After scammer address (B) started dumping the token price by selling $ELR on PancakeSwap, example transactions:  
1) https://bscscan.com/tx/0x8e52247ecb967e0eb5186d50970cafaddc7be01c2e4eddd7a47d4bef7afb487e  
2) https://bscscan.com/tx/0x195b4b038fc68f2687be36a751647bb9770a66e2341001b10f70f462360dcd7d  
3) https://bscscan.com/tx/0x014dd513493ab8849a8540be783699a923a1ede16343f3fc56074a5e030042ea

from the moment the pool was created until July 15, 122k $BUSD was invested, ~$242k was taken from the pool and at the moment 180k $BUSD is still in the pool.

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Involved addresses:

Token creator - scammer address (A): https://bscscan.com/address/0x2cc11e2cade4f7a18f9607ef9b5352bfc6e5edaa

Scammer address (B): https://bscscan.com/address/0x12b7ec933f4ad3f85d9ba0e29e64cc2ccd81d0f6

Scammer address (C): https://bscscan.com/address/0xf2f78e289e5f64692b8e0de1e122f73488006d44

Multisig wallet on which more than 90% of total supply is stored: https://bscscan.com/address/0xF0C13C7b330145c903cCB98F3ccd54D9C9D44708


Proof Links:
- [https://dexscreener.com/bsc/0xf45e5c487cc3f7b77b328b3f460169db628feb8e](https://dexscreener.com/bsc/0xf45e5c487cc3f7b77b328b3f460169db628feb8e)


