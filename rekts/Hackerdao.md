# Hackerdao
![Hackerdao](/rektimages/Hackerdao.png)
- Amount Lost: $65,155.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-5-24

On May 24th, Hackerdao token contract was attacked for 200BNB. The WBNB-Hackerdao pair has been drained in this transaction 0x04673c950....

  


Attacker transaction: https://bscscan.com/tx/0x04673c95054247588bb8380dbc7d361f08f8f0baa319366f48ad46e51d08422d

Blocksec transaction: https://versatile.blocksecteam.com/tx/bsc/0x04673c95054247588bb8380dbc7d361f08f8f0baa319366f48ad46e51d08422d

Attacker address: https://bscscan.com/address/0xcFc591dB031B760961Fe8943a183741ED7Cd1f82

Attacker contract: https://bscscan.com/address/0x24cb6980995aeb7d5a9204e04b17dcd1e99a4694

Victim contract: https://bscscan.com/address/0x94e06c77b02Ade8341489Ab9A23451F68c13eC1C

  


Attack step by step:

1) The attacker used the logic of the Hackerdao contract vulnerability, in which the _transfer function incorrectly processes the uniswapV2 pair.

2) Then, if the recipient's address is the specified Uniswap pair (BSCUSD-Hackerdao pair, 0xbdb426a2fc2584c2d43dba5a7ab11763dfae0225), the additional commission amount will be further reduced from the sender. This leads to a typical pattern of token attacks: if the balance of a Uniswap pair can be reduced without any swap (i.e. the difference between the recorded reserves and the actual token balances), there is a possibility of price manipulation.

3) The attack is carried out by switching from a pair of WBNB-Hackerdao to a pair of BSCUSD-Hackerdao, which leads to an unbalanced price.



