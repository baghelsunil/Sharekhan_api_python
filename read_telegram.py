


import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
import pandas as pd
import nltk
# Replace the values with your own API ID, API hash and phone number
# enter your api id from telegram website
name = 'TEST'
api_id = 8915731
api_hash = '01a519f12ce20e888b8ff13226f9189e'
chat = 'me'
# enter your api hash form telegram api website
phone_number = '+6598272559'
# enter your pone number on this formate

#group_name = '@dabbatradingbulleye'
group_name='@SafeShareTrading'
#group_name = -1770216819
# enter your channel group id -100 after this digit


TELEGRAM_API_TOKEN = '6892868655:AAHYz80uP417eLmvbRf-iYZ1V7qsTVNw_hE'


# Set the time range to get messages from
start_time = datetime.now() - timedelta(hours=24)
flag=0
async def get_group_messages():
    df = pd.DataFrame({'Data':[''],'name':[''],'mobile':['']})
    df1 = pd.DataFrame({'Data':[''],'name':[''],'mobile':['']})
    # Create a Telegram client with the specified API ID, API hash and phone number
    client = TelegramClient('session_name', api_id, api_hash)
    await client.connect()

    # Check if the user is already authorized, otherwise prompt the user to authorize the client
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))

    # Get the ID of the specified group
    group = await client.get_entity(group_name)
    date_today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    yesterday = date_today - timedelta(days=1)
    messages = []
    # below commented code is used for  specified time range
    async for message in client.iter_messages(group, min_id=1):
        print(message.date ,yesterday)
        print( message.message)
        if str(message.date) < str(yesterday):
            break
        messages.append(message)

asyncio.run(get_group_messages())



