import ninjarmmpy
import os
import json

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
    AccessKeyID=os.environ.get('NRMM_KEY_ID'),
    SecretAccessKey=os.environ.get('NRMM_SECRET'),
    Europe=False
)
# Get usernames and logon times for all devices as Python dictionaries
logged_on_users = client.get_logged_on_users()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
logged_on_users = json.dumps(logged_on_users)
# Now we can write the results to a JSON file.
with open('logged_on_users.json', 'w', newline='') as f:
    print(logged_on_users, file=f)
