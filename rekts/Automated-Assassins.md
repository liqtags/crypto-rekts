# Automated Assassins
![Automated Assassins](/rektimages/Automated-Assassins.png)
- Amount Lost: $202,000.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2022-6-3

**Quick Summary**

The Automated Assassins has been rugpulled by the project team. The team that was involved in the project created a collection on OpenSea, then to make the collection look more attractive, they raised the price of the token. When people minted the NFT by investing their funds in the contract, the team called function withdraw() to get all the funds from it in the amount of $202K.

  


 **Details of the Exploit**

Automated Assassins was supposed to be a P2E game.

The team of the project created the NFT contract with this transaction (https://etherscan.io/tx/0x026b705a99af7ff24b1e70e02fc1d432025b4a669320f8d8c6e254204b07d7a4).

  


The project team used funds that were raised in the initial minting phase in order to sweep the floor price of the collection on OpenSea, making the collection appear successful to investors (https://etherscan.io/tx/0x7200806a75448f6fb4f3dcf741195a4479cd3e23bd6674eaad4df338964bb79e).

In this transaction, the _withdraw()_ function is called, where all the $ETH from the contract are withdrawn  
(https://etherscan.io/tx/0x03987fdd2ae42a01b201b4abeab462c8302ab457ff7021b466f5e92ef6c24b40).

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Token contract address: https://etherscan.io/address/0x8abfc9689827db7b00f67b7ebc90ee707bc07437

  


Address that deployed the contract: https://etherscan.io/address/0xff45874e2bde87e773551b7eb086533df02f022f

  


Scammer addresses: 

1) https://etherscan.io/address/0x3c1e66d6fe004b581ace44612726164ad34dbd7f 

2) https://etherscan.io/address/0xb7c8d69703289bdaf21d7a419b7af95b32d8ca40 

3) https://etherscan.io/address/0x67ef43a7b0fdc38db0990413a86f7b0dc0220f7f 

4) https://etherscan.io/address/0x1f07957e1e5f3585c762736a83a2ce3140fccfa9 

5) https://etherscan.io/address/0xd40999c2b045f6a175acc0b478bbf0bed6e918fc 

6) https://etherscan.io/address/0x5609b9338ec0351dd0f31d29c9a5105b0c22371a


Proof Links:
- [https://www.breadcrumbs.app/reports/2247](https://www.breadcrumbs.app/reports/2247)
- [ https://www.chainabuse.com/report/e61fda1b-6791-47b7-8572-3eb5f7435bb6]( https://www.chainabuse.com/report/e61fda1b-6791-47b7-8572-3eb5f7435bb6)


