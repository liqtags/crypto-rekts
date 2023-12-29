# CoW Swap
![CoW Swap](/rektimages/CoW-Swap.png)
- Amount Lost: $160,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2023-2-7

**Quick Summary**

On Feb. 7, the CoW Swap fee manager contract was drained of worth 160k $USD.

  


 **Details of the Exploit**

The CoW Swap uses external resolvers for swap routing to find the best exchange way. The solver also receives a protocol fee.  granted approval for the malicious contract. 27 Feb the malicious contract was approved by the whitelisted solver. After that, the hacker received an opportunity to drain the fee collector contract.

  


 **Block Data Reference**

Exploit TX: 

https://etherscan.io/tx/0x90b468608fbcc7faef46502b198471311baca3baab49242a4a85b73d4924379b

  


Malicious call:

https://etherscan.io/tx/0x92f906bce94bab417cccc87ae046448d7fb8c2c0350b7ed911545577acb3bfc1

  


Exploiter: 

https://etherscan.io/address/0xc0e82c1ed4786f8b7f806d1b8a6335ec485266ff

https://etherscan.io/address/0x94b6f400df694d0de29f600b15baeed83e95658c

  


  



Proof Links:
- [https://twitter.com/CoWSwap/status/1622885842858508290?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1622885842858508290%7Ctwgr%5Eca0c83eee6765e1bb987662a5abf1de0872d621d%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fforklog.com%2Fnews%2Fdetsentralizovannaya-birzha-cow-swap-poteryala-iz-za-vzloma-166-000](https://twitter.com/CoWSwap/status/1622885842858508290?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1622885842858508290%7Ctwgr%5Eca0c83eee6765e1bb987662a5abf1de0872d621d%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fforklog.com%2Fnews%2Fdetsentralizovannaya-birzha-cow-swap-poteryala-iz-za-vzloma-166-000)
- [ https://twitter.com/MevRefund/status/1622793836291407873]( https://twitter.com/MevRefund/status/1622793836291407873)


