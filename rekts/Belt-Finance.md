# Belt Finance
![Belt Finance](/rektimages/Belt-Finance.png)
- Amount Lost: $6,300,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX),Yield Aggregator
- Date: 2021-5-29

**Quick Summary**

Belt Finance suffered a flash loan attack exploiting the Ellipsis strategy, resulting in a loss of approximately $6.3 million.

  


 **Details of the Exploit**

The attacker manipulated the value of a token within a liquidity pool by borrowing cryptocurrency using a flash loan. They exploited a bug in the integration of the Ellipsis strategy within Belt, causing an imbalance in the 3eps pool by swapping BUSD to USDT. This imbalance led to an overestimation of the value of Belt Finance's vault shares. The attacker then withdrew BUSD from the Venus strategy, receiving more tokens than they should have, and providing a profit. The attack was repeated seven times, each iteration providing a profit of about $1 million.

  


 **Block Data Reference**

The attacker's address:

https://etherscan.io/address/0xd8428836ed2a36bd67cd5b157b50813b30208f50

  


The contract used to perform the attack:

https://etherscan.io/address/0x1c93290202424902a5e708b95f4ba23a3f2f3cee#code

  


Example of the attack execution:

https://etherscan.io/tx/0xeefc22f2dbd8e1b886a7e59f66511e2735f4d04484f6258a9db6e661ed490f7b

  


Victim contract:

https://etherscan.io/address/0x41B856701BB8c24CEcE2Af10651BfAfEbb57cf49#code

  


Transaction of stolen funds transferred to the external wallet:

https://etherscan.io/tx/0xa8a61f779f514e59efa05a98152cf56c1942eff6cc56f506dab7c662ac1e775e


Proof Links:
- [https://medium.com/belt-finance/may-29-incident-report-865d20cc46ca](https://medium.com/belt-finance/may-29-incident-report-865d20cc46ca)
- [ https://rekt.news/belt-rekt/]( https://rekt.news/belt-rekt/)


