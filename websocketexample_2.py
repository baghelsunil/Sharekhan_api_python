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

data = {'Datetime': [""],
        'LTP': ['']}

df = pd.DataFrame(data)


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


file_name = "niftybank_live.json"
print("-------------------------- params")
print(params)

token_list = {"action": "subscribe", "key": ["feed"], "value": [""]}
#feed = {"action":"feed","key":["ltp"],"value":["NC26009,MCXENERGY325"]}
#feed = {"action":"feed","key":["ltp"],"value":["GOLD253440","CRUDEOIL258003","NC26009"]}

feed = {"action":"feed","key":["ltp"],"value":["MX572"]}

unsubscribefeed = {"action":"unsubscribe","key":["feed"],"value":["NC22,NF37833,NF37834,MX253461,RN7719"]}
file_name = "niftybank_5min.csv"

sws = SharekhanWebSocket(access_token=access_token_2)
high_5_min = 0
low_5_min = 0
column_index =2  

array_5min = []
new_row_array=['2023-12-08T20:42:07+05:30', 18788.91]


def high_low(csv_reader):
    
	column_values = [int(row[column_index]) for row in csv_reader]
	# Find the highest and lowest values
	highest_value = max(column_values)
	lowest_value = min(column_values)
	print("high -----",highest_value )
	print("Low -----",lowest_value )



def on_data(wsapp, message):
	
	#msg_out = "{}".format(message)
	#print(message)
	msg_json = json.loads(message)
	current_time = datetime.datetime.now().time()
	#print(msg_json['timestamp'], msg_json['data']['ltp'])
	
	new_row = {'Datetime': msg_json['timestamp'], 'ltp': msg_json['data']['ltp']}
	new_row_array.append(msg_json['timestamp'], msg_json['data']['ltp'])

	print(new_row_array)
	
	if current_time.minute % 2 == 0 :
		print("im here ---------")
		high_low(new_row_array)
	#df = df.append(new_row, ignore_index=True)
	

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