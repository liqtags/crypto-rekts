# Nerve Finance
![Nerve Finance](/rektimages/Nerve-Finance.png)
- Amount Lost: $585,882.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-11-14

The attacker:  
https://bscscan.com/address/0xd5476194bdc298b6981f5414b693363f94d69228  
  
The transaction behind the attack:  
https://bscscan.com/tx/0xea95925eb0438e04d0d81dc270a99ca9fa18b94ca8c6e34272fc9e09266fcf1d  
  
The attacker:  
\- borrowed 50,000 BUSD using a flash loan from Fortube  
  
\- swapped 50,000 BUSD for 50,351 fUSDT from Ellipsis  
  
\- invoked the swap function of MetaSwap to swap 50,351 fUSDT for 36,959 Nerve 3-LP with a relatively big slippage  
  
\- invoked the _removeLiquidityOneCoin()_ function of Nerve.3pool with the LP tokens (received in the previous step) to remove the liquidity of BUSD, i.e., 37,071 BUSD  
  
\- invoked the _swapUnderlying()_ function of MetaSwap to swap BUSD for fUSDT, and received 51,494 fUSDT.  
  
The attacker repeatedly executed the above steps to drain the liquidity of the MetaPool and finally harvested 900 BNB.  
  
Stolen funds were deposited into Tornado Cash mixer:  
https://bscscan.com/tx/0xcf43eefbfd8cf94a8daeaa5b05d9530782852018f487927be2dd391ed50aec90  
https://bscscan.com/tx/0x55bd06a000af99dc662685b69f5d093905f07bee5e7b9e84b5c4adf2d8190a53  
https://bscscan.com/tx/0x2dbc18c67be69213497b250934e877306fa7763de8b4d7787ff9c0d61e23067b  
https://bscscan.com/tx/0x17cd04cb3f3162eb983af4eb74bf8a0c0804da9f95733f8311c605c77e334e7c  
https://bscscan.com/tx/0xe5a0a0588b3d1e615b82c30a8baba83b0b700f8a3fa6abc19db82527ce4fa1f4  
https://bscscan.com/tx/0x16ec28d4c386b6ee34488739122d0d75c4e7c4cd699af999bbe7d278b1896581  
https://bscscan.com/tx/0x7f6b43137d3787626613f0908f92af4c589fd20491dc21384ba84eca780bb3c1  
  
The rest were bridged though AnySwap:  
https://bscscan.com/tx/0x0348cc9220d3b2b1c47f5e15d2a3a7746356332ed979e7c21dff1060302332a6  
  
The swap function ignores the impact of the virtual price, which means the value of the LP token will be underestimated and more LP tokens could be swapped out. As a result, it is possible to harvest more pool stablecoins by first fetching back the liquidity of the underlying stablecoins with the corresponding LP token, and then swapping pool stablecoins by invoking the _swapUnderlyin_ g() function.


Proof Links:
- [https://halborn.com/explained-the-synapse-and-nerve-bridge-hacks-november-2021/](https://halborn.com/explained-the-synapse-and-nerve-bridge-hacks-november-2021/)
- [ https://blocksecteam.medium.com/the-analysis-of-nerve-bridge-security-incident-ead361a21025]( https://blocksecteam.medium.com/the-analysis-of-nerve-bridge-security-incident-ead361a21025)


