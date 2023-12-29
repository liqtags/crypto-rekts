# Crosswise
![Crosswise](/rektimages/Crosswise.png)
- Amount Lost: $257,868.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-1-18

The transaction behind the attack:  
https://bscscan.com/tx/0xd02e444d0ef7ff063e3c2cecceba67eae832acf3f9cf817733af9139145f479b  
  
The attacker's address:  
https://bscscan.com/address/0x748346113b6d61870aa0961c6d3fb38742fc5089  
  
The attack was made possible by the public disclosure of a privileged function, which is subsequently used to set the _trustedForwarder_ and further hijack the Crosswise MasterChef owner permission.  
  
The attacker:  
\- called _setTrustedForwarder_ () function to change _trustedForwarder_  
\- transferred the ownership  
\- swapped 0.01 WBNB to 3.71 CRSS through CrosswiseRouter  
\- deposited 1 CROSS to Crosswise MasterChef  
\- set strategy to the new one under the hacker's control  
\- withdrew 692K CRSS from the MasterChef  
\- swapped 692K CRSS to 547 WBNB  
  
Stolen funds were deposited into the Tornado Cash proxy:  
https://explorer.bitquery.io/bsc/txs/calls?caller=0x748346113b6d61870aa0961c6d3fb38742fc5089&contract=0x0d5550d52428e7e3175bfc9550207e4ad3859b17


Proof Links:
- [https://crosswise.medium.com/post-exploit-update-2a24c3370466](https://crosswise.medium.com/post-exploit-update-2a24c3370466)
- [ https://twitter.com/peckshield/status/1483341677045506051]( https://twitter.com/peckshield/status/1483341677045506051)


