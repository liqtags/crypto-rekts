# Revest
![Revest](/rektimages/Revest.png)
- Amount Lost: $2,000,000.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-3-27

An example of the transaction:  
https://etherscan.io/tx/0x613b2de3bb9043884a219296eeb1ada8c47b5a0262b9c68ca06ffd2de3a5d9f5  
  
The exploiter's address:  
https://etherscan.io/address/0xef967ece5322c0d7d26dab41778acb55ce5bd58b  
  
The attacker minted a massive amount of FNFT with no cost and used the minted FNFT to drain assets in the vault.  
  
The attacker:  
\- flashloaned 2 ECO tokens from Uniswap

  
\- called " _mintAddressLock_ " in the Revest contract twice to get 2 FNFT[ID 1036] tokens and 7,700,00 FNFT[ID 1037] tokens  
  
\- during the second FNFT minting process, the attacker exploited the reentrancy issue and called the function “ _depositAdditionalToFNFT_ ” to cause the minted FNFT can be used to drain assets in the vault  
  
\- called " _withdrawFNFT_ " to drain assets from the vault by burning 7,700,001 FNFT[ID 1037] tokens and repaying the flashloan.  
  
Stolen funds were deposited into the Tornado Cash mixer:  
https://bloxy.info/txs/transfers_from/0xef967ece5322c0d7d26dab41778acb55ce5bd58b?currency_id=1


Proof Links:
- [https://revestfinance.medium.com/revest-protocol-exploit-recovery-plan-b06ca33fbdf5](https://revestfinance.medium.com/revest-protocol-exploit-recovery-plan-b06ca33fbdf5)
- [ https://twitter.com/peckshield/status/1508395139542106113]( https://twitter.com/peckshield/status/1508395139542106113)
- [ https://twitter.com/CertiKAlert/status/1508072272468320257]( https://twitter.com/CertiKAlert/status/1508072272468320257)


