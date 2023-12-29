# DEUS Finance
![DEUS Finance](/rektimages/DEUS-Finance.png)
- Amount Lost: $17,900,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-4-28

**Quick Summary**

DEUS Finance was exploited through flash loan and oracle manipulation, resulting in a significant loss.

  


 **Details of the Exploit**

The attacker initiated the exploit by flash loaning 143.2m USDC, which was then swapped to 9.5m DEI via sAMM-USDC/DEI_USDC-DEI, causing an increase in DEI price. 71k DEI was used as collateral to borrow 17.2k DEI from DeiLenderSolidex, and the flash loan was repaid. The attacker was initially funded via Multichain, with the origin of funds coming from an Ethereum address. After the attack, the profit was deposited back to the same Ethereum address.

  


 **Block Data Reference**

The attacker's address:

https://ftmscan.com/address/0x701428525cbac59dae7af833f19d9c3aaa2a37cb

The transaction behind the attack:

https://ftmscan.com/tx/0x39825ff84b44d9c9983b4cff464d4746d1ae5432977b9a65a92ab47edac9c9b5

The Ethereum address where the funds originated and were returned:

https://etherscan.io/address/0x701428525cbac59dae7af833f19d9c3aaa2a37cb

The Tornado Cash mixer where the stolen funds were deposited:

https://bloxy.info/txs/transfers_from/0x701428525cbac59dae7af833f19d9c3aaa2a37cb?currency_id=1


Proof Links:
- [https://twitter.com/DeusDao/status/1519574219419496449](https://twitter.com/DeusDao/status/1519574219419496449)
- [ https://twitter.com/lafachief/status/1519624600719663106]( https://twitter.com/lafachief/status/1519624600719663106)
- [ https://twitter.com/peckshield/status/1519530463337250817]( https://twitter.com/peckshield/status/1519530463337250817)


