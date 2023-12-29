# Cream Finance
![Cream Finance](/rektimages/Cream-Finance.png)
- Amount Lost: $36,154,954.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2021-8-31

**Quick Summary**

Cream Finance got exploited through a vulnerability hidden in the borrow() function, which was repeatedly utilized for reentrancy attacks. The attacker made away with approx. $36 million.

  


 **Details of the Exploit**

Cream (Crypto Rules Everything Around Me) Finance is a decentralized lending protocol designed for institutions, protocols and people in order to access financial services.

The risk for reentrancy arose because of the way $AMP was integrated into the protocol. The $AMP token contract is based on the ERC777 standard, which utilizes the _callPostTransferHooks hook. The attack transactions started with supplying $ETH as a collateral for borrowing $AMP from the crAMP market. When transferring AMP to the attacking contract, the _callPostTransferHooks was called, which in turn triggered the execution of a fallback function in the attack contract allowing the latter to re-enter the crETH market to borrow $ETH against the very same collateral initially supposed to be used for borrowing $AMP.

The flow of an example exploit transaction: https://etherscan.io/tx/0xa9a1b8ea288eb9ad315088f17f7c7386b9989c95b4d13c81b69d5ddad7ffe61e

\- The hacker creates contract A to flash loan 500 $WETH and use the funds as collateral on cream, minting 24.17k crETH;

\- borrows 19.48M $AMP for the received crETH;

\- exploits the reentrancy possibility by repeatedly calling borrow() during the token transfer, taking a further 355 $ETH before the state of the initial borrow() has been updated;

\- uses contract B, which receives a half (9.74M) of A's borrowed $AMP;

\- contract B liquidates part of A's loan, redeeming 187 $WETH and transferring it back to contract A;

\- contract A uses $ETH borrowed via reentrancy to repay the remainder of the flash loan.

  


The profits of the above explained transaction amounted to 41 $ETH and 9.74M $AMP.

In total, 17 attack transactions were conducted netting the attackers a total of $AMP 462,079,976 and $ETH 2,804.96.

  


 **Block Data Reference**

Attack contract A:

https://etherscan.io/address/0x38c40427efbaae566407e4cde2a91947df0bd22b

Attack contract B:

https://etherscan.io/address/0x0ec306D7634314D35139d1dF4A630d829475A125

Exploiter address 1:

https://etherscan.io/address/0xce1f4b4f17224ec6df16eeb1e3e5321c54ff6ede

Exploiter address 2:

https://etherscan.io/address/0x8036EbD0Fc9C120BA0469ffCB27b204AA06aaF1F

  



Proof Links:
- [https://medium.com/cream-finance/c-r-e-a-m-finance-post-mortem-amp-exploit-6ceb20a630c5](https://medium.com/cream-finance/c-r-e-a-m-finance-post-mortem-amp-exploit-6ceb20a630c5)
- [ https://rekt.news/cream-rekt/]( https://rekt.news/cream-rekt/)


