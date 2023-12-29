# Numbers Protocol
![Numbers Protocol](/rektimages/Numbers-Protocol.png)
- Amount Lost: $13,836.00
- Funds Returned: $0.00
- Category: NFT
- Date: 2022-11-23

**Quick Summary**

On the 23rd Of Nov, 2022, the Numbers Protocol was exploited, resulting in the loss of approximately 13,836 $USD.

  


 **Details of the Exploit**

On November 23, 2022, an attack occurred on the Numbers Protocol ($NUM token) on the Ethereum chain, resulting in a loss of approximately $13,836. The root cause of the vulnerability was because the NUM token was incompatible with the Multichain, a cross-chain router protocol. The NUM token lacked a permit function required by the Router protocol, but it did have a default callback function which allowed forged signature to be passed in to trick the cross-chain bridge into transferring the user's assets. The attacker created a fake token using the attack contract which used $NUM as its underlying token, then called the anySwapOutUnderlyingWithPermit function of the Multi-Chain Router contract to drain 557,754.45000198 $NUM tokens from one of the victim users. This function should generally pass in token, and call the permit function of the underlying token for signature approval, before exchanging the token of the authorized user to the specified address. In this case, since the $NUM token contract didn’t have a permit function, but it did have a callback function, which means that when an attacker sent in a fake signature, the callback function would return normally, so the transaction wouldn't fail. Eventually, this allowed the $NUM token at the victim address to be transferred to the specified attack contract. The attacker then used Uniswap to convert the stolen $NUM tokens into $USDC and then into WETH. The attack was front-run by a bot, which paid the builder approximately 10 ETH out of the entire profit.

  


 **Block Data Reference**

Attacker TX:

https://etherscan.io/tx/0x8a8145ab28b5d2a2e61d74c02c12350731f479b3175893de2014124f998bff32


Proof Links:
- [https://medium.com/numbers-protocol/investigation-report-of-multi-chain-bridge-incident-d4773cb3e87b](https://medium.com/numbers-protocol/investigation-report-of-multi-chain-bridge-incident-d4773cb3e87b)
- [ https://neptunemutual.com/blog/taking-a-closer-look-at-the-numbers-protocol-hack/#:~:text=On%20November%2023%2C%202022%2C%20the]( https://neptunemutual.com/blog/taking-a-closer-look-at-the-numbers-protocol-hack/#:~:text=On%20November%2023%2C%202022%2C%20the)
- [the%20loss%20of%20approximately%20%2413%2C836.](the%20loss%20of%20approximately%20%2413%2C836.)


