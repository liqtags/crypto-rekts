# Crema Finance
![Crema Finance](/rektimages/Crema-Finance.png)
- Amount Lost: $8,782,446.00
- Funds Returned: $7,356,932.00
- Category: Exchange (DEX)
- Date: 2022-7-2

**Quick Summary**

Crema Finance was attacked by a white hat hacker for ~$8.8M who then returned the majority of stolen funds, leaving the attacker with 45455 $SOL as a reward for finding the exploit. The Solana network became the place of the exploit, and all funds were transferred by the attacker through the Wormhole Bridge to the ETH network and swapped to 6K $ETH.

  


 **Details of the Exploit**

Crema Finance is a concentrated liquidity protocol that provides superior performance for both traders and liquidity providers on Solana network. ** **

The hacker took advantage of the vulnerability of the Crema Finance protocol to withdraw funds from this platform, but after negotiations between Crema Finance and the attacker, they came to an agreement that the hacker would keep 45455 SOL as a reward for finding the vulnerability, and return the remaining funds back to their ETH network address.

  


Exploit step by step:

1) The hacker created a fake Tick account. Tick Account is a special account that stores price tick data in the Crema Finance platform.

2) After creating a fake Tick account, the attacker bypassed the standard check for the owner of the Tick account. The fraudster wrote the initialized address of the Pool Tick to a fake account in this transaction: https://solscan.io/tx/5kfoGgEvhBiHXz1MBVxn8rfJh3cf98m3D64YHE2Q1SsXLiaahvdK4hCJfkMA7jQFXLjP9YdNSTMSor3oXbKrLTev

3) Next, the hacker deployed the contract and used it to provide a flash loan from Solend to add liquidity to Crema to open positions. Contract creations transaction: https://solscan.io/tx/JdorRBPfKNWnZNhWcjwc9Uz5yYaA15CVjT8kLM12tVUqZUu28CqtVEuJ5KpjWHJmVtL7j7sQVhPHHrByhNEKqej

4) Then the hacker used smart contract to lend a flash loan from Solend to add liquidity on Crema Finance to open positions:

   A) https://solscan.io/tx/5B4QXpMfpDpaX8dg2GF5DVLz9dAiZz1sjPL45wgP7X1o9fpdgCvYKi2FHEosSQBS63uDsos37AyrKC1a4YbKohGv

   B) https://solscan.io/tx/4FaMTKqha9Uw6hvxg5TQc5W7vRDKxVkfPn5GDMThGYSj3tgyCYSzXzQsAsT3dXDY6yZ26iYieV6bcV7bFDkTZ83W

5) After that, the hacker exchanged tokens for $SOL, some of which are on the Solana account, and the rest was transferred to the ETH blockchain through the Wormhole.

  


 **Block Data Reference**

Attacker addresses: 

Solana: https://solscan.io/account/Esmx2QjmDZMjJ15yBJ2nhqisjEt7Gqro4jSkofdoVsvY

ETH: https://etherscan.io/address/0x8021b2962db803b73aa874030b0b42c202e8458f

Attacker's smart contract: https://solscan.io/account/CiDwX4eMS7hfit1oMHK6MCrgve9HVvgm2PAp7Cz6Bck

Contract creation transaction: https://solscan.io/tx/JdorRBPfKNWnZNhWcjwc9Uz5yYaA15CVjT8kLM12tVUqZUu28CqtVEuJ5KpjWHJmVtL7j7sQVhPHHrByhNEKqej

Victim address: https://solscan.io/account/Ej4KxxUz73edQzjfsPVWvYxT5eyhQoWoXpo7BYm2Ejhj

  


Attacker returning funds transactions:

1) https://etherscan.io/tx/0xb5935f1fc30921733644de621bb64589f57c650a1985cc5d01c9d24ce03a95bb

2) https://etherscan.io/tx/0xe7bda58d0d0e7ffdbdfd13326da8d26312442e078a86d6458c276ecbfc3a3d3a

3) https://solscan.io/tx/5BxSYVzfaNaKT3HsHGrSze2R4Ue5121e2zJH67u7ncFHqauCzpfm92yk3ULDrtHwt46dF44NwyDC3mYx2cVJDtrS

4) https://solscan.io/tx/5sN74N2Mb9TrbU5LZ5VqyeX5xroeLSaXkWdzzNVbA1sYw7EumvDKBTiRinUdf7esCCz81quoEpGQzsjs6uLWYjJx


Proof Links:
- [https://www.coindesk.com/tech/2022/07/04/solana-defi-protocol-crema-loses-88m-in-exploit/](https://www.coindesk.com/tech/2022/07/04/solana-defi-protocol-crema-loses-88m-in-exploit/)
- [ https://news.bitcoin.com/exploit-forces-crema-finance-to-temporarily-suspend-services-8-7-million-stolen/]( https://news.bitcoin.com/exploit-forces-crema-finance-to-temporarily-suspend-services-8-7-million-stolen/)
- [ https://www.certik.com/resources/blog/4XzSJEeWC2bRppR9CeBckw-crema-finance-exploit]( https://www.certik.com/resources/blog/4XzSJEeWC2bRppR9CeBckw-crema-finance-exploit)
- [ https://www.binance.com/en/news/flash/7143600]( https://www.binance.com/en/news/flash/7143600)


