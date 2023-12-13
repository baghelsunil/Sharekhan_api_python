# package import statement
from SharekhanApi.sharekhanConnect import SharekhanConnect

# Make a object call

api_key = "p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj"
login = SharekhanConnect(api_key)
vendor_key = "" 
#"""Pass the vendor key for vendor login otherwise keep it blank"""
version_id = "null"
"""Only null/1005/1006 version id is allowed to be passed"""
state=12345
url = login.login_url(vendor_key=vendor_key, version_id=version_id)
#"""This will provide you the redirect login url which can be used to login in the sharekhan account"""
print(url)


#"""After Successfully Login You will receive the request token value then you have to decrypt the token value by using secret key and then swap the request token which is a combination of RequestId and CustomerId.Then after that decrypt the request token value."""

request_token = "Valid Request Token Value"
secret_key = "Your Secret Key value"

#"""Use generate session method when you are passing version id """
session=login.generate_session(request_token,secret_key)
# Generating access token for version id and pass parameters as it is passed below 
access_token=login.get_access_token(api_key,session,state,versionId=version_id)

#"""Use generate session without version id method when you are not passing version id """
sessionwithoutvesionId=login.generate_session_without_versionId(request_token,secret_key)
# Generating access token for without version id 
access_token=login.get_access_token(api_key,sessionwithoutvesionId,state)

print(access_token)

# Make a object for SharekhanConnect class
#"""Here we are passing the api-key, access-token and vendor-key(when needed) as a request header parameters"""
access_token = "Your access token value"
sharekhan = SharekhanConnect(api_key,access_token)
print(sharekhan.requestHeaders())   # for printing request headers

# Place order history

orderparams={
 "customerId": "946423",
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B", #--> (B, S, BM, SM, SAM)
 "quantity": 1,
 "disclosedQty": 0,
 "price": "149.5",
 "triggerPrice": "0",
 "rmsCode": "ANY",
 "afterHour": "N",
 "orderType": "NORMAL",
 "channelUser": "sunitab63",  #(Use LoginId as ChannelUser)
 "validity": "GFD",
 "requestType": "NEW",
 "productType": "INVESTMENT" #--> (INVESTMENT or (INV), BIGTRADE or (BT), BIGTRADEPLUS or (BT+))
 #Below parameters need to be added for FNO trading
"instrumentType": "FUTCUR"; #--> (Future Stocks(FS)/ Future Index(FI)/ Option Index(OI)/ Option Stocks(OS)/ Future Currency(FUTCUR)/ Option Currency(OPTCUR))
"strikePrice": "-1";
"optionType": "XX"; #--> (XX/PE/CE)
"expiry": "31/03/2023";
}

 order=sharekhan.placeOrder(orderparams)
 print("PlaceOrder: {}".format(order))

# modify order

orderparams={
 "orderId":"XXXXXXXXXXX",
   "customerId": "XXXXXXX",
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B",--> (B, S, BM, SM, SAM)
 "quantity": 1,
 "disclosedQty": 0,
 "price": "149.5",
 "triggerPrice": "0",
 "rmsCode": "ANY",
 "afterHour": "N",
 "orderType": "NORMAL",
 "channelUser": "XXXXXXX",  (Use LoginId as ChannelUser)
 "validity": "GFD",
 "requestType": "MODIFY",
 "productType": "INVESTMENT"--> (INVESTMENT or (INV), BIGTRADE or (BT), BIGTRADEPLUS or (BT+))
 #Below parameters need to be added for FNO trading
"instrumentType": "FUTCUR";--> (Future Stocks(FS)/ Future Index(FI)/ Option Index(OI)/ Option Stocks(OS)/ Future Currency(FUTCUR)/ Option Currency(OPTCUR))
"strikePrice": "-1";
"optionType": "XX";--> (XX/PE/CE)
"expiry": "31/03/2023";
}
order=sharekhan.modifyOrder(orderparams)
print("ModifyOrder: {}".format(order))

# cancel  order

orderparams={
 "orderId":"XXXXXXX",
 "customerId": "XXXXXXX",
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B",--> (B, S, BM, SM, SAM)
 "quantity": 1,
 "disclosedQty": 0,
 "price": "149.5",
 "triggerPrice": "0",
 "rmsCode": "ANY",
 "afterHour": "N",
 "orderType": "NORMAL",
 "channelUser": "XXXXXXX",  (Use LoginId as ChannelUser)
 "validity": "GFD",
 "requestType": "CANCEL",
 "productType": "INVESTMENT"--> (INVESTMENT or (INV), BIGTRADE or (BT), BIGTRADEPLUS or (BT+))
 #Below parameters need to be added for FNO trading
"instrumentType": "FUTCUR";--> (Future Stocks(FS)/ Future Index(FI)/ Option Index(OI)/ Option Stocks(OS)/ Future Currency(FUTCUR)/ Option Currency(OPTCUR))
"strikePrice": "-1";
"optionType": "XX";--> (XX/PE/CE)
"expiry": "31/03/2023";
}
order=sharekhan.cancelOrder(orderparams)
print("CancelOrder: {}".format(order))

# Retrieves all positions

customerId="customerId < int data type>"
order=sharekhan.trades(customerId)
print("Postion Reports: {}".format(order))

# Retrieve history of an given order

exchange="exchange value <string>"
customerId="customerId <int data type>"
orderId="orderId <int data type>"
order=sharekhan.exchange(exchange, customerId, orderId)
print("Order Details: {}".format(order))

# Retrieves the trade  generated by an order

exchange="exchange value <string>"
customerId="customerId <int data type>"
orderId="orderId <int data type>"
order=sharekhan.exchangetrades(exchange, customerId, orderId)
print("Trade Generated By an Order : {}".format(order))


# services Holdings

customerId="customerId <int data type>"
order=sharekhan.holdings(customerId)
print("Holdings : {}".format(order))

# Script Master

exchange="exchange value <string>"
order=sharekhan.master(exchange)
print("Script Master : {}".format(order))


# Historical Data

exchange="exchange value <string>"
scripcode="Unique scripcode provided by the broker <int>"
interval="Available Intervals <string>"
order=sharekhan.historicaldata(exchange, scripcode, interval)
print("Holdings Data: {}".format(order))