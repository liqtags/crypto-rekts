# Zabu Finance
![Zabu Finance](/rektimages/Zabu-Finance.png)
- Amount Lost: $3,200,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-9-12

The attacker:  
https://cchain.explorer.avax.network/address/0x9ed2D048e90CfFa5e4A778678CBc3acb8A3Abf86/transactions  
  
The transaction behind the attack:  
https://cchain.explorer.avax.network/tx/0x8b3042e55a63f39bb388240a089cf4d51e59abe7cb0bff303c6dbb19eaeb75ac/token-transfers  
  
The hack was due to the lack of deflationary token support in the MasterChef contract. By repeated deposits and withdrawals with the MasterChef, the attacker frequently triggers the tax collection, which led to the exploit.  
  
The attacker deployed the contract with the malicious logic at:  
https://cchain.explorer.avax.network/tx/0x771c4454e2681f46bfb04e20acde021127e912b8a345baa98e3502761665c319/internal-transactions  
  
Further, he interacted with that contract to successfully pulled out 4.5 billion ZABU tokens in Zabu Farm Contract.  
  
The list of stolen assets:  
\- WETH: 402.9  
\- WAVAX: 23,157  
\- PNG: 21,501  
\- AVE: 106,848  
\- USDT: 361,267  
\- JOE: 23,958.93 


Proof Links:
- [https://beincrypto.com/zabu-finance-exploited-on-avalanche-3-2m/](https://beincrypto.com/zabu-finance-exploited-on-avalanche-3-2m/)
- [ https://cointelegraph.com/news/zabu-token-price-flatlines-after-3-2m-attack-on-avalanche-blockchain]( https://cointelegraph.com/news/zabu-token-price-flatlines-after-3-2m-attack-on-avalanche-blockchain)


