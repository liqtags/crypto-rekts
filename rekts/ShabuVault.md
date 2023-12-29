# ShabuVault
![ShabuVault](/rektimages/ShabuVault.png)
- Amount Lost: $4,357.00
- Funds Returned: $0.00
- Category: Token
- Date: 2020-11-4

At first, the contract deployer removed himself from the list of minters, at this transaction:  
https://etherscan.io/tx/0x497aa751563746ef288e18efad5a0c8ec5ecc04f8e7508d5ece3976d65ab7016  
  
However, he left an opportunity in the token smart contract that would have allowed him to reinstate himself as a minter. He invoked _addMinter_ function in the following transaction:  
https://etherscan.io/tx/0x58bcb174d2442878adad1bdaddb6ac98e7ce346b5cd9e9b8ed80c1cd06676b14

  


After doing this, the owner generated an additional 4K SHABU tokens and placed them in his wallet. The owner could increase the tax rate to 100% and put himself on the whitelist. The project exit scammed after the token contract owner drained liquidity, stealing 10 ETH. ShabuVault's website and social media are inaccessible.


Proof Links:
- [https://archive.ph/Cff4B](https://archive.ph/Cff4B)


