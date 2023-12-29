# Uranium Finance
![Uranium Finance](/rektimages/Uranium-Finance.png)
- Amount Lost: $57,200,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2021-4-28

**Quick Summary**  
Pair contracts in Uranium v2 had a bug due to which anyone could interact with them and withdraw almost all tokens due to a calculation error.

  


 **Details of the Exploit**  
Before interacting with Uranium, the attacker sent the minimum amount of each token to pair contracts. After that, they used a low-level function _swap_ () whose execution should drain both reserves.  
  
Stolen funds:  
\- 34k WBNB ($18M)

\- 17.9M BUSD ($17.9M)

\- 1.8k ETH ($4.7M)

\- 80 BTC ($4.3M)

\- 26.5k DOT ($0.8M)

\- 638k ADA ($0.8M)

\- 5.7M USDT ($5.7M)

\- 112k U92  
  
With the help of PancakeSwap, DOT and ADA were swapped to ETH. After that, the attacker withdrew 2,438 ETH via Anyswap to Ethereum (deposited into Tornado Cash mixer at https://etherscan.io/txs?a=0xc61429117038a1f13881dd7410b80771f28e06ec) and 80 BTC to Bitcoin. 1M USDT and 99k DAI (bought with USDT) went to xDAI.

  


 **Block Data Reference**

The attacker's address:  
https://bscscan.com/address/0x2b528a28451e9853f51616f3b0f6d82af8bea6ae#tokentxns  
The transaction behind the attack:  
https://bscscan.com/tx/0x5a504fe72ef7fc76dfeb4d979e533af4e23fe37e90b5516186d5787893c37991


Proof Links:
- [https://uraniumfinance.medium.com/exploit-d3a88921531c](https://uraniumfinance.medium.com/exploit-d3a88921531c)
- [ https://rekt.news/uranium-rekt/]( https://rekt.news/uranium-rekt/)
- [ https://twitter.com/FrankResearcher/status/1387347025742557186]( https://twitter.com/FrankResearcher/status/1387347025742557186)
- [ https://twitter.com/BeTheb0x/status/1387288334649622528?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1387288334649622528%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcointelegraph.com%2Fnews%2F50m-reportedly-stolen-from-bsc-based-uranium-finance]( https://twitter.com/BeTheb0x/status/1387288334649622528?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1387288334649622528%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fcointelegraph.com%2Fnews%2F50m-reportedly-stolen-from-bsc-based-uranium-finance)


