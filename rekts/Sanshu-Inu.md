# Sanshu Inu
![Sanshu Inu](/rektimages/Sanshu-Inu.png)
- Amount Lost: $279,608.00
- Funds Returned: $0.00
- Category: Token
- Date: 2021-7-21

The attacker's address:  
https://etherscan.io/address/0x0333e323e61aa8afa38a1623604a165dcb9f4fec  
  
The affected Memstake contract:  
https://etherscan.io/address/0x35c674c288577df3e9b5dafef945795b741c7810#code  
  
The attacker:  
\- created two attack contracts, the first one deposited 2,049B KEANU:  
https://etherscan.io/address/0x67a54b340392e661af8f757ba03674ede40d9dc3  
  
the second one is the attack contract:  
https://etherscan.io/address/0xe30dc9b3c29534e9b4e9a166c2f44411163ad59f  
  
\- borrowed a large number of KEANU tokens using the flash loan from UniswapV2, and then deposited the tokens into/withdraws from the Memestake using the second smart contract. Since the KEANU has the deflation mechanism, which burns 2% tokens for each transaction, the real number of tokens deposited into the Memestake is smaller than the value ( _user.amount_ ) maintained by the Memestake contract. The attacker repeated this process and made the number of KEANU tokens inside the Memestake decrease to a small one (1e-07):  
https://etherscan.io/tx/0x00edd68087ee372a1b6e05249cc6c992bb7b8478cc0ddc70c2a1453428285808  
  
\- invoked the _Memestake.updatePool_ () to update the _accMfundPerShare_. This value relies on the number of KEANU tokens (which was manipulated in the second step.) Then the attacker obtained a large number of Mfund(~61M):  
https://etherscan.io/tx/0xa945b1857630e730bd3fac6459c82dee44da45e35cfbbd6dfb7b42146e8dde41  
  
\- swapped the MFund and KEANU to WETH and deposited stolen funds into Tornado Cash mixer:  
https://bloxy.info/txs/calls_from/0x0333e323e61aa8afa38a1623604a165dcb9f4fec?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967  
  
The attacker gained 156.51 ETH as profits.


Proof Links:
- [https://sanshu-inu.medium.com/woofdate-2-1-0-61eaa995f1be](https://sanshu-inu.medium.com/woofdate-2-1-0-61eaa995f1be)
- [ https://blocksecteam.medium.com/the-analysis-of-the-sanshu-inu-security-incident-28c0c7c0e783]( https://blocksecteam.medium.com/the-analysis-of-the-sanshu-inu-security-incident-28c0c7c0e783)


