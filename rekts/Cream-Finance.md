# Cream Finance
![Cream Finance](/rektimages/Cream-Finance.png)
- Amount Lost: $0.00
- Funds Returned: $0.00
- Category: Borrowing and Lending,Exchange (DEX)
- Date: 2021-3-17

DNS hijacking was discovered at Cream Finance. Their GoDaddy account was hacked, and users were redirected to a phishing website.  
  
Incident timeline:  
1\. The website was down; users reported a website outage

2\. GoDaddy DNS CNAME record not pointing to their hosting IP, consistent with the website outage

3\. DNS A record was updated to the correct IP; root cause analysis began

4\. Noticed DNS cache pollution, consistent with user reports; Began DNS migration to Cloudflare

5\. Discovered that GoDaddy login credentials were compromised and could not log in

6\. CoinGecko, CoinMarketCap, and imToken were notified to update the website link and put up warning messages

7\. Two alternative websites were put for users to continue using Cream Finance

8\. The ownership of the domain was reclaimed with the help of GoDaddy, started to recover the service and ensure the security

9\. The website returned to normal, while some regions were still affected as DNS propagation continued


Proof Links:
- [https://medium.com/cream-finance/postmortem-report-of-dns-hijacking-66ab9c6ce63d](https://medium.com/cream-finance/postmortem-report-of-dns-hijacking-66ab9c6ce63d)


