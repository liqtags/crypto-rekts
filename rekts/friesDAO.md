# friesDAO
![friesDAO](/rektimages/friesDAO.png)
- Amount Lost: $2,299,999.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-10-27

**Quick Summary**

On October 27th, an attacker exploited the friesDAO contracts, taking control of the deployer address through a profanity attack vector and drained the treasury of its USDC, resulting in a loss of 2,138,705.403949 USDC, and drained the FRIES tokens in the staking contract and sold them through Uniswap, extracting 120.128930112550592565 ETH ($189,954.761991 at the time).

  


 **Details of the Exploit**

The friesDAO contracts were deployed by one address, which had not transferred ownership of the contracts to a different address such as multisig after deployment. The attacker was able to exploit the contracts by brute-forcing the private key using profanity's vulnerabilities, which reduced the possibilities of private keys due to flaws in generation, and gained control of the deployer contract. The first part of the attack drained all of the USDC from the treasury by swapping it to a bit of FRIES tokens, setting the manual, fixed refund rate variable to a high number, changing the merkle root whitelist of the NFT, and refunded the small bit of purchased FRIES token for the entire treasury’s USDC. The second part took all of the FRIES out of the staking pool, then sold them through Uniswap to extract USDC from the liquidity pool.

  


 **Block Data Reference**

Attacker addresses:

https://etherscan.io/address/0x6b88d0f4e94013b38e7c49ddc24135bfb0e2d49b

  


  



Proof Links:
- [https://www.theblock.co/post/180973/friesdao-hacked-for-2-3-million-in-latest-profanity-exploit](https://www.theblock.co/post/180973/friesdao-hacked-for-2-3-million-in-latest-profanity-exploit)
- [https://docs.google.com/document/d/1xKZmj1aeM9iFrdQ7sieUNvh0_UI60worl1lfs5ImXk0/edit](https://docs.google.com/document/d/1xKZmj1aeM9iFrdQ7sieUNvh0_UI60worl1lfs5ImXk0/edit)
- [https://thespoon.tech/hack-drains-friesdao-restaurant-project-of-2-3m-in-what-looks-like-potentially-lethal-blow/](https://thespoon.tech/hack-drains-friesdao-restaurant-project-of-2-3m-in-what-looks-like-potentially-lethal-blow/)


