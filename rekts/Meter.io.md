# Meter.io
![Meter.io](/rektimages/Meter.io.png)
- Amount Lost: $4,400,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-2-6

The attacker's address:  
https://etherscan.io/address/0x8d3d13cac607B7297Ff61A5E1E71072758AF4D01  
  
The attacker minted a substantial amount of BNB and WETH tokens, draining the bridge reserve of its BNB and wETH before all bridge transactions could be halted by Meter. This case also impacted the Hundred Finance on Moonriver.  
  
Meter_io Passport is a fork of ChainSafe's ChainBridge, but with one change introduced to the deposit method of the ERC20 Handler.  
  
The extended code had a wrong trust assumption which allowed the hacker to call the underlying ERC20 deposit function to fake a BNB or ETH transfer.  
  


Exploit scenario:

\- the Meter Bridge Contract provided by ChainSafe Systems has a vulnerability in _deposit_ () function

\- _deposit_ () function doesn't check _calldata_ "data" parameter to be matched with the message value in the function call

\- this vulnerability allows anybody to call this function with fake deposit data and not be reverted

the attacker exploited this vulnerability and make a few deposits from the Ethereum network:

https://etherscan.io/tx/0xdfea6413c7eb3068093dcbbe65bcc9ba635e227c35e57fe482bb5923c89e31f7

https://etherscan.io/tx/0x2d3987963b77159cfe4f820532d729b0364c7f05511f23547765c75b110b629c

\- the attacker exploited this vulnerability and made a few deposits from the BSC network:

https://bscscan.com/tx/0xc4d7e160c7652f2db22681aa2777c5b37937bf30375c5b2c6b2bd172ae984950

https://bscscan.com/tx/0x63f37aff7e40b85b0a6b3fd414389f6011cc09b276dc8e13b6afa19061f7ed8e

https://bscscan.com/tx/0xc7eb98e00d21ec2025fd97b8a84af141325531c0b54aacc37633514f2fd8ffdc

\- the attacker called _swapOut()_ to withdraw a fake deposited amount from another chain:

https://moonriver.moonscan.io/tx/0xb3298f62504423a97db6a6fc4132e6bf1f4225b1e7deb33260495254280d7050

\- the attacker used AnySwap and cBridge to collect all funds in the Ethereum address  
  
Stolen funds were deposited into Tornado Cash mixer on Ethereum:  
https://bloxy.info/txs/transfers_from/0x8d3d13cac607b7297ff61a5e1e71072758af4d01?currency_id=1


Proof Links:
- [https://twitter.com/Meter_IO/status/1490103308421255168](https://twitter.com/Meter_IO/status/1490103308421255168)
- [ https://twitter.com/ishwinder/status/1490227406824685569]( https://twitter.com/ishwinder/status/1490227406824685569)
- [ https://rekt.news/meter-rekt/]( https://rekt.news/meter-rekt/)
- [ https://twitter.com/peckshield/status/1490121762847092736]( https://twitter.com/peckshield/status/1490121762847092736)


