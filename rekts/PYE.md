# PYE
![PYE](/rektimages/PYE.png)
- Amount Lost: $2,600,000.00
- Funds Returned: $0.00
- Category: Other
- Date: 2022-3-24

PYE smart contract was exploited in a bunch of transactions. The example transaction:  
https://bscscan.com/tx/0x3823a6841b025e871928306de1805d994366bc8d283494a8f15d0884e67fe2b1  
  
The exploit occurred because of the lack of "k invariant verification" in the _swap_ () routine, meaning that a caller verification was removed in the PYESwapPair. There are suspicions that this was an insider job.  
  
The part of the stolen funds was deposited into the Tornado Cash mixer on the BNB chain, the rest was bridged to Ethereum and deposited into the mixer as well:  
https://etherscan.io/address/0x85b86b43d5fdb380c8b2c3b67f0fced3570a92ee


Proof Links:
- [https://twitter.com/DevTeamSix/status/1507148822849355776](https://twitter.com/DevTeamSix/status/1507148822849355776)
- [ https://twitter.com/peckshield/status/1507143800791003159]( https://twitter.com/peckshield/status/1507143800791003159)


