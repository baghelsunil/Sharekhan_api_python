


import json

acc_Token = json.loads('{'status': 200, 'message': 'access_token', 'timestamp': '2023-11-07T19:24:08+05:30', 'data': {'customerId': '946423', 'loginId': 'SUNITAB63', 'userId': None, 'token': 'eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJJNkxrMnFLM3FpZ1RTMFFDR2ZMMzliMXNKZTFEcXMvQUtvbDJkSGNydHNFV3FyZHZuZ3JGWVIvUDRJdXZsZi8rSTQ3YzhUSGgyb2VXdDBZbTdLYndkSDZQNmZLem0yM2FUUFdEZFZPcTRUUTZibElvYXhoTzdlUVhRT1ZMRHQ4OFJwVmpTZWJiRFZFY01SY2l0SnBGUm5VVE9rL1dzRzYwZS9udnVCcE03Zk09IiwiaWF0IjoxNjk5MzY1MjQ4LCJleHAiOjE2OTkzODE3OTl9.mx-AnK5K6AoU8HEWXjiSvJRSBP-hUR_vx_hKWiZJ6iE', 'btplusServiceEnabled': False, 'exchanges': ['NF', 'BC', 'NC'], 'state': '12345'}}')

#z = json.load(acc_Token)
print("********************************")
print(acc_Token)

print("********************************")

print acc_Token['data']['token']