# Ultimate Set Dollar
![Ultimate Set Dollar](/rektimages/Ultimate-Set-Dollar.png)
- Amount Lost: $0.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2021-1-2

The minter of the token contract is an upgradable proxy contract. Upgradable proxy was used as MasterChef contract: https://etherscan.io/address/0x61ee8806891e9411722ad20c1e30be7da8ad933d  
  
The contract deployer added initial liquidity at:  
https://etherscan.io/tx/0x76950cb779dc80951a64538edadc3f9bd7bd27aa1e3c2fb5137a6e88f4635e81  
  
The unverified contract addressed the proxy contract by calling _rebase_ () function 12 times:  
https://etherscan.io/address/0x4d01e88831280fd9d5b8d8c3e4f9e33d02cd7d76#tokentxns  
  
This led to the token mint directly onto the unverified contract, which finally sold minted tokens at:  
https://etherscan.io/tx/0xd13883590ceaedb3ac6249d898e1823e16971c04b4fa9fef0e900a7bb5cb4b63  
  
The proxy contract was able to mint tokens by calling _advance_ () function:  
https://etherscan.io/tx/0xa02b66f1e5a339aa88793561f47968cc662434b7c8a09b870ca73c465ca3dd87


Proof Links:
- [https://twitter.com/CaptainJackAPE/status/1344933208832368647](https://twitter.com/CaptainJackAPE/status/1344933208832368647)


