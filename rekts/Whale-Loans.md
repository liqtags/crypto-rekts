# Whale Loans
![Whale Loans](/rektimages/Whale-Loans.png)
- Amount Lost: $12,374.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-6-20

Whale Loans was exploited due to K-check of the WhaleSwap Finance Pair contract. When a user swaps, there is an issue with the magnitude of the parameters passed in. 

The attacker flashloaned [](https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955)BSC-USD and then returns flashloan with a K-check parameter in function _swap()_ contract WhaleswapPair.sol of magnitude 10000^4. However, the K-check takes a parameter of magnitude 10000^2, which causes the K-check to fail.

  


Exploiter address: https://bscscan.com/address/0xd793ff8d744828c25da7f80123b88dd5c2bf7a50

Attack transaction: https://bscscan.com/tx/0x9f5b02cb1ce2d75ba457a2d152d89b6d3932ff057c03739a0071fb816e0ebab3

Attacker contract: https://bscscan.com/address/0xf95536755732544e41baad22f1c79d1ee529385f

Victim address: https://bscscan.com/address/0x8bfee2caff6b5d4ac9f438f4b1f36feeb5e76794


Proof Links:
- [https://www.certik.com/resources/blog/2V34hTMNWst97BQA62FaBf-whale-loans-incident-analysis](https://www.certik.com/resources/blog/2V34hTMNWst97BQA62FaBf-whale-loans-incident-analysis)


