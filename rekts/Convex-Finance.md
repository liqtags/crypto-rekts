# Convex Finance
![Convex Finance](/rektimages/Convex-Finance.png)
- Amount Lost: $11,578.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-6-23

**Quick Summary**

A DNS attack was conducted on Convex Finance. The hacker managed to create a contract with a similar address, prompting users to sign approval without noticing the substitution.

  


 **Details of the Exploit**

[](https://www.youtube.com/watch?v=U4xMcd_1mKY)Convex Finance, a protocol offering boosted rewards for Curve liquidity providers and stakers.

Hackers changed the original website address with the original contract to a copy of the website with a fake contract address.

Original contract address: 0xF403C135812408BFbE8713b5A23a04b3D48AAE31

Malicious contract address: 0xF403a2c10B0B9feF8f0d4F931df5d86aD187AE31.

The hackers managed to recreate the address of the contract, very similar to the address of the Convex contract, and the users did not notice the substitution, paying attention to the first 4 or last 4 characters thinking there is no problem and signed the malicious approval transaction. In total, 15,968 $CVXCRV and 433 $CRV were lost.

  


 **Block Data Reference**

Scammer address: https://etherscan.io/address/0xb73261481064f717a63e6f295d917c28385af9aa

Malicious contract address: https://etherscan.io/address/0xF403a2c10B0B9feF8f0d4F931df5d86aD187AE31

  


Accounts that approved malicious contract:

1) https://etherscan.io/address/0x496e53c32a69a79a82ed85d2913010dd2f9d1b4f

2) https://etherscan.io/address/0x4ffc5f22770ab6046c8d66dabae3a9cd1e7a03e7

3) https://etherscan.io/address/0x5b186c93a50d3cb435fe2933427d36e6dc688e4b

4) https://etherscan.io/address/0x624301090700ea1e3c5b5224f89adfae405412c1

5) https://etherscan.io/address/0x92557b6ffa116b53cf2c3bc1d6d33f78d97ed4c9


Proof Links:
- [https://thedefiant.io/convex-exploit/](https://thedefiant.io/convex-exploit/)
- [ https://convexfinance.medium.com/post-mortem-of-events-june-23-3d6db955dc7d]( https://convexfinance.medium.com/post-mortem-of-events-june-23-3d6db955dc7d)


