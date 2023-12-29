# Walletreum
![Walletreum](/rektimages/Walletreum.png)
- Amount Lost: $138,340.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2020-11-15

**Quick Summary**

Walletreum's project deployer abused the mint() function and extracted $138k from the project and its investors.

  


 **Details of the Exploit**

Walletreum was supposed to be an innovative crypto asset management tool focussing on lending and borrowing and real-world application. Unfortunately, the smart contract had malicious functions embedded that allowed the project deployer to mint as many $WALT token as desired.

In fact, the contract deployer used the _mint_ () function to generate 500 billion tokens onto an external wallet:  
https://etherscan.io/tx/0xc0f3b0576f18a714d78b822754489d4201c9e36fb0ce4b2f53a93217564710e5

The EOA wallet exchanged the minted tokens for 138,439 $USDT.  
https://bloxy.info/txs/calls_from/0x665f384184a20fa92ecdf87f52d76d25fa29d358?signature_id=1102183&smart_contract_address_bin=0x7a250d5630b4cf539739df2c5dacb4c659f2488d  
The $USDT 138,439 were exchanged for $ETH:  
https://etherscan.io/tx/0xc47c26a8e8704d2af53b69be32c9716e5907299673ba11e15864ccd5ee6e7f15  
Then the attacker decided to swap all of the $ETH in his wallet for 156,120 USDT:  
https://etherscan.io/tx/0xe20d10e798ff5ec588923063fd9b508ddd540d5cda769dc9fd50008d8bfce7ac  
Then funds were then transferred to Binance in multiple transactions as can be seen in the example transactions:  
https://etherscan.io/tx/0xf9cf08f5a3823bb29079d6de8e026bc7d1ad1b90345e2d589b4bb98bf10f221f  
https://etherscan.io/tx/0xcce3eacb6be772d188485fce2c0bd2505738e2957861342729459fe1e87217f9

 **Block Data Scanner**

Project Deployer:

https://etherscan.io/address/0xa5e552e3d643cc89f3b1ceccfd6f42c5c1aee775

EOA Scammer Wallet:

https://etherscan.io/address/0x665f384184a20fa92ecdf87f52d76d25fa29d358


Proof Links:
- [https://archive.ph/6b3Sd](https://archive.ph/6b3Sd)


