# Parity
![Parity](/rektimages/Parity.png)
- Amount Lost: $34,000,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2017-7-19

**Quick Summary**

Parity multisig wallet has been attacked by a hacker in two transactions, taking profit of $34M.

  


 **Details of the Exploit**

The attacker had drained 153,037 ETH from three high-profile multi-signature contracts used to store funds from past token sales. The attacker's address:  
https://etherscan.io/address/0xb3764761e297d6f121e79c32a65829cd1ddb4d32  
  
The attacker sent two transactions to each of the affected contracts: the first to obtain exclusive ownership of the MultiSig, and the second to move all of its funds.  
  
1st transaction (call to _initWallet_ ):  
https://etherscan.io/tx/0x9dbf0326a03a2a3719c27be4fa69aacc9857fd231a8d9dcaede4bb083def75ec  
  
2nd transaction:  
https://etherscan.io/tx/0xeef10fc5170f669b86c4cd0444882a96087221325f8bf2f55d6188633aa7be7c  
  
This function was probably created as a way to extract the wallet’s constructor logic into a separate library. The wallet contract forwards all unmatched function calls to the library using _delegatecall_  
  
This causes all public functions from the library to be callable by anyone, including _initWallet_ , which can change the contract’s owners. Unfortunately, _initWallet_ has no checks to prevent an attacker from calling it after the contract was initialized. The attacker exploited this and simply changed the contract’s _m_owners_ state variable to a list containing only their address, and requiring just one confirmation to execute any transaction:  
https://etherscan.io/tx/0x9dbf0326a03a2a3719c27be4fa69aacc9857fd231a8d9dcaede4bb083def75ec  
  
After that, the attacker executed the function to send all funds to an account controlled by the attacker:  
https://etherscan.io/tx/0xeef10fc5170f669b86c4cd0444882a96087221325f8bf2f55d6188633aa7be7c

  


 **Block Data Reference**

Attacker address:

https://etherscan.io/address/0xb3764761e297d6f121e79c32a65829cd1ddb4d32

  



Proof Links:
- [https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7/](https://blog.openzeppelin.com/on-the-parity-wallet-multisig-hack-405a8c12e8f7/)


