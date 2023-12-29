# dYdX
![dYdX](/rektimages/dYdX.png)
- Amount Lost: $211,002.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-11-24

Affected contract:  
https://etherscan.io/address/0x53773fE5ff4451c896127Dd2c91b8dE7ac51Ba2C  
  
Timeline:  
  
Nov 27 05:21. The dydX team received a report from a member of a trading firm regarding a vulnerability in the dYdX deposit proxy contract.  
  
Nov 27 06:40. The dYdX team confirmed the bug. They asked samczsun and Georgios from Paradigm to join them in the war room as they respond to the vulnerability.  
  
Nov 27 06:50. The dYdX and Paradigm teams together decided the best course of action is to execute a white-hat hack of vulnerable funds to move them to a safe location.  
  
Nov 27 07:33. As samczsun finished a proof of concept for a white-hat hack, the dydX began implementing the recovery flow in the frontend and implementing a bot to save any additional funds that become vulnerable.  
  
Nov 27 08:01. The dydX determined that ~700 addresses had allowances set on the vulnerable proxy contract. Of these, about 180 had funds at risk, totaling ~$2M.  
  
Nov 27 09:27. The dydX team asked Etherscan to remove the verified source code from the proxy contract and they made the source code on GitHub private.  
  
Nov 27 10:33. The white-hat escrow contract was deployed.  
  
Nov 27 10:56. The _setAllowance_ () function was disabled in the dYdX exchange frontend.  
  
Nov 27 12:04. The first white-hat hack was executed via flashbots.  
  
Nov 27 12:22. The front end was updated to show the warning and recovery process to users affected by the bug. Allowances for deposits were re-enabled using the old deposit flow.  
  
Nov 27 12:32. Announcement was made on Twitter and Discord:  
https://twitter.com/dydxprotocol/status/1464572467872247815?s=20  
  
Nov 27 12:43. The second white-hat hack was executed via flashbots for two more addresses.  
  
Nov 27 13:16. A recovery bot was deployed to automatically retrieve and escrow any more funds that become vulnerable.  
  
As of Dec 8 at 18:00 UTC, $533,000 of additional funds were rescued by the bot, and nearly 80% of affected addresses have revoked approval from the vulnerable contract. Another estimated $211,000 in funds were exploited by frontrunner bots.


Proof Links:
- [https://dydx.exchange/blog/deposit-proxy-post-mortem](https://dydx.exchange/blog/deposit-proxy-post-mortem)


