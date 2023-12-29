# BabyDAO
![BabyDAO](/rektimages/BabyDAO.png)
- Amount Lost: $7,602.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-7-6

**Quick Summary**

The $BabyDAO token has been rugpulled by the token creator for $7.6k. Then funds where sent to another address from which they were laundered via Tornado.cash.

  


 **Details of the Exploit**

The token creator deployed a BabyDAO contract, where 10T tokens were minted to his account (https://bscscan.com/tx/0x3af2f636d7b5b2965f818fd374b1c7b6cb9d0b697375b2e1c50a823043650e88).

After the token deployment, the scammer address created a pair on PancakeSwap of $10 WBNB and $100M BabyDAO (https://bscscan.com/tx/0x8ad196e570fc4382c343c9fe0c706715ee94d362515bba83c4f663068f8f183b).

After 14 days, 300 $BNB was sent to the deployer's address, of which 290 $BNB was used to increase the liquidity pool on PancakeSwap.

Transfer transactions to deployer's address: https://bscscan.com/tx/0x166c1cedcbcfc9bafbd4c15ec55e633a4070167d4706eee0109c370061231429

Adding liquidity to PancakeSwap: https://bscscan.com/tx/0x67e83954bd116ff9145146d267e3722405671e66c5495dfea09581843bccec3c

When the price of the token went up, the deployer removed liquidity and took a profit of 32.25 $WBNB. All the funds were transferred to another address where funds were laundered via Tornado.cash.

Transferring funds to address from which funds were laundered via Tornado.cash: https://bscscan.com/tx/0x40a34d6f65a8155e15d4b72955ced2ab1a8f3bff1d5d365072c7407d04a31ea3

  


As the time of this writing information on this case is scarce **. More sources will be added if the case should develop.**

  


 **Block Data Reference**

Creator address: https://bscscan.com/address/0xe153c4b638d2c5db64adf804bd7410203e29c78a

The address to which the tokens were sent for laundering via Tornado.cash: https://bscscan.com/address/0xd759da5909237b687fc53bab9dd92bfd8deb7f0a

Token address: https://bscscan.com/address/0xf2d5d38fa88f9e2be0830351275d0724f96b0f5f


Proof Links:
- [https://dexscreener.com/bsc/0xf2d5d38fa88f9e2be0830351275d0724f96b0f5f](https://dexscreener.com/bsc/0xf2d5d38fa88f9e2be0830351275d0724f96b0f5f)


