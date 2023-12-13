from SharekhanApi.sharekhanConnect import SharekhanConnect
import requests


import sys
import json

api_key = "p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj"
login = SharekhanConnect(api_key)
#login="https://api.sharekhan.com/skapi/auth/login.html?api_key=p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj&vendor_key=&state=12345&version_id=1005"
vendor_key = ""         # vendor key for vendor login otherwise keep it null
version_id = None #"1005"         # version id= 1005 or 1006 otherwise keep it null
state=12345
url = login.login_url(vendor_key, version_id)
#url="https://api.sharekhan.com/skapi/auth/login.html?api_key=p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj&state=12345&version_id=1005"

file_name = "Sharekhan_portfolio.json"

#def login_url(self, vendor_key=None, version_id=None):"""Get the remote login URL to which a user should be redirected to initiate the login flow."""
#base_url = "{}?api_key={}".format(self._login_url, self.api_key)
# Check if vendor_key is provided and add it to the URL if available
#if vendor_key:base_url += "&vendor_key={}".format(vendor_key)
#else:print("No Vendor Key")# state parameter in the URL is set to 
#12345base_url += "&state=12345"# Check if version_id is provided and add it to the URL if availableif 
#version_id:base_url += "&version_id={}".format(version_id)else:print("No Version Id")
#return base_url


print("++++++++++Login+++++++++++++++++++++")
print(login)
print("+++++++++++++++++++++++++++++++")
print(url)

response = requests.get(url)


print("++++++++++++ response+++++++++++++++++++")
print(response)

#print(login)
print("-------------------")

secret_key="wWsdmInxJRK5GTmKSrMH1nlcG2HL2qXu"

     # for printing request headers

access_token_1 = open("access_token.txt", 'r').read()

sharekhan = SharekhanConnect(api_key,access_token=access_token_1)


print("++++++++++++ sharekhan+++++++++++++++++++")
print(sharekhan.requestHeaders())  

print(sharekhan)

# services Holdings

customerId="946423"




exchange="BC"
scripcode=500410
interval="daily"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Holdings Data: {}".format(order))




