import requests
import json
import yfinance as yf
import datetime
from tabulate import tabulate
from prettytable import PrettyTable

import pandas as pd
# Create an empty DataFrame with columns
columns = ["Stock", "hold", "Current", "Aval_qty", "hold_cost", "hold_curr_diff"]
df = pd.DataFrame(columns=columns)


import warnings
warnings.filterwarnings("ignore")

# Get the current date and time
now = datetime.datetime.now()
bot_token = '6892868655:AAHYz80uP417eLmvbRf-iYZ1V7qsTVNw_hE'

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


def main():

    file_name_1 = "Sharekhan_portfolio"
    file_path_tele=portfolio_price(file_name_1)
    
    send_msg_tel = open(file_path_tele).read()
    send_to_telegram(send_msg_tel)
    
    file_name_1 = "TW_Portfolio"
    file_path_tele=portfolio_price(file_name_1)
    
    send_msg_tel = open(file_path_tele).read()
    send_to_telegram(send_msg_tel)
    
    file_name_1 = "SYFE_IBKR_Portfolio"
    file_path_tele=portfolio_price(file_name_1)
    send_msg_tel = open(file_path_tele).read()
    send_to_telegram(send_msg_tel)
    
    file_name_1 = "SG_Portfolio"
    file_path_tele=portfolio_price(file_name_1)
    send_msg_tel = open(file_path_tele).read()
    send_to_telegram(send_msg_tel)
# end of main function 


def portfolio_price(file_name_1):
	file_path = file_name_1 + ".json"  # Reading sharekhan portfolio
	file_path_tele = file_name_1 +".txt" #sending message for sharekhan
	print(file_path,file_path_tele )	
	f = open(file_path)
	Holdings_data = json.load(f)
	
	with open(file_path_tele, 'w+') as file_name: # Write the data to the file
		print(file_name_1 + " :: " + now.strftime("%Y-%m-%d %H:%M:%S"), file=file_name)
		for item in Holdings_data['data']:
			if item['exchange'] == "Nasdaq":
				exchange = ""
			elif item['exchange'] == "NSE":
				exchange = ".NS"
			else:
				exchange = "."+item['exchange'] 
			
			price = get_stock_price(item['tradingSymbol']+exchange)
			print("-----------------------", file=file_name)
			if price is not None:
				row = {"Stock" : item['tradingSymbol'] }
				#print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price,2)],['% change', get_change(round(price,2),item['holdPrice'])]], tablefmt="plain"), file=file_name)
				print((float(item['aval']) * float(price) ) - (float(item['aval']) * float(item['holdPrice']) ))
			else:
				price_BO = get_stock_price(item['tradingSymbol']+".BO")
				if price_BO is not None:
					print("hello")
					#print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']] ,['Curr Price', round(price_BO,2)],['% change', get_change(round(price_BO,2),item['holdPrice'])]], tablefmt="plain"), file=file_name)
				else:
				    print("hello")
					#print(tabulate([['Stock', item['tradingSymbol']],['Hold Price',item['holdPrice']]], tablefmt="plain" ), file=file_name)
	return file_path_tele 
  
 
 
# main function calling 

if __name__ == "__main__":
    main()





