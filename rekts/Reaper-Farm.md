# Reaper Farm
![Reaper Farm](/rektimages/Reaper-Farm.png)
- Amount Lost: $1,700,000.00
- Funds Returned: $0.00
- Category: Yield Aggregator
- Date: 2022-8-2

**Quick Summary**  
The Reaper Farm protocol was hacked due to the lack of validation checks, as a result of which user funds were withdrawn to the attacker's account.  
 **  
Details of the Exploit**

Reaper is an auto-compounding yield farm that maximizes users' yields by leveraging the power of compound interest.

The Reaper Farm protocol had a lack of validation check, which the attacker took advantage of, stealing $1.7M.

The attacker created a smart contract (https://ftmscan.com/tx/0xe7635f32b7e073186445d6400c83d429f130b34921a32347afbce10eefbdc607 ) which was used to withdraw funds from the protocol to the attacker address (B).

Example transactions:

1) https://ftmscan.com/tx/0xc929f3b9312ff26be0adb1c3ff832dbdafdcbcaad33d002744effd515e53c9d5

2) https://ftmscan.com/tx/0x24770e104ae1f8f47d1c095046379557ba3d17e49d3186e5f46f22d1067a57e9

3) https://ftmscan.com/tx/0x7f79934a9c2fb01e3f7af57939746cfdc4b3854ecfff712b84a593e60d8e3754

Full list of transactions: https://ftmscan.com/token/0x04068da6c83afcfa0e13ba15a6696662335d5b75?a=0x2c177d20b1b1d68cc85d3215904a7bb6629ca954

Then all stolen tokens were bridged from FTM to ETH.

Example transactions:

1) https://ftmscan.com/tx/0x2fa4eb1813a77a143b72006c682733a54eddef43fb1a0ec2b85b448a830a8913

2) https://ftmscan.com/tx/0x345b6f910bd318f1ab5df7c67effd4e808a202ac1f9c186bf69af7c6f49d5504

3) https://ftmscan.com/tx/0x551f875e2a9bf101f52e8138248ed74bc5201d9029ca7171c6c0a605c9a12e9d

Then all funds were laundered via Tornado.Cash.

  


 **Block Data Reference**

Attacker addresses: 

(FTM) scammer address(A): https://ftmscan.com/address/0x5636e55e4a72299a0f194c001841e2ce75bb527a

(FTM) scammer address(B): https://ftmscan.com/address/0x2c177d20b1b1d68cc85d3215904a7bb6629ca954

(ETH) scammer address(B): https://etherscan.io/address/0x2c177d20b1b1d68cc85d3215904a7bb6629ca954

  


Attacker's contract address: https://ftmscan.com/address/0x8162a5e187128565ace634e76fdd083cb04d0145


Proof Links:
- [https://chaindebrief.com/reaper-farm-got-hacked/#:~:text=Reaper%20Farm%2C%20previously%20known%20as%20Reaper%20finance%2C%20was%20just%20hacked.&text=The%20yield%20aggregator%2C%20which%20is](https://chaindebrief.com/reaper-farm-got-hacked/#:~:text=Reaper%20Farm%2C%20previously%20known%20as%20Reaper%20finance%2C%20was%20just%20hacked.&text=The%20yield%20aggregator%2C%20which%20is)
- [multi%2Dstrategy%20vault%20was%20hacked.&text=The%20smart%20contract%20had%20a](multi%2Dstrategy%20vault%20was%20hacked.&text=The%20smart%20contract%20had%20a)
- [anybody's%20assets%20to%20their%20account.](anybody's%20assets%20to%20their%20account.)


