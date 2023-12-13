import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials_file.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the specific Google Sheet (by its URL or name)
sheet = client.open('Your Google Sheet Name')

# Access a specific worksheet
worksheet = sheet.worksheet('Sheet1')  # Replace 'Sheet1' with your sheet name

# Get all values from the worksheet
values = worksheet.get_all_values()

# Print the values
for row in values:
    print(row)
