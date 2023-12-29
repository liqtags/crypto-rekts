# Nft Trader
![Nft Trader](/rektimages/Nft-Trader-Reentrancy-Attack.png)
- Amount Lost: $481,888.00
- Funds Returned: $0.00
- Category: Exchange (DEX),NFT
- Date: 2023-12-16

**Quick Summary**

NFT Trader platform exploited via reentrancy attack, resulting in the loss of NFTs and 481,888 USD worth 210.8 ETH.

  


 **Details of the Exploit**

NFT Trader, a trading platform for NFTs, was exploited on Dec 16, 2023, through a reentrancy attack. The vulnerability was in the project's old smart contract, which had approvals of user funds. The attacker stole various NFTs, including Bored Ape Yacht Club, Mutant Ape Yacht Club, and World of Women. The APE tokens were swapped for ETH and then deposited into TornadoCash. The attacker communicated with the project via on-chain messages, expressing their willingness to return the stolen NFTs, which were eventually returned to the project. The total loss amounted to 481,888 USD worth 210.8 ETH.

  


 **Block Data Reference**

Attacker Addresses:

https://etherscan.io/address/0x909F2159780e64143CF08f32dBBF56Ed19478fda

https://etherscan.io/address/0xd717b85b5da61a56afeb57173c7336084243cdf0

  


Malicious Contract Address:

https://etherscan.io/address/0xc446e0a1e22b54e18303022ff8c5c8ab364d6ebb

  


Malicious Transactions:

https://etherscan.io/tx/0x18f216480346a61707c7db9be831142cb9c1b683b5de6b1a6913254c887d9c39

https://etherscan.io/tx/0x11bb6c85f5dd58f1c68f591a4370e2e55dd808e52b54b6f183dd7c8a9813a3cc

  


Funds Draining Transactions:

https://etherscan.io/tx/0x3d79e70d82615daff0ad767b8ee22c6130191affc367a8640d47d5f368f0526d

https://etherscan.io/tx/0xf31333bd23b34d41b2c8b6676e3569596201a633fe30dac5a1cab4837571112a

  


TornadoCash Deposit Transaction:

https://etherscan.io/tx/0x7d64e9b4096bf7ca7b7d0336bcae9d7b9c9a934c23de6644d896410f2aa99222

  


On-chain Message from Attacker:

https://etherscan.io/tx/0xc2f91dbab46531732908a317290e18297670d0bb02bb66f94aa883ec448d9391


Proof Links:
- [https://twitter.com/NftTrader/status/1736015091563438475](https://twitter.com/NftTrader/status/1736015091563438475)


