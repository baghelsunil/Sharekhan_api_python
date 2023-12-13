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

'''
Instrument type, such as EQ, FS, FI and so on

optionType String Available parameters: CE, PE, FUT

Exchange Name

NSE-Equity - NC
BSE-Equity - BC
NSECUR- RN

NSEFO - NF
MCXFO -MX

'''

print("++++++++++Login+++++++++++++++++++++")
print(login)
print("+++++++++++++++++++++++++++++++")
print(url)

response = requests.get(url)


print("++++++++++++ response+++++++++++++++++++")
print(response)

#print(login)
print("-------------------")
request_token="b1-43_axI_DBPnd03lX9DmAdjIHQ98EYlUIp73BcFCr4r5Tw9G7XegUa56eMWGTr7OF62UUAmQ=="


secret_key="wWsdmInxJRK5GTmKSrMH1nlcG2HL2qXu"


#"""Use generate session method when you are passing version id """
#session=login.generate_session(request_token,secret_key)
#session="YVropqm2E-3KKHdtgHHmbSoLsJbC9Pp5q3UMhlhDNzu8xM-Apya1TfnH86uSNyGh20Dw1Cys0Q"

#print("-------session------------")

#print(session)
print("-------------------")

# Generating access token for version id and pass parameters as it is passed below
#access_token=login.get_access_token(api_key,session,state,versionId=version_id)

#"""Use generate session without version id method when you are not passing version id """
sessionwithoutvesionId=login.generate_session_without_versionId(request_token,secret_key)

print("Session ID without version -------------------")
print(sessionwithoutvesionId)




f = open('access_token.txt')
access_token_2 = f.read()
print(access_token_2)


print( "------------- type ----------- ")
print(type(access_token_2))

#access_token = "Your access token value"
#sharekhan = SharekhanConnect(api_key,access_token)
sharekhan = SharekhanConnect(api_key,access_token=access_token_2)

print("sharekhan ******* -------------------")
print(sharekhan)
print("sharekhan request headers ******* -------------------")
print(sharekhan.requestHeaders())       # for printing request header



exchange="MX"
order=sharekhan.master(exchange)
#print("Script Master : {}".format(order))

file_name = "MX.txt"

with open(file_name, 'w') as file:
    # Write the data to the file
    file.write((format(json.dumps(order, indent=4)))
	)
    

#Script Master


