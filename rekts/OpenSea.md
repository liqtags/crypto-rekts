# OpenSea
![OpenSea](/rektimages/OpenSea.png)
- Amount Lost: $1,019,300.00
- Funds Returned: $75,000.00
- Category: NFT
- Date: 2022-1-24

A bug has been exploited to purchase NFTs from users of OpenSea, at well below market value.  
  
Was identified at least five attackers who have exploited this loophole to purchase at least twelve NFTs for much less than their market value. These include Bored Ape Yacht Club, Mutant Ape Yacht Club, Cool Cats, and Cyberkongz NFTs.  
  
The exploit:  
\- when you list an item for sale (or bid) you are signing data that validate that you are willing to sell your NFT at this price  
  
\- the signature is saved in OpenSea's DB off-chain and when someone wants to buy your NFT, they will send to their smart contract your previously signed data where the signature and sale information (such as expiration & price) are validated on-chain before making the transfer  
  
\- when you cancel a listing, you are required to perform a transaction. The reason is that someone might save your signed listing (which are public - i.e https://orders.rarible.com or even their API) and use it later, even if the listing got removed from the UI  
  
\- the transaction on-chain will save the fact that you canceled this sale on their smart contract and even if someone will try to use your signed data from before, the on-chain validation will reject the sale  
  
\- the bug stems from the fact that previously you could re-list an NFT without canceling it and all the previous listings are not canceled on-chain, this is why re-listing will not work  
  
For example, at around 7 am on January 24, a Bored Ape Yacht Club NFT #9991 was purchased for 0.77 ETH ($1,800). This family of NFTs currently sells for at least $198,000. Twenty minutes later the hacker sold the NFT for 84.2 ETH ($196,000) – realizing a profit of $194,000.  
  
One attacker, going by the pseudonym "jpegdegenlove" paid a total of $133,000 for seven NFTs – before quickly selling them on for $934,000 in ether. Five hours later this ether was sent through Tornado Cash, a "mixing" service that is used to prevent blockchain tracing of funds:  
https://etherscan.io/address/0xb1a22cc48f6784f629a994917cd6474923630c48  
  
Victims were partially compensated:  
https://etherscan.io/tx/0xa4712e1f9aed57a26db689cabd47cc22a23e8638bb8c7be051cdeff27fd66bef  
https://etherscan.io/tx/0x8c7327bf6d2bdb3e8f3db70fd87f160ff9f2b0940d4f0cdf6b9380d32295bf9c


Proof Links:
- [https://twitter.com/_lut1/status/1485571998331781123](https://twitter.com/_lut1/status/1485571998331781123)
- [ https://www.elliptic.co/blog/bug-allows-nfts-worth-over-1-million-to-be-stolen]( https://www.elliptic.co/blog/bug-allows-nfts-worth-over-1-million-to-be-stolen)


