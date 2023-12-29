# TECRA
![TECRA](/rektimages/TECRA.png)
- Amount Lost: $642,756.00
- Funds Returned: $0.00
- Category: Token
- Date: 2022-2-4

The exploiter's address:  
https://etherscan.io/address/0xb19b7f59c08ea447f82b587c058ecbf5fde9c299  
  
The transaction behind the exploit:  
https://etherscan.io/tx/0x81e9918e248d14d78ff7b697355fd9f456c6d7881486ed14fdfb69db16631154  
  
The attacker:  
\- approved a big number of tokens to the Uniswap pool  
\- bought 101 TCR from the pool  
\- used the loophole to burn the TCR owned by the pool, increasing the TCR price  
\- used the bought TCR to take away a lot of USDT  
  
Wrong implementation:  
    function burnFrom(address from, uint256 amount) external {  
          require(_allowances[msg.sender][from] >= amount, ERROR_ATL);  
  
Correct one:  
require(_allowances[from][msg.sender] >= amount, ERROR_ATL);  
  
The actual token implementation allows any account A to burn tokens from any other account B if account A approves that number of tokens to B.  
  
The part of the stolen funds was deposited into Tornado Cash mixer, and the rest holds on the exploiter's address:  
https://bloxy.info/txs/transfers_from/0xb19b7f59c08ea447f82b587c058ecbf5fde9c299?currency_id=1


Proof Links:
- [https://archive.is/gfc3F](https://archive.is/gfc3F)
- [ https://twitter.com/Mauricio_0218/status/1490082089441673217]( https://twitter.com/Mauricio_0218/status/1490082089441673217)


