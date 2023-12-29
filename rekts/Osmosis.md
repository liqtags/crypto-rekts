# Osmosis
![Osmosis](/rektimages/Osmosis.png)
- Amount Lost: $5,000,000.00
- Funds Returned: $0.00
- Category: Exchange (DEX)
- Date: 2022-6-8

Osmosis has been rugged by liquidity pool providers. Size of loss is ~$5M. One of the attackers added liquidity USDC and OSMO. The attacker then received GAMM LP tokens in return, which represented his share in the pool. They immediately revoked GAMM LP tokens, thereby receiving 50% more than the amount of USDC and OSMO that were added as liquidity.

  


Token address: https://www.mintscan.io/osmosis/account/osmo1w4x44ek799hvg97x0mfwu6gg5dww2r8fhkgrgj

Example transaction: https://www.mintscan.io/osmosis/account/osmo1hq8tlgq0kqz9e56532zghdhz7g8gtjymdltqer

  


Attack example step by step:

1\. Add liquidity to a pool 

2\. Remove liquidity from the pool allowing 50% extra. No bonding needed. 

3\. Rinse and repeat


Proof Links:
- [https://twitter.com/osmosiszone/status/1534470729797976064](https://twitter.com/osmosiszone/status/1534470729797976064)
- [ https://twitter.com/osmosiszone/status/1534432704246292480]( https://twitter.com/osmosiszone/status/1534432704246292480)


