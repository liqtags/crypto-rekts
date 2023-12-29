# Rari Fuse
![Rari Fuse](/rektimages/Rari-Fuse.png)
- Amount Lost: $79,749,026.00
- Funds Returned: $79,749,026.00
- Category: Borrowing and Lending
- Date: 2022-4-30

**Quick Summary**

Seven of Rari's Fuse pools were drained due to re-entrancy attack. The total amount of losses is ~$80m.

  


 **Details of the Exploit**

 **Rari enables the creation of so-called Fuse Pools permissionless lending pools that anyone with a wallet can access from anywhere to lend or borrow ERC-20 tokens.**

The attack drained Rari's pools while Rairy's pools were unaffected. Fei Rari uses a fork of the Compound code that doesn't follow the check-effect-interaction pattern which the attacker took advantage making a re-entrancy attack via CEther which uses call.value to send ETH.

  


Attack flow:

1) Attacker flash loaned 150m USDC and 50k WETH

2) Deposited 150m USDC as collateral into fUSDC-127 contract for loans. This contract is a fork of vulnerable smart-contract of Compound protocol.

3) The attacker borrows 1,977 ETH via _borrow()_ function

4) As the _borrow()  _function does not follow the check-effect-interaction pattern and transfers ETH to the attacker’s contract before updating the attacker’s borrow records.

5) As the attacker’s borrow record not updated, the attacker made a re-entrant call to _exitmarket()_ that allows the attacker to withdraw his collateral.

The attacker repeated the following actions, repaid the flash loan, and kept the remaining profit for himself.

  


Funds lost:

  * ETH - 6 037.81

  * FEI - 20 251 603.11

  * DAI - 14 278 990.68

  * LUSD - 1 948 952.18

  * USDC - 10 055 556.33

  * USDT - 132 959.90

  * RAI - 31 615.87

  * FRAX - 13 101 364.94

  * UST - 2 765 891




Total lost in USD: 79 749 026$

 **Update 22.09.2022:**

Tribe DAO which is a conglomerate of Midas Capital, Rari Capital, Fei Protocol and Volt Protocol has passed an on-chain vote with 99% consent to fully reimburse the $80m in losses victims suffered in the Rari capital exploit.

 **Block Data Reference**

Attacker Address: https://etherscan.io/address/0x6162759eDAd730152F0dF8115c698a42E666157F

Attack transactions: 

ETH: https://etherscan.io/tx/0xab486012f21be741c9e674ffda227e30518e8a1e37a5f1d58d0b0d41f6e76530

Arbitrum: https://arbiscan.io/tx/0x3212d091792f81f18a31aab753de6b3128d79dcb5e8392167249595f813203ef

Attacker contracts:

1) https://etherscan.io/address/0xE39f3C40966DF56c69AA508D8AD459E77B8a2bc1

2) https://etherscan.io/address/0x32075bad9050d4767018084f0cb87b3182d36c45


Proof Links:
- [https://www.certik.com/resources/blog/6LiXVtPQ8q5AQfqOUPnTOS-revisiting-fei-protocol-incident](https://www.certik.com/resources/blog/6LiXVtPQ8q5AQfqOUPnTOS-revisiting-fei-protocol-incident)
- [ https://coingape.com/fei-protocol-exploited-80-mln-tornado-cash/]( https://coingape.com/fei-protocol-exploited-80-mln-tornado-cash/)
- [ https://coinyuppie.com/fei-protocol-attack-event-analysis-how-to-break-the-reentrancy-vulnerability/]( https://coinyuppie.com/fei-protocol-attack-event-analysis-how-to-break-the-reentrancy-vulnerability/)
- [ https://decrypt.co/99103/fei-protocol-offers-10m-bounty-after-80m-rari-capital-exploit]( https://decrypt.co/99103/fei-protocol-offers-10m-bounty-after-80m-rari-capital-exploit)


