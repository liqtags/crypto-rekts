# Rikkei Finance
![Rikkei Finance](/rektimages/Rikkei-Finance.png)
- Amount Lost: $1,115,266.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,NFT
- Date: 2022-4-15

**Quick Summary**  
The Rikkei Finance project was exploited by a hacker who replaced the main price oracle with a malicious one due to the lack of access measures in SetOracleData, which led to the loss of $1.1M.  
 **  
Details of the Exploit**

Rikkei Finance is a DeFi lending and borrowing protocol and an NFT Marketplace.

The attacker deployed a fake ChainLink contract, taking advantage of the vulnerability to replace the real ChainLink address with a fake one. The attacker created a smart contract that was used to carry out an attack on the project in this transaction: 

https://bscscan.com/tx/0xb660132567cf5fb60af136762729fd9ad0662baf01ac6cc74b0a285e5b3399dd

After creating the contract, the attacker called the function "0x21e85463" which caused a number of transactions to empty the protocol. All the stolen funds were laundered via Tornado.Cash.

  


 **Block Data Reference**

Attacker address: https://bscscan.com/address/0x803e0930357ba577dc414b552402f71656c093ab

Attacker contract addresses: 

1) https://bscscan.com/address/0xe6df12a9f33605f2271d2a2ddc92e509e54e6b5f

2) https://bscscan.com/address/0xa36f6f78b2170a29359c74cefcb8751e452116f9

Attack transaction: https://bscscan.com/tx/0x93a9b022df260f1953420cd3e18789e7d1e095459e36fe2eb534918ed1687492


Proof Links:
- [https://www.certik.com/resources/blog/6HPWlnxlEFnyKkbJL4LkGe-revisiting-rikkei-finance-exploit](https://www.certik.com/resources/blog/6HPWlnxlEFnyKkbJL4LkGe-revisiting-rikkei-finance-exploit)
- [ https://knownseclab.com/news/625e865cf1c544005a4bdaf2]( https://knownseclab.com/news/625e865cf1c544005a4bdaf2)
- [ https://blockmagnates.com/rikkei-finance-hack/]( https://blockmagnates.com/rikkei-finance-hack/)
- [ https://rikkeifinance.medium.com/rikkei-finance-incident-investigation-report-b5b1745b0155]( https://rikkeifinance.medium.com/rikkei-finance-incident-investigation-report-b5b1745b0155)


