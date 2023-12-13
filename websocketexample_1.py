# websocket Programming Testing

from SharekhanApi.sharekhanWebsocket import SharekhanWebSocket
import time
import json
import datetime

import pandas as pd


#access_token = "Your Access Token Value"

f = open('access_token.txt')
access_token_2 = f.read()
print(access_token_2)


print( "------------- type ----------- ")
print(type(access_token_2))


data = {'Date_time': ['2023-12-13T13:21:19+05:30'], 'LTP': [47150.75]}
#data = {'Date_time': ['2023-12-13T12:36:16+05:30'],'LTP': [46000.00]}

df = pd.DataFrame(data)

print(df)

'''

# Creating a class
class MyObject:
    def __init__(self, value):
        self.value = value

# Creating an instance of the class and assigning it to a variable
access_token = MyObject(access_token_2)
'''

params = {
    "access_token": access_token_2
}
action = 1
mode = 1


i = 0


file_name = "niftybank_live.json"
print("-------------------------- params")
print(params)

token_list = {"action": "subscribe", "key": ["feed"], "value": [""]}
#feed = {"action":"feed","key":["ltp"],"value":["NC26009,MCXENERGY325"]}
feed = {"action":"feed","key":["ltp"],"value":["NC26009"]}
unsubscribefeed = {"action":"unsubscribe","key":["feed"],"value":["NC22,NF37833,NF37834,MX253461,RN7719"]}
file_name = "niftybank_5min.csv"

sws = SharekhanWebSocket(access_token=access_token_2)
high_5_min = 0
low_5_min = 0



def on_data(wsapp, message):
	
	#msg_out = "{}".format(message)
	#print(message)
	msg_json = json.loads(message)
	current_time = datetime.datetime.now().time()
	
	print(current_time.minute % 2)
	print(msg_json['status'])
	
	print((msg_json['timestamp'], msg_json['data']['ltp']))
	
	if int(msg_json['status']) == 100:
		new_row = {'Date_time': [msg_json['timestamp']], 'LTP': [msg_json['data']['ltp']]}
		df.loc[len(df)] = [msg_json['timestamp'], msg_json['data']['ltp']]
		
	

	if int(current_time.minute % 2) == 0:
		print("---------------------------------------")
		df_2 = pd.DataFrame(df, index=Date_time)
		resampled_df = df_2.resample('5T').agg({'Values': ['max', 'min']})
		print("\nResampled DataFrame:")
		print(resampled_df)

		print(df)
		# Calculate the highest and lowest values from the 'Values' column
		highest_value = df['LTP'].max()
		lowest_value = df['LTP'].min()

		# Print the results
		print("\nHighest Value:", highest_value)
		print("Lowest Value:", lowest_value)
		i=1
		print("---------------------------------------")
	
	#if not int(current_time.minute % 2) == 0:
	#	i=0

		



	

	#print(msg_json['timestamp'], msg_json['data']['ltp'], msg_json['status'])
'''	
		
	if current_time.minute % 2 == 0	:
	 print(array_5min)
	 file_name = "niftybank_5min_" +str(current_time.hour) +str(current_time.minute) +".csv"
	 print(file_name)
	 with open(file_name, 'a') as file:
	  file.write(array_5min)
	
	if msg_json['status'] == 100:
	  	  print(msg_json['timestamp'], msg_json['data']['ltp'])
	  	  if high_5_min < msg_json['data']['ltp']:
	  	   high_5_min = msg_json['data']['ltp']
	  	   print("high-------------",high_5_min)
	  	  
	  	  if low_5_min > msg_json['data']['ltp']:
	  	   low_5_min = msg_json['data']['ltp']
	  	   print("low-------------",low_5_min)
	
	print(current_time.minute % 2)
		
	if current_time.minute % 2 == 0 and msg_json['status'] == 100:
	  print("im here")
	  print(msg_json['timestamp'], msg_json['data']['ltp'],high_5_min, low_5_min)
	  high_5_min = 0
	  low_5_min = 0
'''
	
	#print(msg_out)
	
	#time.sleep(10)

    #with open(file_name, 'a') as file:
    # Write the data to the file
     #file.write("Ticks: {}".format(message))
	#v_high = json("{}".format(message))
	#print(type("{}".format(message))
    #print(v_high['data']['high'])
    #high = message['data']['high']
    #print("high ------", high)
    
    #print("Ticks: {}".format(json.dumps(message, indent=4)))
    #time.sleep(10)


def on_open(wsapp):
    print("on open")
    sws.subscribe(token_list)
    sws.fetchData(feed)
    #sws.unsubscribe(unsubscribefeed)


def on_error(wsapp, error):
    print(error)


def on_close(wsapp):
    print("Close")


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()