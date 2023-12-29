# Fantom
![Fantom](/rektimages/Fantom.png)
- Amount Lost: $62,500.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-7-1

**Quick Summary**

A validator wallet was drained for 250k FTM by an attacker during the node setup process on Fantom network. The problem is a go-opera code bug, allowing users to unlock the local account with http/ws enabled.

  


 **Details of the Exploit**

The attacker tracked the transfers to the node accounts, so he could know when and how much a validator account would receive, and taking advantage of the vulnerability, was able to steal money from the node validator. The vulnerability is in the _UnlockAccount()  _function, in which the _ExtRPCEnabled()_ flag does not work correctly, which makes the entire security check useless.

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**



