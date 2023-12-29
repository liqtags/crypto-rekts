# Omni Bridge
![Omni Bridge](/rektimages/Omni-Bridge.png)
- Amount Lost: $271,800.00
- Funds Returned: $0.00
- Category: Bridge
- Date: 2022-9-16

**Quick Summary**

Omni Bridge was hacked by exploiting a smart contract on the EthereumPoW chain. 200 $WETH was stolen by a replay attack and transferred through Mexc Global.

  


 **Details of the Exploit**

Omni Bridge is a crosschain bridge. A replay attack was launched against Omni Bridge on the EthereumPoW chain, which resulted in a hacker exploiting 200 $WETH. The hacker was able to withdraw bridged funds from the both EthereumPoS and EthereumPoW chains because the OmniBridge contract failed to validate chainId before approving the transaction.

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0x82faed2da812d2e5cced3c12b3baeb1a522dc677

OmniBridge address:

https://etherscan.io/address/0x8eb3b7d8498a6716904577b2579e1c313d48e347

EthereumPoS transaction:

https://etherscan.io/tx/0xbddb0cc8bc9949321e1748f03503ed1a20dd618fbf0a51dc5734c975b1f8bdf5

EthereumPoW transaction:

https://www.oklink.com/en/ethw/tx/0x9c072551861ce384203516f4d705176a2d2e262d5b571d853467425f1a861fb4


Proof Links:
- [https://cryptoslate.com/ethereum-pow-loses-200-weth-to-omni-bridge-vulnerability-exploit/](https://cryptoslate.com/ethereum-pow-loses-200-weth-to-omni-bridge-vulnerability-exploit/)


