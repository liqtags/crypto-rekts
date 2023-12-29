# Horizon by Harmony
![Horizon by Harmony](/rektimages/Horizon-by-Harmony.png)
- Amount Lost: $100,000,000.00
- Funds Returned: $1,400,000.00
- Category: Bridge
- Date: 2022-6-23

**Quick Summary**

Harmony's Horizon Bridge was exploited by an attacker resulting in losses of roughly $100M. The bridge was secured by multisig wallet which needed 2 out of 5 wallets to confirm transaction. The hacker gained control over 2 wallets which enabled the attacker to drain the funds of the bridge and transfer said funds to his wallet.

  


 **Details of the Exploit  **

For yet unspecified reasons the attacker gained access over 2 of the 5 multisig wallets.

The attacker was able to enter and confirm transactions by himself. The exploit resulted in the loss of: ETH, USDC, WBTC, USDT, DAI, BUSD, AAG, FXS, SUSHI, AAVE, WETH, and FRAX. The ONE token was not affected by this attack.

  


For more context, bridges in DeFi are used to enable interoperability between blockchains. Through bridges a user of DeFi may pursue opportunities in an ecosystem that is not native to the coins or tokens a user is holding. For example through Harmony's Horizon Bridge a user holding $ETH on the Ethereum network could bridge $ETH over to the Harmony blockchain receiving newly minted wrapped $1ETH on a 1:1 ratio. 

  


Since the funds on the bridge were seized by the attacker, the receipt was no longer backed by the collateral on a 1:1 ratio. The depreciation of the wrapped assets were felt by users in the form of massive slippages on dexes and other bridges as users tried to flee the Harmony Ecosystem.

  


Below a breakdown of the specific function used by the attacker.

  


1) The multisig owner called the _submitTransaction(),  _then to confirm owner calls confirmTransaction() from the MultiSigWallet with the input transactionId 21106.

2) The executeTransaction() function has made an external call with input that will call the unlockEth() function in the Ethmanager contract. The input specifies the amount, recipient, and receiptId to be passed to the unlockEth() function.

3) The following steps were repeated with different ids.

  


 **Block Data Reference**

Attacker transactions:

640K BUSD: https://bscscan.com/tx/0x4ed7941394725e49e7423e56553901c4ce841792c70e87adeee282cd78500668

Link to attacker draining bridge for ERC20 tokens: https://etherscan.io/address/0x0d043128146654c7683fbf30ac98d7b2285ded00#tokentxns

  


Multisig wallet addresses that were compromised:

1) https://etherscan.io/address/0xf845a7ee8477ad1fb4446651e548901a2635a915

2) https://etherscan.io/address/0x812d8622c6f3c45959439e7ede3c580da06f8f25

These addresses confirmed the transaction with id 21108. It can be checked by this multisig wallet (https://etherscan.io/address/0x715CdDa5e9Ad30A0cEd14940F9997EE611496De6#readContract) in the _getConfirmations()  _function.

  


Attacker addresses:

1) https://etherscan.io/address/0x0d043128146654c7683fbf30ac98d7b2285ded00

2) https://etherscan.io/address/0x58f4baccb411acef70a5f6dd174af7854fc48fa9

3) https://etherscan.io/address/0x9e91ae672e7f7330fc6b9bab9c259bd94cd08715

4) https://etherscan.io/address/0x1ec6f83b55c3f4cefc630442716872ba15f16430

5) https://etherscan.io/address/0x432a9cb4353bed67ec5351734d4a44c0826847ae

6) https://etherscan.io/address/0x4507ac1bdf4ae5e61ffcec3a9aeda312e2505970

7) https://etherscan.io/address/0x8a0858888beeb5d1435ecd3657831699f169c3f4

  


Victim addresses:

Harmony ETH Bridge: https://etherscan.io/address/0xf9fb1c508ff49f78b60d3a96dea99fa5d7f3a8a6

Harmony ERC20 Bridge: https://etherscan.io/address/0x2dCCDB493827E15a5dC8f8b72147E6c4A5620857

Harmony BUSD Bridge: https://etherscan.io/address/0xfd53b1b4af84d59b20bf2c20ca89a6beeaa2c628

  


Funds from the Harmony hack are being laundered via Tornado Cash mixing services. In total 42,000 ETH ~$44,7m have been laundered as the time of writing.


Proof Links:
- [https://rekt.news/harmony-rekt/](https://rekt.news/harmony-rekt/)
- [ https://www.certik.com/resources/blog/2QRuMEEZAWHx0f16kz43uC-harmony-incident-analysis]( https://www.certik.com/resources/blog/2QRuMEEZAWHx0f16kz43uC-harmony-incident-analysis)
- [ https://www.cnbc.com/2022/06/24/hackers-steal-100-million-in-crypto-from-harmonys-horizon-bridge.html]( https://www.cnbc.com/2022/06/24/hackers-steal-100-million-in-crypto-from-harmonys-horizon-bridge.html)
- [ https://techcrunch.com/2022/06/24/harmony-blockchain-crypto-hack/]( https://techcrunch.com/2022/06/24/harmony-blockchain-crypto-hack/)


