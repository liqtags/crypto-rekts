# bZx
![bZx](/rektimages/bZx.png)
- Amount Lost: $47,600,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2021-11-5

**Quick Summary**

The private key controlling BSC and Polygon deployments was compromised, allowing attackers to transfer ownership of the core bZx contracts and withdraw users' deposited collateral.

  


 **Details of the Exploit**

The attackers initiated the exploit by transferring ownership of the core bZx contracts. This was done by invoking the target contract with a method through a fallback function with delegatecall. This allowed the attackers to withdraw users' deposited collateral from interest iTokens into another address. The same method was used on the Polygon chain.

  


Involved addresses:

\- Exploiter 1: 0x74487eed1e67f4787e8c0570e8d5d168a05254d4

\- Exploiter 2: 0x0acc0e5faa09cb1976237c3a9af3d3d4b2f35fa5

\- Exploiter 3: 0x967bb571f0fc9ee79c892abf9f99233aa1737e31

\- Exploiter 4: 0x6551fb9be444987f7482012cbf7ea95a1ee8dd0e

  


 **Block Data Reference**

The transaction behind the attack:

\- setTerget(): https://bscscan.com/tx/0x57e4aa5f2303a0ad4d1d74b1f33ba08a7ae2bf33cb1fa13870230779a3d52199

\- transferOwnership(): https://bscscan.com/tx/0x9b16f5e8a648f72be3f9657880b26e525018e40e8873a14161690f8f48bf01b9

\- iDOGE => DOGE: https://bscscan.com/tx/0xd1cff35db2583a2b3a239195c4567c8b63589079f8a1a9bdd0ef88a75b1ec18d

\- iETH => ETH: https://bscscan.com/tx/0xa288f212bb84d0fa21274d93bc562ad4ecb4c702ff136ba897bbb65d0e50ca88

\- iBNB => BNB: https://bscscan.com/tx/0x2dbb3df6959ba95da3bec8f618a3014f0d14e16816f2502e16d21e24e2597b6a


Proof Links:
- [https://twitter.com/bZxHQ/status/1456603269355094021](https://twitter.com/bZxHQ/status/1456603269355094021)


