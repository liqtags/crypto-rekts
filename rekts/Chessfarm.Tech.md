# Chessfarm.Tech
![Chessfarm.Tech](/rektimages/Chessfarm.Tech.png)
- Amount Lost: $167,772.00
- Funds Returned: $0.00
- Category: Other
- Date: 2020-11-11

**Quick Summary**

Investors of the Chessfarm.Tech project were betrayed due to the project deployers privileged withdrawal access, which enabled the deployer to extract approx. $167k from the project.

  


 **Details of the Exploit**

The Chessfarm.Tech project was a DEX, deployed on the Binance Smart Chain. The project promised to have tackled problems such as hyperinflation and price dumping through its new fair chess distribution. Only 5% of the staking rewards were supposed to go towards the team in order to fund further developments.

The contract deployer added initial liquidity at:  
https://www.bscscan.com/tx/0xe2fd4137ef507c034c665f3fea4d6f77d873c5374ad27d3a21f8926bcb426f0b  
and made the $CHESS token tradable on pancake swap.  
Merely 5 days later the contract deployer used a hidden migration functionality under the _reduceReward_ () function, by invoking it, the deployer received all deposited tokens from the staking smart contract, as can be seen in the following example transactions:  
https://www.bscscan.com/tx/0xeefee4f7828e16a84062b0c3cf429d0cd4cc231a1ca6bc4950296490b98d430d  
https://www.bscscan.com/tx/0x4abde5e6cdd45b0c6eeb46fd324988a2a65baa188f0876342006088cf0267ee3

The received tokens were then sold by the contract deployer as can be seen in the example transaction:  
https://www.bscscan.com/tx/0x777cb33644a763aa7e846495dc654e30f64e02f18313f537c3e722d8fceb50b1  
The deployer managed to gain around $BNB 4000 and decided the funds for Binance BTC tokens at:  
https://www.bscscan.com/tx/0xd68620c0681c5fe6281ebde24c7d573734ae4c90f6b9d4f02f585f3e8262f4e8  
The received $BTCB were distributed between different external addresses and deposited into Binance exchange, here an example:  
https://www.bscscan.com/address/0x4bf9af802d9804c2e4e3308c5658123eeac89947#tokentxns  
  
The deployer also made sure to remove the liquidity in order to maximize his profit:  
https://www.bscscan.com/tx/0x52f89a249f4bbe6f3c029def0765a4ad6897fc98931f786725bc486fd07229a2

  


 **Block Data Reference**

Example Transactions (Reduce Rewards)

https://www.bscscan.com/tx/0x50b1a1594d9980e2bfca18dc80c7e5fa99c0170602936bbe37a7d527c322f447  
https://www.bscscan.com/tx/0xfff49ffe24c3105b134e264748dfac4f4bcb3928d3207cde0f5d1f9c84edcd40  
https://www.bscscan.com/tx/0x84ddf423ecb1448466f3079a20004dda9619a75f4a4d5c6c5b671f5ebb1f93d5  
https://www.bscscan.com/tx/0x80611a1a729b0d49557aff9b2b9e83e8701ca264b640eacb924e9bb5e424b18f  
https://www.bscscan.com/tx/0x2b1818c93db9c64be6865b034fafafc52bb228c703b544802b1a72430ee366f1

  


Example Transaction (Deployer Dumping)

https://www.bscscan.com/tx/0x353ce25e0d03838cb5255688a2a59f3428c117592aba570e98d73b39bde4e569  
https://www.bscscan.com/tx/0xaaf8648a4b2fa3577e83220a8923570a45fc8c858a51a138b48dbf0913f391d4  
https://www.bscscan.com/tx/0x604533dde572b549b0f247c0f68555977353ed429a4e8112de334bd8ce49b698  
https://www.bscscan.com/tx/0xebbf66a68dabb526bf673cda2a93ac947017963fb642327136a9a1047a4c79b3



