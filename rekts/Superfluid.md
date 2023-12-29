# Superfluid
![Superfluid](/rektimages/Superfluid.png)
- Amount Lost: $20,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-2-8

**Quick Summary**

Superfluid protocol was exploited which lead to a loss of project funds for roughly 20,000,000 $USD.

  
 **Details of the Exploit**  
Superfluid is a streaming protocol for real-time crypto transfers. On February 8, 2022, an attacker exploited Superfluid’s host contract by passing in faulty calldata, which allowed them to create distribution indexes spoofing several different accounts that held Super-tokens. This vulnerability enabled the attacker to move funds from Superfluid user wallets to exchanges on Polygon and swap them to ETH. The funds currently sit in the attacker’s wallet.

In total, 11,008 MATIC, 1,507,931 MOCA, 28 ETH, 39,357 sdam3CRV, 19,387,874 QI, 44,581 SDT, 23,653 STACK, and 562,834 USDC were stolen by the attacker. At the time of writing, over 2,700 ETH is sitting in the attacker’s wallet, as well as 500,000 MOCA.  
  
 _callAgreement_ () function was exploited by replacing the bytes memory callData parameter. This parameter contains ctx value which can be decoded to get such properties: timestamp, msgSender, agreementSelector, userData, appAllowanceGranted, appAllowanceWanted, appAllowanceUsed, appAddress, appAllowanceToken. Ctx was replaced with the fake one, so the attacker was able to drain all SuperToken contract funds.

  


 **Block Data Reference**  
Attacker address:  
https://polygonscan.com/address/0x1574f7f4c9d3aca2ebce918e5d19d18ae853c090

  


Malicious transaction:  
https://polygonscan.com/tx/0x396b6ee91216cf6e7c89f0c6044dfc97e84647f5007a658ca899040471ab4d67

  


Malicious contract:

https://polygonscan.com/address/0x32d47ba0affc9569298d4598f7bf8348ce8da6d4  
  
Claim transaction:  
https://polygonscan.com/tx/0xdee86cae2e1bab16496a49b2ec61aae0472a7ccf06f79744d42473e96edd6af6


Proof Links:
- [https://twitter.com/QiDaoProtocol/status/1490944375165128706](https://twitter.com/QiDaoProtocol/status/1490944375165128706)
- [ https://beincrypto.com/qidao-experiences-exploit-of-superfluid-smart-contract-code-20m-estimated-to-be-lost/]( https://beincrypto.com/qidao-experiences-exploit-of-superfluid-smart-contract-code-20m-estimated-to-be-lost/)
- [ https://twitter.com/Superfluid_HQ/status/1491045880107048962]( https://twitter.com/Superfluid_HQ/status/1491045880107048962)


