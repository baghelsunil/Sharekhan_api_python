

import datetime

current_time = datetime.datetime.now().time()


print(current_time.minute % 2)


	
'''		
if msg_json['status'] == 100:
		new_row = {'date_time': msg_json['timestamp'], 'LTP': msg_json['data']['ltp']}
		data = data.append(new_row, ignore_index=True)
'''

if current_time.minute % 2 == 0	:
		print("---------------------------------------")
		#print(data)
		print("---------------------------------------")

