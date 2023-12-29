# SharkTron
![SharkTron](/rektimages/SharkTron.png)
- Amount Lost: $10,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2020-10-28

**Quick Summary**

Malicious function in the staking contract allowed the contract deployer to transfer 229M TRX from it. The tokens were then spread to different EOAs and exchanges.

  


 **Details of the Exploit**

The contract deployer had the ability to call the rrInfo() function in the staking contract, which was designed for the malicious transfer of TRX from it. An example of this function calling resulted in a 1M TRX transfer. The code of the smart contract isn’t verified. The deployer then bought SRX and SWD on JustSwap. There was another malicious function, getAllT(), which was used to perform a rug pull, removing 229M TRX from the staking contract. These TRXs were then sent to other EOAs.

  


 **Block Data Reference**

  


The contract deployer:

https://tronscan.org/#/address/TJTAYhG2EwqWuMF6v1UFP3KqZXX32UBtdz

  


Example of the function calling (1M TRX transfer):

https://tronscan.org/#/transaction/f1aa69f5bb2c70572006ffc7b94f8b000c1f047d00b57224357cbd0bce80b1f7

  


Transaction of 229M TRX removed from staking contract:

https://tronscan.org/#/transaction/f381e7d013022504257e02d3e6b51bef247ed94b8e916999dbb33a3e07a919af

  


Transactions of TRXs sent to other EOAs:

https://tronscan.org/#/transaction/793669f6efa3321704c06578a6941fca6f4a098512c7ff9808802c90da5fbd4f

https://tronscan.org/#/transaction/c1bf2b328ce16f53d65908b21d128ca7e5492ec848f9f3cf8a577ea907a9e460

https://tronscan.org/#/transaction/e68088aff5aa8dd688faa4b7b4d679aed5e74fc2969036207d07da8f12cc3fb8

https://tronscan.org/#/transaction/657315fb2bd3e3581376d691b26f87691166927273cbd937243dfcdb52b3128f


Proof Links:
- [https://news.bitcoin.com/sharktron-defi-project-devs-exit-scam-tron-foundation-says-part-of-missing-funds-now-frozen/](https://news.bitcoin.com/sharktron-defi-project-devs-exit-scam-tron-foundation-says-part-of-missing-funds-now-frozen/)
- []()


