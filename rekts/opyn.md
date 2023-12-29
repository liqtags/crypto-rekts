# opyn
![opyn](/rektimages/opyn.png)
- Amount Lost: $371,260.00
- Funds Returned: $371,260.00
- Category: Other
- Date: 2020-8-4

The example transaction of the attack:  
https://etherscan.io/tx/0xd06378b73536e7718895069a5219855774d362db47312dc304dfd4b6e39ef000  
  
This exploit was carried out by using _exercise_ () function with more than two vaults containing ETH as the underlying asset. Because the implementation interprets the same batch of ETH as many batches of ETH receptions, the hacker re-uses that batch of ETH to recover the collateral USDC and profit. Opyn allowed anyone to exercise a vault with underlying assets and oTokens. By burning the oTokens and taking in the underlying assets, the Option Contracts payout collateral assets to the caller of _exercise_ ().  
  
The Opyn ETH Put contract must take in the underlying assets and burn oTokens inside the __exercise_ () method before paying out collateral assets. The _transferFrom_ () function is used to transfer assets from the msg.sender to address(this), which is a very typical approach. When the underlying asset is ETH, the treatment is completely different. In Solidity, msg.value refers to the amount of ETH carried by the current transaction that would be collected by the smart contract with a payable interface (in this example, _exercise_ ()).


Proof Links:
- [https://medium.com/opyn/opyn-eth-put-exploit-c5565c528ad2](https://medium.com/opyn/opyn-eth-put-exploit-c5565c528ad2)
- [ https://blog.peckshield.com/2020/08/05/opyn/]( https://blog.peckshield.com/2020/08/05/opyn/)


