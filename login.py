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

#https://api.sharekhan.com/skapi/auth/login.html?api_key=p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj&state=12345&version_id=1005


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
request_token="NB25xfntWMetDHhn01rATXwsvp354OZfv0By_HN4JRb4r5Tw9G7XNF_EvVELzxbMB_ErmtooHw=="


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

# Generating access token for without version id
access_token=login.get_access_token(api_key,sessionwithoutvesionId,state)

print("access token type ******* -------------------")
print(type(access_token))
print((access_token))
print("access token ******* -------------------")
print(access_token['data']['token'])

access_token_1=access_token['data']['token']

f = open('access_token.txt', 'w') 
f.write(str(access_token_1))
f.close()

f = open('access_token_obj.txt', 'w') 
f.write(str(access_token))
f.close()


#access_token = "Your access token value"
#sharekhan = SharekhanConnect(api_key,access_token)
sharekhan = SharekhanConnect(api_key,access_token=access_token_1)

print("sharekhan ******* -------------------")
print(sharekhan)
print("sharekhan request headers ******* -------------------")
print(sharekhan.requestHeaders())       # for printing request headers




# Replace this URL with the one you want to call
#url = 'https://api.sharekhan.com/skapi/services/reports/946423'
#url_holdings = 'https://api.sharekhan.com/skapi/services/holdings/946423'

# Send an HTTP GET request to the URL
#response = requests.get(url_holdings)

# Check if the request was successful (status code 200)
#if response.status_code == 200:
#    print('Request was successful!')
    # Print the content of the response
#    print(response.text)
#else:
#    print(f'Error: Request failed with status code {response.status_code}')
    



# services Holdings

customerId="946423"

exchange="BC"
scripcode=500410
interval="daily"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Holdings Data: {}".format(order))







Holdings=sharekhan.holdings(customerId)
print("Holdings : {}".format(Holdings))








with open(file_name, 'w') as file:
    # Write the data to the file
    file.write((format(json.dumps(Holdings, indent=4)))
	)
    


sys.exit()


# Place order history

orderparams={
 "customerId": customerId,
 "scripCode": 1052,
 "tradingSymbol": "USDINR",
 "exchange": "RN",
  "transactionType": "B",
  "quantity": 1,
  "disclosedQty": 0,
  "price": "82.0075",
  "triggerPrice": "0",
   "rmsCode": "ANY",
   "afterHour": "N",
   "orderType": "NORMAL",
   "channelUser": "XXXXX",
   "validity": "GFD",
   "requestType": "NEW",
   "productType": "INVESTMENT",
   "instrumentType": "FUTCUR",
   "strikePrice": -1,
   "expiry": "31/03/2023",
   "optionType": "XX"
   }
order=sharekhan.placeOrder(orderparams)
print("PlaceOrder: {}".format(order))

# modify order

orderparams={
 "orderId":"259130707",
    "customerId": customerId,
    "scripCode": 1052,
    "tradingSymbol": "USDINR",
    "exchange": "RN",
    "transactionType": "B",
    "quantity": 2,
    "disclosedQty": 0,
    "price": "81.1050",
    "triggerPrice": "0",
    "rmsCode": "SKNSECURR2",
    "afterHour": "N",
    "orderType": "NORMAL",
    "channelUser": "XXXXX",
    "validity": "GFD",
    "requestType": "MODIFY",
    "productType": "INVESTMENT",
    "instrumentType": "FUTCUR",
    "strikePrice": -1,
    "expiry": "31/03/2023",
    "optionType": "XX"
    }
order=sharekhan.modifyOrder(orderparams)
print("ModifyOrder: {}".format(order))

#cancel  order

orderparams={
  "orderId":"259130707",
    "customerId": customerId,
    "scripCode": 1052,
    "tradingSymbol": "USDINR",
    "exchange": "RN",
    "transactionType": "B",
    "quantity": 2,
    "disclosedQty": 0,
    "price": "81.1050",
    "triggerPrice": "0",
    "rmsCode": "SKNSECURR2",
    "afterHour": "N",
    "orderType": "NORMAL",
    "channelUser": "XXXXX",
    "validity": "GFD",
    "requestType": "CANCEL",
    "productType": "INVESTMENT",
    "instrumentType": "FUTCUR",
    "strikePrice": -1,
    "expiry": "31/03/2023",
    "optionType": "XX"
    }
order=sharekhan.cancelOrder(orderparams)
print("CancelOrder: {}".format(order))

# Fund details

exchange="MX"
#customerId="customerId <int data type>"
order=sharekhan.funds(exchange, customerId)
print("Fund Details : {}".format(order))

# Retrieves all orders for the day

#customerId="customerId <int data type>"
order=sharekhan.reports(customerId)
print("Order Reports: {}".format(order))

#Retrieve history of an given order

exchange="RN"
#customerId="customerId <int data type>"
orderId=259130707
order=sharekhan.exchange(exchange, customerId, orderId)
print("Order Details: {}".format(order))


# Retrieves all positions
#customerId="customerId <int data type>"
order=sharekhan.trades(customerId)
print("Postion Reports: {}".format(order))


# Retrieves the trade  generated by an order

exchange="NC"
#customerId="customerId <int data type>"
orderId=585194484
order=sharekhan.exchangetrades(exchange, customerId, orderId)
print("Trade Generated By an Order : {}".format(order))

# services Holdings

#customerId="customerId <int data type>"
order=sharekhan.holdings(customerId)
print("Holdings : {}".format(order))

#Script Master

exchange="MX"
order=sharekhan.master(exchange)
print("Script Master : {}".format(order))

# Historical Data

exchange="BC"
scripcode=500410
interval="daily"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Holdings Data: {}".format(order))

