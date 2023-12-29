# TheDAO
![TheDAO](/rektimages/TheDAO.png)
- Amount Lost: $50,000,000.00
- Funds Returned: $0.00
- Category: Stablecoin
- Date: 2016-6-17

**Quick Summary**

The DAO ecosystem's smart contract was hacked, and 3,600,000 $ETH was stolen, which leads to the division of the blockchain into Ethereum Classic ($ETC) and Ethereum ($ETH)

  


 **Details of the Exploit**  
1\. Propose a split and wait until the voting period expires. (DAO.sol, _createProposal_ ).

2\. Execute the split. (DAO.sol, _splitDAO_ ).

3\. Let the DAO send your new DAO its share of tokens. ( _splitDAO_ -> TokenCreation.sol, _createTokenProxy_ ).

4\. Make sure the DAO tries to send you a reward before it updates your balance but after doing (3). ( _splitDAO_ -> _withdrawRewardFor  _-> ManagedAccount.sol, _payOut_ ).

5\. While the DAO is doing (4), have it run splitDAO again with the same parameters as in (2) ( _payOut_ -> __recipient.call.value_ -> __recipient()_ ).

6\. The DAO will now send you more child tokens and go to withdraw your reward before updating your balance. (DAO.sol, _splitDAO_ ).

7\. Back to (5)!

8\. Let the DAO update your balance. Because (7) goes back to (5), it never actually will.

  


Deconstructing the constructor arguments that created that child DAO leads us to a curator.  
That smart contract is just a regular multi-signature wallet, with most of its past transactions being adding/removing owners and other wallet management tasks.  
The true total funds lost cannot be calculated properly. The mentioned amount is taken from different sources.

  


 **Block Data Reference**  
The malicious DAO creator:  
https://etherscan.io/address/0x4a574510c7014e4ae985403536074abe582adfc8  
Start of the drain:  
https://etherscan.io/tx/0x0ec3f2488a93839524add10ea229e773f6bc891b4eb4794c3337d4495263790b  
The malicious child DAO "The Dark DAO":  
https://etherscan.io/address/0x304a554a310c7e546dfe434669c62820b7d83490  
The account that executed the transactions behind the split is:  
https://etherscan.io/address/0xf35e2cc8e6523d683ed44870f5b7cc785051a77d  
The proposal was created and initiated by account:  
https://etherscan.io/address/0xb656b2a9c3b2416437a811e07466ca712f5a5b5a at transaction:  
https://etherscan.io/tx/0x5798fbc45e3b63832abc4984b0f3574a13545f415dd672cd8540cd71f735db56

Curator address:

https://etherscan.io/address/0xda4a4626d3e16e094de3225a751aab7128e96526


Proof Links:
- [https://hackingdistributed.com/2016/06/18/analysis-of-the-dao-exploit/](https://hackingdistributed.com/2016/06/18/analysis-of-the-dao-exploit/)
- [ https://medium.com/@oaeee/the-rise-of-the-dark-dao-72b21a2212e3#.rnb1n01h8]( https://medium.com/@oaeee/the-rise-of-the-dark-dao-72b21a2212e3#.rnb1n01h8)


