# Cauldron
![Cauldron](/rektimages/Cauldron.png)
- Amount Lost: $370,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2022-9-6

**Quick Summary**

The biggest flash loan attack on Avalanche in 2022 was detected. The attacker took 370,000 $USD after interacting with several assets.

  


 **Details of the Exploit**

The attacker interacted with Cauldron, Aave, JoeSwap, and Curve for various purposes. The attacker used a malicious smart contract with an unverified source code to withdraw 998,000 $nxUSD using LP tokens worth 500,000 $USDC. The full attack flow of the exploit transaction succeeded as follows:

   1\. The attackers malicious contract flashloaned 51,000,000 $USDC from Aave

   2\. 280,000 $USDC were swapped to $WAVAX with JoeSwap

   3\. liquidity was added using claimed $WAVAX and 260,000 $USDC so 0.0045 JoeLPToken was received

   4\. The remaining 50,460,000 $USDC were swapped for $WAVAX on JoeSwap and it changed the reserve of the pool

   5\. The attackers contract called the updateExchangeRate function on the CauldronV2 smart contract, which changed the ExchangeRate variable according to the previous JoeSwap pool's reserve amount

   6\. The attackers contract deposited 0.0045 JoeLPToken to the CauldronV2 and 998,000 $nxUSD were withdrawn from DegenBox. Because of the manipulated ExchangeRate variable, the attacker was able to take that amount for 500,000 $USD worth JoeLPTokens

   7\. The remaining $WAVAX were swapped back for 50,426,896 $USDC on the previous JoeSwap pool

   8\. Consequently, Curve.fi and other pools were used to swap 998,000 $nxUSD for 970,010 $USDC

   9\. The 51,025,500 $USDC for the flash loan were paid back to Aave

   10\. The profit amounted to 371,406 $USDC and were transferred to an EOA address.

  


 **Block Data Reference**

CauldronV2 vulnerable contract:

https://snowtrace.io/address/0xe767c6c3bf42f550a5a258a379713322b6c4c060

Exploit transaction:

https://snowtrace.io/tx/0x0ab12913f9232b27b0664cd2d50e482ad6aa896aeb811b53081712f42d54c026

Attacker address:

https://snowtrace.io/address/0x69992a2e5d6ec031ab16733975110f0b43a0b1af

Attacker smart contract:

https://snowtrace.io/address/0x16b94c6358fe622241d055811d829281836e49d6

DegenBox contract:

https://snowtrace.io/address/0x0b1f9c2211f77ec3fa2719671c5646cf6e59b775

Stolen funds sent to:

https://snowtrace.io/address/0x8ec74e6f9627d445f546cdc606a35a3334378381

  



Proof Links:
- [https://archive.is/TiUzv](https://archive.is/TiUzv)
- [ https://archive.is/Rt3Up]( https://archive.is/Rt3Up)


