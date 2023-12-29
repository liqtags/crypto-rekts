# Atlantis Loans
![Atlantis Loans](/rektimages/Atlantis-Loans.png)
- Amount Lost: $1,251,622.00
- Funds Returned: $0.00
- Category: Borrowing and Lending
- Date: 2023-6-10

**Quick Summary**

Atlantis Loans, a BSC-based lending protocol, was exploited, leading to a loss of 1,251,622 $USD.

  


 **Details of the Exploit**

Atlantis Loans is a Lending and Borrowing platform running on Binance Smart Chain. On June 10, 2023, Atlantis Loans, a DeFi lending protocol on the BNB chain, fell victim to a governance attack. The attacker exploited a vulnerability that allowed them to become the administrator of the token's proxy contract and manipulate its functions. This was achieved through a malicious governance proposal created in the GovernorBravo contract on June 7, 2023, which set the admin of multiple ABep20Delegator contracts as malicious contracts. After a lockup period of 172,800 seconds, the malicious contract was set as a proxy contract admin for all tokens. This allowed the attacker to modify the ABep20Delegate implementation to include a backdoor, enabling the transfer of users' assets to their control. The attacker currently controls approximately $1,161,848 worth of funds, while the rest stolen funds are at the attacker's initial address. Notably, a similar malicious proposal with ID 49 was submitted by the attacker on April 12, 2023, but it failed to pass the quorum.

  


 **Block Data Reference**

Attacker Address:

https://bscscan.com/address/0xeade071ff23bcef312dec938ece29f7da62cf45b

  


Funds Holder Address:

https://bscscan.com/address/0xD8E918824a560CD83A90d8E97CA19a54314D6f9f

  


Malicious Contract Address:

https://bscscan.com/address/0x027383c520c289cb5c4b66f8e0c8ca65d0769094

  


Malicious Transaction:

https://bscscan.com/tx/0x3b0df86f548946d9dda9fb4177ae27bf33f06315c73ea50945ab9e53a041d7e1

  


Funds Transfer Transaction:

https://bscscan.com/tx/0x71656b958dc3add42335d83b1a04e8e2b316f0254d62f6c430d50cb2d44b67bd


Proof Links:
- [https://twitter.com/0xJ1M/status/1667466456622137346](https://twitter.com/0xJ1M/status/1667466456622137346)
- [ https://neptunemutual.com/blog/understanding-atlantis-loans-exploit/]( https://neptunemutual.com/blog/understanding-atlantis-loans-exploit/)


