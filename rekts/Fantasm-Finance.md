# Fantasm Finance
![Fantasm Finance](/rektimages/Fantasm-Finance.png)
- Amount Lost: $2,622,097.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-3-9

The exploiter's address:  
https://ftmscan.com/address/0x47091e015b294b935babda2d28ad44e3ab07ae8d  
  
The exploiter:  
\- deployed contract to trigger the exploit  
https://ftmscan.com/address/0x944b58c9b3b49487005cead0ac5d71c857749e3e  
  
\- minted XFTM by input only FSM token without entering any FTM  
\- collected XFTM token  
\- sold XFTM token to FTM  
\- bought more FSM and repeated the first step to get a larger amount of FTM  
\- sold all his FTM for ETH and bridged these ETH to Ethereum via Celer Bridge  
\- deposited stolen funds into Tornado Cash mixer:  
https://etherscan.io/address/0x47091e015b294b935babda2d28ad44e3ab07ae8d  
  
That contract exploited the error in Fantasm’s Pool contract where the developer missed the condition checking for the minimum amount of input FTM when minting XFTM.


Proof Links:
- [https://medium.com/@fantasmfinance/fantasm-finance-post-mortem-exploit-09-march-2022-daf48ead016f](https://medium.com/@fantasmfinance/fantasm-finance-post-mortem-exploit-09-march-2022-daf48ead016f)
- [ https://twitter.com/PeckShieldAlert/status/1501743350869012481]( https://twitter.com/PeckShieldAlert/status/1501743350869012481)


