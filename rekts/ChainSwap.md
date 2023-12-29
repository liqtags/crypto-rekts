# ChainSwap
![ChainSwap](/rektimages/ChainSwap.png)
- Amount Lost: $800,000.00
- Funds Returned: $0.00
- Category: Bridge
- Date: 2021-7-2

The attacker's wallet:  
https://etherscan.io/address/0x941a9e3b91e1cc015702b897c512d265fae88a9c#tokentxns  
  
For cross-chain transfers, each token has its own proxy contract, with the implementation pointing to the Factory contract. The hacker used the Factory contract's _receive_ () method. The attacker was required to pay a fee of 0.005 ETH in __chargeFee_. There are no real authentication checks, and just one signature is necessary. To get around this, the attacker simply signed signatures with new addresses each time. In the __receive()_ function, the volume argument is subsequently sent to the attacker's address.


Proof Links:
- [https://chain-swap.medium.com/chainswap-post-mortem-and-compensation-plan-90cad50898ab](https://chain-swap.medium.com/chainswap-post-mortem-and-compensation-plan-90cad50898ab)
- [ https://github.com/tinchoabbate/chainswap-exploit-poc]( https://github.com/tinchoabbate/chainswap-exploit-poc)


