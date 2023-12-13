from SharekhanApi.sharekhanConnect import SharekhanConnect
import requests
import json
import yfinance as yf
from tabulate import tabulate
import datetime
from prettytable import PrettyTable


import warnings
#warnings.filterwarnings("ignore")

api_key = "p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj"
login = SharekhanConnect(api_key)
vendor_key = ""         # vendor key for vendor login otherwise keep it null
version_id = "1005"         # version id= 1005 or 1006 otherwise keep it null
state=12345
#url = login.login_url(vendor_key, version_id)
#url="https://api.sharekhan.com/skapi/auth/login.html?api_key=p5ZoRAd5kLpYsZGh1VVIpXmcAOX4WrWj&state=12345&version_id=1005"
customerId="946423"

# telegram code here 
bot_token = '6892868655:AAHYz80uP417eLmvbRf-iYZ1V7qsTVNw_hE'
TOKEN = bot_token

#:up: UP! button :arrow_up_small:
#up button
#:arrow_down_small:
#down button
#:arrow_up:
#up arrow
#:arrow_down:
#down arrow
#:small_red_triangle_down:
#red triangle pointed down


def send_to_telegram(message):

    apiToken = bot_token
    chatID = '1556120359'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response.text)
    except Exception as e:
        print(e)

# ----------------


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        #return round(((current - previous) / previous) * 100.0,2)
        a=round(((current - previous) / previous) * 100.0,2)
        if a > 0:
         return str(a) + '\U00002747'
        else:
         return str(a) + '\U0000203C'
        
    except ZeroDivisionError:
        return 0


def get_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    stock_info = stock.history(period='1d')  # Fetching today's data

    if not stock_info.empty:
        current_price = stock_info['Close'][0]
        return current_price
    else:
        return None


#def login_url(self, vendor_key=None, version_id=None):"""Get the remote login URL to which a user should be redirected to initiate the login flow."""
#base_url = "{}?api_key={}".format(self._login_url, self.api_key)
# Check if vendor_key is provided and add it to the URL if available
#if vendor_key:base_url += "&vendor_key={}".format(vendor_key)
#else:print("No Vendor Key")# state parameter in the URL is set to 
#12345base_url += "&state=12345"# Check if version_id is provided and add it to the URL if availableif 
#version_id:base_url += "&version_id={}".format(version_id)else:print("No Version Id")
#return base_url

f = open('access_token.txt')
access_token = f.read()
#print(access_token)

#access_token = dict({'status': 200, 'message': 'access_token', 'timestamp': '2023-11-11T13:38:23+05:30', 'data': {'customerId': '946423', 'btplusServiceEnabled': False, 'loginId': 'SUNITAB63', 'token': 'eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJJNkxrMnFLM3FpZ1RTMFFDR2ZMMzliMXNKZTFEcXMvQUtvbDJkSGNydHNFV3FyZHZuZ3JGWVIvUDRJdXZsZi8rSTQ3YzhUSGgyb2VXdDBZbTdLYndkSDZQNmZLem0yM2FUUFdEZFZPcTRUUTZibElvYXhoTzdlUVhRT1ZMRHQ4OFJwVmpTZWJiRFZFY01SY2l0SnBGUm5VVE9rL1dzRzYwZS9udnVCcE03Zk09IiwiaWF0IjoxNjk5NjkwMTAzLCJleHAiOjE2OTk3MjczOTl9.mM9N1wYb0gG7WdmuAx21f1KOI5pVgf1q_TYPlmYPPpQ', 'userId': None, 'exchanges': ['NF', 'BC', 'NC'], 'state': '12345', 'broker': 'Sharekhan', 'fullName': 'Sunita Sunita Baghel'}})

#print("access token type ******* -------------------")
#print(type(access_token))
#print((access_token))
#print("access token ******* -------------------")
#print(access_token['access-token']['data']['token'])

#print(access_token['data']['token'])

#access_token_1=access_token['access-token']['data']['token']

#access_token_1=access_token['data']['token']

access_token_1=access_token

# Get the current date and time
now = datetime.datetime.now()

#access_token = "Your access token value"
#sharekhan = SharekhanConnect(api_key,access_token)
sharekhan = SharekhanConnect(api_key,access_token=access_token_1)

#print("sharekhan ******* -------------------")
#print(sharekhan)
#print("sharekhan request headers ******* -------------------")
#print(sharekhan.requestHeaders())       # for printing request headers


# Replace this URL with the one you want to call
#url = 'https://api.sharekhan.com/skapi/services/reports/946423'
url_holdings = 'https://api.sharekhan.com/skapi/services/holdings/946423'

# Send an HTTP GET request to the URL
response = requests.get(url_holdings)



customerId="946423"



#Script Master

exchange="MX"
order=sharekhan.master(exchange)
file_name = "script.txt"
print("Script Master : {}".format(order) )


file_path = "Sharekha_stocks.json"

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print('Sharekhan Request was successful!')
    
    Holdings=sharekhan.holdings(customerId)
    Holdings_data = json.loads(json.dumps(Holdings))
    print(format(json.dumps(Holdings, indent=4)))
    with open(file_path, 'w') as file:
    # Write the data to the file
     file.write((format(json.dumps(Holdings, indent=4)))
	)
    
    # Print the content of the response
#    print(response.text)
else:
    print(f'Error: Request failed with status code {response.status_code}')
    # Opening JSON file
    f = open(file_path)
    Holdings_data = json.load(f)

# returns JSON object as 
# a dictionary

    

# services Holdings
#print(format(json.dumps(Holdings, indent=4)))
#print(type(Holdings))
#print(Holdings_data)




# Open the file in write mode ('w' mode)





file_path_tele = "tel_message_sharekhan.txt"

# Iterate through the JSON array
with open(file_path_tele, 'w+') as file_name:
    # Write the data to the file
    for item in Holdings_data['data']:
     price = get_stock_price(item['tradingSymbol']+".NS")
          
     if price is not None:
      #file.write(item['tradingSymbol']+ item['holdPrice'] + round(price,2) + (get_change(round(price,2)+ item['holdPrice'])
      print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price,2)],['% change', get_change(round(price,2),item['holdPrice'])]],headers=['', '', '', '']), file=file_name)

     else:
      price_BO = get_stock_price(item['tradingSymbol']+".BO")
      if price_BO is not None:
       print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price_BO,2)],['% change', get_change(round(price_BO,2),item['holdPrice'])]],headers=['', '', '', '']), file=file_name)
      else:
       print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']]] , headers=['', '']), file=file_name)
      

file_name.close()


send_msg_tel = open(file_path_tele).read()

send_to_telegram("Sharekhan Portfolio\n"+now.strftime("%Y-%m-%d %H:%M:%S"))
send_to_telegram(send_msg_tel)



file_path_tele = "tel_message_Us_Portfolio.txt"

# Opening JSON file
f = open('US_Stock.json')
file_name=open(file_path_tele,"w+")

# returns JSON object as 
# a dictionary
data = json.load(f)


# Iterating through the json
# list
for item in data:
 #print(item['STOCK'])
 price = get_stock_price(item['STOCK'])
 if price is not None:
  #file.write(item['tradingSymbol']+ item['holdPrice'] + round(price,2) + round(get_change(round(price,2)+ item['holdPrice']),2))
  print(tabulate([['Stock', item['STOCK']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price,2)],['% change', get_change(round(price,2),item['holdPrice'])]],headers=['', '', '', '']), file=file_name)
 else:
  print(tabulate([['Stock', item['STOCK']],['Hold Price',item['holdPrice']]] , headers=['', '']), file=file_name)
  


# Closing file
file_name.close()

send_msg_tel = open(file_path_tele).read()

send_to_telegram("US Portfolio Syfe and IBKR\n"+now.strftime("%Y-%m-%d %H:%M:%S"))
send_to_telegram(send_msg_tel)

# Place order history





file_path_tele = "tel_message_tw.txt"



# Opening JSON file
f = open('TW_Stocks.json')
# returns JSON object as 
# a dictionary
Holdings_data = json.load(f)


t = PrettyTable(['Stock', '.', ' '])
t.add_row(['H Price', 'C Price', '% Change'])


# Iterate through the JSON array
with open(file_path_tele, 'w+') as file_name:
    # Write the data to the file
    for item in Holdings_data['data']:
     price = get_stock_price(item['tradingSymbol']+".NS")
          
     if price is not None:
      #file.write(item['tradingSymbol']+ item['holdPrice'] + round(price,2) + round(get_change(round(price,2)+ item['holdPrice']),2))
      #print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price,2)],['% change', round(get_change(round(price,2),item['holdPrice']),2)]],headers=['', '', '', '']), file=file_name)
      #print(tabulate([[ item['tradingSymbol'],item['holdPrice'], round(price,2), round(get_change(round(price,2),item['holdPrice']),2)]],headers=['', '', '', '']), file=file_name)
      t.add_row([item['tradingSymbol'],'',''])
      t.add_row([item['holdPrice'], round(price,2), get_change(round(price,2),item['holdPrice'])])
     else:
      price_BO = get_stock_price(item['tradingSymbol']+".BO")
      if price_BO is not None:
       #print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price_BO,2)],['% change', get_change(round(price_BO,2),item['holdPrice'])]],headers=['', '', '', '']), file=file_name)
       t.add_row([item['tradingSymbol'], item['holdPrice'], round(price,2), get_change(round(price_BO,2),item['holdPrice'])])
      else:
       #print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']]] , headers=['', '']), file=file_name)
       t.add_row([item['tradingSymbol'], item['holdPrice'], 0, 0,0])
    
    print("TW Portfolio\n"+now.strftime("%Y-%m-%d %H:%M:%S"),file=file_name)
    print(t,file=file_name)
      
file_name.close()
send_msg_tel = open(file_path_tele).read()
send_to_telegram(send_msg_tel)
print(send_msg_tel)




orderparams={
 "customerId": customerId,
 "scripCode": 2475,
 "tradingSymbol": "ONGC",
 "exchange": "NC",
 "transactionType": "B",
 "quantity": 1,
 "disclosedQty": 0,
 "price": "174.50",
 "triggerPrice": "0",
 "rmsCode": "ANY",
 "afterHour": "Y",
 "orderType": "NORMAL",
 "channelUser": "sunitab63",
 "validity": "MYGTD",
 "gtdd" :"01/12/2023",
 "requestType": "NEW",
 "productType": "INVESTMENT"
}

#order=sharekhan.placeOrder(orderparams)
#print("PlaceOrder: {}".format(order))








# Script Master

exchange="NF"
#script_master=sharekhan.master(exchange)
script_master=""
#print("Script Master : {}".format(json.dumps(script_master, indent=4)))


# Define the file path
file_path = "output.txt"

# Open the file in write mode ('w' mode)
with open(file_path, 'w') as file:
    # Write the data to the file
    file.write(("Script Master : {}".format(json.dumps(script_master, indent=4)))
)
