# DataDAO Finance
![DataDAO Finance](/rektimages/DataDAO-Finance.png)
- Amount Lost: $781,637.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-1-30

**Quick Summary**

A backdoor is created in the supportsInterfaceCall() function that allowed to do calls to token contracts and transfer Part tokens of those who did approvals to the malicious  Part contract.

  


  


 **Details of the Exploit**

By 13.09.2022, supportsInterfaceCall() is being continuously called. For now, the last function execution was done on the 10th of Aug 2022. The tokens draining started on the 31th of Jan 2022.

As a result, the following losses take place: 

558348 USDC

214749  DAI

8540 MIM

  


Still, any approved tokens left are endangered and can be drained anytime. This again demonstrates the importance of monitoring approved contracts and checking them for vulnerabilities and backdoors. 

  


 **F** **unds lost** : 781 637

  


 **Block Data Reference**

Backdoor function (supportinterfaceCall())

https://ftmscan.com/address/0x689e0205d21337cfebbe0beabf33e1bae2a1ae06#code#L1007

Example transactions 

https://ftmscan.com/tx/0x754b5ab0d6aaec00e4a7f173caccce3fc3e999d2a1a58192ae7a11527b9189d5

https://ftmscan.com/tx/0x5d1242f7e07f5f803005039f490d5d0c84d73679bb1a239df6cac342f54d088b

Recipient of tokens

https://ftmscan.com/address/0xfc2fb8fd8c98b6a16a0da7638e1c0b8085f8ed69


Proof Links:
- [https://finance.yahoo.com/news/users-datadao-finance-risk-losing-103641748.html](https://finance.yahoo.com/news/users-datadao-finance-risk-losing-103641748.html)


