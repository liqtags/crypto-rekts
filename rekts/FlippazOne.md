# FlippazOne
![FlippazOne](/rektimages/FlippazOne.png)
- Amount Lost: $6,828.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-7-5

**Quick Summary**

The creators of the FlippazOne project created a NFT smart contract, which is also an auction contract. The contract included a serious vulnerability in the _ownerWithdrawAllTo()  _function, in which there is no verification of the owner, which allows anyone to take all the funds of the contract through calling this public function.

  


 **Details of the Exploit**

The contract creator of FlippazOne created a contract with a vulnerability that enables anyone to withdraw all $ETH ** ** from the contract to any address. The vulnerability lies in the fact that this function does not have a check on the owner, which means anyone can pick up $ETH tokens to their address at any time. This account with address (https://etherscan.io/address/0x194a39f48f1d5e310d0e0cc25e727c7d2bff0b14) made a bid sending 1.5 $ETH to the FlippazOne contract that were successfully withdrawn by unverified contract (https://etherscan.io/address/0xb314fd4ac6e10a7e27929cbc8db96743739c82b6) in this transaction: https://etherscan.io/tx/0x670da209fb1168941c4565a9a86f87d1011b24b857ea64f658b126a43f031fa0.

Then another 4 $ETH were withdrawn by EOA address in this transaction: https://etherscan.io/tx/0xf2cc19d4c8bfb04e35789e9b716c5f1ba8b893df3a821b104ed5f845230a3762

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Vulnerable contract address: https://etherscan.io/address/0xE85A08Cf316F695eBE7c13736C8Cc38a7Cc3e944

Contract owner and creator: https://etherscan.io/address/0x7f377ee93b2c7856838c9fb7effe0ba34399d9d3



