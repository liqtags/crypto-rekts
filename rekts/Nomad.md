# Nomad
![Nomad](/rektimages/Nomad.png)
- Amount Lost: $190,000,000.00
- Funds Returned: $36,342,325.00
- Category: Bridge
- Date: 2022-8-1

**Quick Summary**  
The Nomad bridge was exploited for aprox. $190 million by what has to be declared as Web3`s first "crowd-looting" event.  
 **  
Details of the Exploit**

The Nomad bridge is an interoperability protocol that connects five different blockchains, namely Avalanche, Ethereum, Evmos, Milkomeda C1 and Moonbeam. The initial attack appears to have taken place with this transaction, where 100 (WBTC) were extracted from the protocol; https://etherscan.io/tx/0x61497a1a8a8659a06358e130ea590e1eed8956edbd99dbb2048cfb46850a8f17. This hack was made possible by an operational error incurred by the team, which had been found and commented upon in an audit report made by Quantstamp. Essentially, at the initialization of the contract the "process()" function checks messages for an acceptable merkle root. The team accidentally marked the zero root (0x00) as acceptable. This error enabled every message to be auto-proven by default. Essentially, the attacker was able to process transactions without any proving by calling the function "process()".

This information spread within the community and all that was needed to participate in the looting of the protocol was finding a transaction that worked and copy-pasting the transaction with the wallet of desire at the receiving end. This is the reason why tokens were predominantly extracted in the exact same denomination.

  


The initial attack was followed by hundreds of EOA`s extracting assets such as $WBTC, $FXS, $C3, $DAI, $USDC from the bridge. Amongst the looters were reputable hackers from other exploits such as the Rari Capital Exploiter as well as White hat hackers who intend to return the funds.

  


As the time of this writing approx. $32 million have been returned to the Nomad Recovery Funds Address https://etherscan.io/address/0x94A84433101A10aEda762968f6995c574D1bF154 by white hat hackers and cooperating culprits.

  


  


 **Block Data Reference**

Attacker address: https://etherscan.io/address/0x56d8b635a7c88fd1104d23d632af40c1c3aac4e3

Attacker contract address: https://etherscan.io/address/0xf57113d8f6ff35747737f026fe0b37d4d7f42777

Attack transactions: 

1) https://etherscan.io/tx/0x61497a1a8a8659a06358e130ea590e1eed8956edbd99dbb2048cfb46850a8f17

2) https://etherscan.io/tx/0x29b67e0701ddd910ff6a069aa039015eb78b1ee6d99ad8da5d0ef63916f3fd57

3) https://etherscan.io/tx/0xdf6bef0d8dee8b44863ac61092a711b877dcfe3d61da93d7289e0c6285af1b45

4) https://etherscan.io/tx/0x3dbed4a1ebb2289273370ce0ef10302882927abe946299cf2ca3073f1a3dcdd9

  


Nomad Recovery Funds Address:

https://etherscan.io/address/0x94A84433101A10aEda762968f6995c574D1bF154


Proof Links:
- [https://cointelegraph.com/news/nomad-token-bridge-drained-of-190m-in-funds-in-security-exploit](https://cointelegraph.com/news/nomad-token-bridge-drained-of-190m-in-funds-in-security-exploit)
- [ https://www.coindesk.com/tech/2022/08/02/nomad-bridge-drained-of-nearly-200-million-in-exploit/]( https://www.coindesk.com/tech/2022/08/02/nomad-bridge-drained-of-nearly-200-million-in-exploit/)
- [ https://www.livemint.com/news/world/cryptocurrency-how-nomad-token-bridge-hack-took-place-that-drained-nearly-200-million-funds-in-exploit-11659418968336.html]( https://www.livemint.com/news/world/cryptocurrency-how-nomad-token-bridge-hack-took-place-that-drained-nearly-200-million-funds-in-exploit-11659418968336.html)


