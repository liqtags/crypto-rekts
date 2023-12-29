# Cashio
![Cashio](/rektimages/Cashio.png)
- Amount Lost: $48,000,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2022-3-23

**Quick Summary**

Cashio protocol was exploited due to incorrect collateral validation during minting, which has led to infinite minting.

  


 **Details of the Exploit**  
The validation of the LP tokens is to be deposited via the _saber_swap.arrow_ (USDT-USDC LP) is incomplete, as the mint field is never validated. As a consequence, the hacker was able to deploy a bogus contract that was never verified, followed by a chain of bogus accounts that all passed validation since they were only compared to one another.

  
In addition, in order to pass the _common collateral_ verification, the hacker created a fake bank and was able to instruct the program to mint the original $CASH token because there was no check that the bank's token matched the one being minted.

  


After these actions, the hacker minted 2 billion $CASH tokens, and the part of $CASH was burnt to SaberLPTokens. Then another part of the tokens was withdrawn out to $UST and $USDC. The remaining $CASH was swapped for 8,600,000 $UST and 17,000,000 $USDC. Most of the stolen funds were bridged to Ethereum address. 

  


The hacker left the message in the transaction "Account with less than 100k have been returned. All other money will be donated to charity."

  


 **Block Data Reference**

The hacker's address:  
https://solscan.io/account/6D7fgzpPZXtDB6Zqg3xRwfbohzerbytB2U5pFchnVuzw

  


Validation transaction:  
https://solscan.io/tx/3t1zqtKk4CgCk5ZDZMGSwdfvvWPekyQ5r8Prhk9MiR5Sw8vujCnFBncAuFCttw3oXzacMRH9ud3VY5virUY2Z39y

  


Mint transaction:

https://solscan.io/tx/2X1TKidhbocN5HRLVWRUk8W1YSQH9b6VH7biAm1ad5jwTZNrPSxajz2cyorrvqtUbWUAmCb52Yqk8VxYF2P6H5tP

  
Burning to SaberLPTokens transaction:  
https://solscan.io/tx/4g5okypEDK9xdDwcootYz86uzTXm41VX7WosiJETGisiG2XpvNgT59djDiD2vwstQtCFF9bqSnViYJGF9Z9QrUvV  
  
Withdraw transaction:  
https://solscan.io/tx/pjUgAeUfWaSSJuw2Cq1cQ9gHNWs8jkxJMtHqVAMuwhg3Uk9LN9Y2obfwt6Qm8bztg56xidWBMytzmqyWzvbsrwH  
  
Ethereum address funds were sent:  
https://etherscan.io/address/0x86766247ba3405c5f15f06b895294200809e9cfb

The message hacker left:  
https://etherscan.io/tx/0xa8394d2e55042f84d096c72dd1075fa2648faf88e248c7992273b4d50a6a647b


Proof Links:
- [https://twitter.com/CashioApp/status/1506571243067224064](https://twitter.com/CashioApp/status/1506571243067224064)
- [ https://twitter.com/samczsun/status/1507056110934511619?s=28]( https://twitter.com/samczsun/status/1507056110934511619?s=28)


