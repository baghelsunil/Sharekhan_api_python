# websocket Programming Testing

from SharekhanApi.sharekhanWebsocket import SharekhanWebSocket


#access_token = {'status': 200, 'message': 'access_token', 'timestamp': '2023-11-09T21:47:46+05:30', 'data': {'customerId': '946423', 'loginId': 'SUNITAB63', 'token': 'eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJJNkxrMnFLM3FpZ1RTMFFDR2ZMMzliMXNKZTFEcXMvQUtvbDJkSGNydHNFV3FyZHZuZ3JGWVIvUDRJdXZsZi8rSTQ3YzhUSGgyb2VXdDBZbTdLYndkSDZQNmZLem0yM2FUUFdEZFZPcTRUUTZibElvYXhoTzdlUVhRT1ZMRHQ4OFJwVmpTZWJiRFZFY01SY2l0SnBGUm5VVE9rL1dzRzYwZS9udnVCcE03Zk09IiwiaWF0IjoxNjk5NTQ2NjY2LCJleHAiOjE2OTk1NTQ1OTl9.H2CWJJEIBm9K23ykUTylTKMBKIeNOzj_mtqSUUH9FzM', 'userId': None, 'btplusServiceEnabled': False, 'exchanges': ['NF', 'BC', 'NC'], 'broker': 'Sharekhan', 'state': '12345', 'fullName': 'Sunita Sunita Baghel'}}
f = open('access_token_obj.txt')
access_token = f.read()
print(access_token)

params = {
    "access_token": access_token
}
action = 1
mode = 1

token_list = {"action": "subscribe", "key": ["feed"], "value": [""]}
feed = {"action":"feed","key":["ltp"],"value":["MCXSENERGY"]}
unsubscribefeed = {"action":"unsubscribe","key":["feed"],"value":["NC22,NF37833,NF37834,MX253461,RN7719"]}

sws = SharekhanWebSocket(access_token)


def on_data(wsapp, message):
    print("Ticks: {}".format(message))


def on_open(wsapp):
    print("on open")
    # sws.subscribe(token_list)
    # sws.fetchData(feed)
    # sws.unsubscribe(unsubscribefeed)


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