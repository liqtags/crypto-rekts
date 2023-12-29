# Lever
![Lever](/rektimages/Lever.png)
- Amount Lost: $652,941.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2021-11-26

The attacker:  
https://bscscan.com/address/0x1bd2c35424bcb28b79ff75b540bbe0c84902f76b  
  
The transaction behind the attack:  
https://bscscan.com/tx/0xb5365a299c07c81670e52934893793ad7c225a5cf30b641e20b451b2b5815593  
  
Attack contract A:  
https://bscscan.com/address/0x5f92949a14e92d42ac182b27e1541fca4ca13f4e  
  
Attack contract B:  
https://bscscan.com/address/0x3790c9b5a9b9d9aa1c69140a5f01a57c9b868e1e  
  
Steps:

\- attack contract A flash loaded 2,100 BNB from PancakeSwap and deposited 2000 BNB on Lever’s BNB vault  
  
\- borrowed 1500 BNB from Lever’s BNB vault and transferred it to Lever attack contract B  
  
\- attack contract B deposited 1500 BNB and used it to drain 32.78 ETH, 1,068.05 BAKE, 167.25 XVS, 1,042.89DAI, 64,157.79 BUSD, 54,335.19USDT ,2.8806 BTC, 1,930.01CAKE, 463.0078DOT, and 332.9184 WBNB  
  
\- The total loss equals $652941.  
  
Attack contract A used attack contract B’s 1500 xBNB (which had been collateralized to borrow other assets) to repay the 1500 dBNB it borrowed, by calling the _repay_ () function in the MarginPool.sol contract.  
  
The contract didn’t check the liabilities of the caller. The attack contract B was able to repay the attack contract A’s dtoken with its xtoken. The attack contract A repaid the flash loan on PancakeSwap.


Proof Links:
- [https://levernetwork.medium.com/full-report-of-the-lever-hack-ee508cf7488c](https://levernetwork.medium.com/full-report-of-the-lever-hack-ee508cf7488c)


