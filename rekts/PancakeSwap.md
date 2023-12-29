# PancakeSwap
![PancakeSwap](/rektimages/PancakeSwap.png)
- Amount Lost: $0.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2020-11-3

Bad actors took advantage of a flaw in the connection between the MasterChef contract and the SyrupBar contract. Previously, when CAKE was staked, an equivalent number of SYRUP tokens were created. The SYRUP tokens would be burnt once the CAKE was unstaked and withdrawn. The exact attack here was that if a user invoked the MasterChef contract's emergencyWithdraw method to withdraw their staked CAKE, the related SYRUP tokens were not burned as planned. This enabled malicious actors to mint additional SYRUP tokens using their CAKE tokens on a regular basis.  
  
Because there were much more SYRUP tokens in circulation than was permitted, the bad actors received a larger share of Syrup Pool rewards. 


Proof Links:
- [https://medium.com/pancakeswap/update-on-the-syrup-incident-8f54bf5c054d](https://medium.com/pancakeswap/update-on-the-syrup-incident-8f54bf5c054d)
- [ https://www.bsc.news/post/pancakeswap-emergency-brake-on-syrup-pools]( https://www.bsc.news/post/pancakeswap-emergency-brake-on-syrup-pools)


