# Solana Slope Wallet
![Solana Slope Wallet](/rektimages/Solana-Slope-Wallet.png)
- Amount Lost: $5,200,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-8-3

**Quick Summary**  
Solana was subjected to a major exploit due to which approximately 8k Slope wallets were robbed in the amount of ~ $5.2M.  
 **  
Details of the Exploit**

Slope is a web-based, non-custodial crypto wallet and browser extension that allows users to manage assets on the Solana blockchain.

Wallets on the Solana chain were compromised by a hacker who managed to gain access to users' private keys, thanks to which the hacker managed to withdraw funds to his address.

The hacker used a proxy to track network requests. Slope Wallet developers used Sentry to transfer data to the network. By default, Sentry does not use 2FA from which it can be concluded that most likely the Sentry Slope account was compromised, and since the data storage period in Sentry is 90 days, and it is possible to track the data of users who created their accounts in this period of time, the hacker gained access to the clean data of users' wallets such as mnemonic and private key. The vulnerability was also noticed in mobile devices based on android and iOS, most likely the application was written using the Flutter framework, which contains a bug, so the hacker also had access to private user data.

  


 **Block Data Reference**

Hacker account address:

(SOL) 1) https://solscan.io/account/GeEccGJ9BEzVbVor1njkBCCiqXJbXVeDHaXDCrBDbmuy

(SOL) 2) https://solscan.io/account/5WwBYgQG6BdErM2nNNyUmQXfcUnB68b6kesxBywh1J3n

(SOL) 3) https://solscan.io/account/CEzN7mqP9xoxn2HdyW6fjEJ73t7qaX9Rp2zyS6hb3iEu

(SOL) 4) https://solscan.io/account/Htp9MGP8Tig923ZFY7Qf2zzbMUmYneFRAhSp7vSg4wxV

Address that received 0.5 $SOL from the Binance Hot Wallet on Solana: https://solscan.io/account/HYaQcKPcWgLe7gpA99EUbDSGuzJCupNVCRXmXP37xYXv#solTransfers

  


(ETH) https://etherscan.io/address/0xc611952D81E4ECbd17c8f963123DeC5D7BCe1c27


Proof Links:
- [https://www.cnbc.com/2022/08/03/hackers-attack-solana-crypto-stealing-millions.html](https://www.cnbc.com/2022/08/03/hackers-attack-solana-crypto-stealing-millions.html)
- [ https://www.coindesk.com/markets/2022/08/03/phantom-wallet-exploit-drains-millions-in-sol-tokens/]( https://www.coindesk.com/markets/2022/08/03/phantom-wallet-exploit-drains-millions-in-sol-tokens/)
- [ https://techcrunch.com/2022/08/03/solana-wallet-hack/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACHToES-jkSGGdm2C5QA3IenvVC5xIbhJCO0Espn7z1IHdqn9g9P0J0cSr4vftR6iu-AmRWFOOg0zpkcHOJuPWA2NimMxMhH4vO2Fs04PpCiyrafzbC7RlUMeLwo34NXlzWAMIfQ9BZQ2BX0fHA2A0kr6-BHhdCtrnkPghllnHkr]( https://techcrunch.com/2022/08/03/solana-wallet-hack/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAACHToES-jkSGGdm2C5QA3IenvVC5xIbhJCO0Espn7z1IHdqn9g9P0J0cSr4vftR6iu-AmRWFOOg0zpkcHOJuPWA2NimMxMhH4vO2Fs04PpCiyrafzbC7RlUMeLwo34NXlzWAMIfQ9BZQ2BX0fHA2A0kr6-BHhdCtrnkPghllnHkr)


