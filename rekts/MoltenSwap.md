# MoltenSwap
![MoltenSwap](/rektimages/MoltenSwap.png)
- Amount Lost: $121,994.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2021-3-7

The Master Chef contract contains hidden functionality under the _set_ () function, which was invoked multiple times by the contract deployer at:  
https://explorer.bitquery.io/bsc/txs/calls?internal=false&contract=0xb9c56744f90f3b8f6da2650485846650c33e7070&method=d9638422  
  
Calling _set_ () function led to the LP tokens transfer onto the external wallet, example transaction:  
https://bscscan.com/tx/0x3b8ed32a339123f0a7abf56abdfe32a86761c2bc2d00f1ebec6c472c4b53de91 (at the bottom of the list)  
  
The liquidity was removed by the external wallet multiple times at:  
https://bscscan.com/tx/0x31c99d77dc9e501838f7586438e967d924989d040e552bb49773dda362e84d55  
https://bscscan.com/tx/0xde655409ea12e50805e237bf2fcb177135c00d8e4e7eefb132471c55ee4887cc  
https://bscscan.com/tx/0x6c9d7e8bbc9dab21adb4ad69494686fc36671bcbb669c840597b476843e4de6b  
https://bscscan.com/tx/0x21d2c374ab9ddae760c409275a944bbe6abb0e4946b1bdcc8f569c1e92e69a10  
https://bscscan.com/tx/0x3a0c56b9c7ccffae75e2b9d9786abb723434ff6db5413e212d866f2fe08cb1bb  
https://bscscan.com/tx/0xdcd892c22e23d93546e9955b1aabd0320fb3b6e96aae3353b47f5b323981b640  
https://bscscan.com/tx/0x9033ed6a75127ee2ab47ba57d89bbcc7fadbf58d4ad00bdeb5a8a69b599f1865  
https://bscscan.com/tx/0x0deb3c9747056218e448a364dd00f1bc63a7b5c2b08e61975d4d2cf0cdd73e5e  
https://bscscan.com/tx/0x53a1f15d43cb2d67614ec67e8d68bca33878497cbe8a1d1c173ade73967da8e0



