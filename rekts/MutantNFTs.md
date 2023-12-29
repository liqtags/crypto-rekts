# MutantNFTs
![MutantNFTs](/rektimages/MutantNFTs.png)
- Amount Lost: $25,000.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2023-1-26

**Quick Summary**

The Lab from Mutants is an NFT staking platform that was exploited with a profit of about $25k USD.

  


 **Details of the Exploit**

The recent attack involved using stake keys from various users in a payment address controlled by the attacker, creating Franken addresses. This allowed the attacker to trick our Token Reward Claim validation and claim rewards belonging to other users. Our vulnerability was relying on a simple comparison of stake addresses to determine reward claim eligibility. The attacker was limited to exploiting only eligible rewards and did not impact tokens in our Treasury wallet. The exact method used to obtain other users' reward information is unknown, but it's believed to involve examining addresses engaging with our Raffles/Stakes contracts and querying our API.

  


 **Block Data Reference**

Exploited claims list was provided by Mutants team:

https://mutants-assets.fra1.cdn.digitaloceanspaces.com/others/spoof-attack-hashes.txt


Proof Links:
- [https://twitter.com/jshycs/status/1618373108590837760?s=46&t=Nt5hwUhMdE6xNxykzYzNOQ](https://twitter.com/jshycs/status/1618373108590837760?s=46&t=Nt5hwUhMdE6xNxykzYzNOQ)
- [ https://twitter.com/MutantNFTs/status/1618711926279933952]( https://twitter.com/MutantNFTs/status/1618711926279933952)


