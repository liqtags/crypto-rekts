# Bondly
![Bondly](/rektimages/Bondly.png)
- Amount Lost: $6,800,989.00
- Funds Returned: $6,800,987.00
- Category: Other
- Date: 2021-7-14

**Quick Summary**

Bondly Finance suffered a hack on July 15, 2021.  The attacker was able to mint 373 million BONDLY tokens and profited for 6,800,987 USD

  


 **Details of the Exploit**

The attacker's address:  
https://etherscan.io/address/0xc433d50dd0614c81ee314289ec82aa63710d25e8  
  
The owner (0x58a058ca4b1b2b183077e830bc929b5eb0d3330c) of _StakingReward_ contract (0x6bee9387bb670a7f3e3b355d0389419c2aa598d1) was compromised and the owner had an allowance on sending BONDLY tokens:  
  
function send(address to, uint256 amount) onlyOwner nonReentrant external {

        require(sent.add(amount) <= maxCap, "capitalization exceeded");

        sent = sent.add(amount);

        bondToken.transfer(to, amount);

    }  
  
The contract owner sent tokens to the attacker's address at:  
https://etherscan.io/tx/0xc2b339468b23cc8b98d6d4534e87d8ec3b85a0d26f8c169a22efe14d221cfaae  
  
The attacker used received tokens to mint 200,460,00 zenBONDLY on the MANTRA DAO ZENTEREST platform and proceeded to use the funds as collateral to borrow a series of other cryptocurrency assets that were then stolen:  
https://etherscan.io/tx/0x46526cbfbb14b0bb914d35d5b0f32b0e40e9783b67c0a000e8431f698924795f  
  
The owner of _StakingReward_ contract sent extra tokens to the external wallet owned bt the attacker:  
https://etherscan.io/tx/0xbcea5abcb1b446b971eb67b6dd69736e68d273097774284ca5f257df2a31c3c7  
  
A series of Bondly-held wallets were compromised and the funds immediately transferred to the Attacker’s wallet address. In addition, hundreds of small transfers of 10,000, 20,000, and 200,000 BONDLY were made to numerous wallet addresses, which we believe were owned by the Attacker. In addition to Bondly tokens, the transfers included 271,790,246 $BONDLY BSC tokens and 6,620,128 $BONDLY Polygon tokens.  
  
The attacker moved 3,569 Uniswap V2 liquidity tokens from compromised Bondly wallets to the Attacker’s wallet. Later it was identified that Attacker removed liquidity from Uniswap:  
https://etherscan.io/tx/0x6a8f9d1e686bb226e0ef387923b527dc20c700249df14b42ae0cfc5a9c426d9d  
  
501 Ether, stored at the following Ethereum address, which included Bondly assets, were sent to Tornado Cash through a series of transactions by the attacker:  
https://etherscan.io/address/0xa465e908abbda0ba0da598cced8abd4901b2f634  
  
https://bloxy.info/txs/calls_from/0xa465e908abbda0ba0da598cced8abd4901b2f634?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967  
  
The attacker sent 5.2m DAI and 202 ETH to the Tornado Cash mixer:  
https://bloxy.info/txs/calls_from/0xc433d50dd0614c81ee314289ec82aa63710d25e8?signature_id=994162&smart_contract_address_bin=0x722122df12d4e14e13ac3b6895a86e84145b6967


Proof Links:
- [https://bondlyfinance.medium.com/bondly-attack-july-14th-2021-postmortem-beb7cf02e9ba](https://bondlyfinance.medium.com/bondly-attack-july-14th-2021-postmortem-beb7cf02e9ba)


