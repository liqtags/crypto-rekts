# Cream Finance
![Cream Finance](/rektimages/Cream-Finance-2.png)
- Amount Lost: $130,000,000.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,Exchange (DEX)
- Date: 2021-10-27

**Quick Summary**

The flash loan attack happened on CreamFinance for the second time. Funds were stolen for a total of 130,000,000 $USD.

  


 **Details of the Exploit**  
The attacker:  
\- borrowed $500m DAI from Maker

\- deposited to yDAI into yUSD Curve pool (yDAI/yUSDC/yUSDT/yTUSD)

\- deposited $500m yUSD into yUSD Yean Vault  
\- minted $500m cryUSD by depositing minted yUSD Yearn Vault into Cream Finance

\- flash borrowed $2b ETH using contract

\- minted cETHER by depositing $2b ETH into Cream Finance

\- borrowed $500m yUSD Yean Vault by using the $2b ETH as collateral

\- minted $500m cryUSD by depositing the $500m yUSD Yean Vault back in Cream Finance

\- transferred $500m cryUSD to his address, balance: $1b cryUSD

\- borrowed $500m yUSD Yearn Vault by using the $2b ETH collateral

\- minted $500m cryUSD by depositing the $500m yUSD Yearn Vault back in Cream Finance

\- transferred $500m cryUSD to his address, balance: $1.5b cryUSD

\- borrowed $500m yUSD Yearn Vault, debt $1.5b against a $2b collateral

\- transferred $500m yUSD Yearn Vault to his address, balance: $1.5b cryUSD and $500m yUSD Yearn Vault

\- bought $3m DUSD from Curve

\- burnt $3m DUSD for the underlying yUSD Yearn Vault collateral, balance: $1.5b cryUSD and $503m yUSD Yearn Vault

\- burnt $503m yUSD Yearn Vault shares for the underlying yUSD tokens, the total supply of yUSD Yearn Vault reduced to $8m

\- transferred $8m yUSD to yUSD Yearn Vault. The yUSD balance becomes $16m while the total supply remains $8m. The price of yUSDVault share becomes $2

\- contract's debt increased to $3b against $2b collateral  
\- using $3b of cryUSD collateral on his balance, borrowed $2b ETH

\- balance: $2b ETH, $500m yUSD, and $1b in Cream collateral ($3b cryUSD collateral minus $2b ETH debt)

\- ETH and yUSD were used to pay back the flash loans and utilize the remaining $1b collateral to drain tokens from Cream Finance  
  
When retrieving the share price of the yUSD pool, Cream's lending pool uses its pricePerShare interface directly, and this interface is supplemented by the contract's collateral balance and the amount of collateral assets in the strategy pool. To calculate the price of a single share, divide the total number of shares by the number of shares outstanding. As a result, by simply moving the collateral to yUSD, the user can easily increase the price of a single share, allowing the collateral in the Cream loan pool to lend more funds.

  


 **Block Data Reference**

The attacker's addresses:

https://etherscan.io/address/0x24354d31bc9d90f62fe5f2454709c32049cf866b

https://etherscan.io/address/0x921760e71fb58dcc8de902ce81453e9e3d7fe253

  


Attacker contract address:  
https://etherscan.io/address/0x961d2b694d9097f35cfffa363ef98823928a330d

  
The transaction under the attack:  
https://etherscan.io/tx/0x0fe2542079644e107cbf13690eb9c2c65963ccb79089ff96bfaf8dced2331c92


Proof Links:
- [https://archive.vn/Z5Lev](https://archive.vn/Z5Lev)
- [ https://archive.is/kZVAa]( https://archive.is/kZVAa)


