# Health
![Health](/rektimages/Health.png)
- Amount Lost: $8,800.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-10-20

**Quick Summary**

Price of the HEALTH token in a Uniswap pool was manipulated allowing the attacker to take a 33 BNB profit. 

  


 ** **Details of the Exploit****

The exploit was possible due to a bug in the internal _tranfer() function of the token contract that was causing decrease of HEALTH in the pool. 

  


The attack was performed in three transactions. Each transaction involved the following steps: 

1\. Taking a flash loan of 40 WBNB;

2\. Exchanging the borrowed amount to HEALTH;

3\. Calling 999 token transfers with 0 value. Due to the bug in _transfer(), the number of HEALTH in the pool decreased each time, hence the token price was increasing.

4\. Exchanging the inflated HEALTH token to WBNB with profit. 

5\. Paying back the flashloan 

  


 **Block Data Reference**

 **The attacker contract:**

 **https://bscscan.com/address/0x80e5fc0d72e4814cb52c16a18c2f2b87ef1ea2d4  **

  


 **The attack transactions:**

https://bscscan.com/tx/0xae8ca9dc8258ae32899fe641985739c3fa53ab1f603973ac74b424e165c66ccf 

https://bscscan.com/tx/0x780f712866bc2ad2a32239b2702121856693476580ffee772f9a49148be0266a 

https://bscscan.com/tx/0x0daad55e460d673a554fc9458032ce70d3d201b6506474b15b24f2f14aa3a462


Proof Links:
- [https://blog.solidityscan.com/health-token-hack-analysis-dad822fbf0](https://blog.solidityscan.com/health-token-hack-analysis-dad822fbf0)
- [ https://twitter.com/BlockSecTeam/status/1583073442433495040]( https://twitter.com/BlockSecTeam/status/1583073442433495040)


