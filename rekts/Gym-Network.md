# Gym Network
![Gym Network](/rektimages/Gym-Network.png)
- Amount Lost: $2,100,000.00
- Funds Returned: $0.00
- Category: Gaming / Metaverse
- Date: 2022-6-8

Gym Network has been exploited for $2.1M. The _depositFromOtherContract()_ function is a wrapper for the __autoDeposit()_ function, where there is no _transfer()  _function to transfer a user’s deposit to the contract, so a user can call _deposit()_ and ‘create deposit record’ without actually transferring tokens. 

Now function is resolved adding _onlyBank()  _modifier.

  


Exploiter address (BSC): https://bscscan.com/address/0xb2c035eee03b821cbe78644e5da8b8eaa711d2e5

Exploiter contract (BSC): https://bscscan.com/address/0x7cbfd7bccd0a4a377ec6f6e44857efe42c91b6ea

Victim contract: https://bscscan.com/address/0x0288fba0bf19072d30490a0f3c81cd9b0634258a

Repaired contract: https://bscscan.com/address/0x7df0bc661b6a239ae2f41f9548f6b17f7bd8328b

  


Exploiter transactions example:

1) https://bscscan.com/tx/0x171a448161f2c438cca0502599a6784561d11099c9218e2125c5f3c7a6705dd3

2) https://bscscan.com/tx/0x91f5e625447da3e7d0d409d5c7762c94c4d5793ab34430b81a9889e5ef9f37dd

3) https://bscscan.com/tx/0x12970f3962b4bacd01bb4e3dc086804e4e5861134db5dd80d7e4671aa7f23d16

  


The attacker has created several contracts to perform these steps:

The attacker calls the _depositFromOtherContract()  _function with the deposit amount set to 8M GYMNET, without transferring money because there is no transfer function.

Next attacker calls _withdraw()_ function to withdraw 8M GYMNET.

Then attacker swaps GYMNET tokens to BNB and sends them to this address: https://bscscan.com/address/0xb2c035eee03b821cbe78644e5da8b8eaa711d2e5[](https://bscscan.com/address/0xb2c035eee03b821cbe78644e5da8b8eaa711d2e5)  


  


All funds were laundered via TornadoCache.


Proof Links:
- [https://twitter.com/GymNet_Official/status/1534452473754157056](https://twitter.com/GymNet_Official/status/1534452473754157056)


