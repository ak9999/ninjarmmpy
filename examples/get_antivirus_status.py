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
# Get antivirus statuses for all devices as Python dictionaries
status = client.get_antivirus_status()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
status = json.dumps(status)
# Now we can write the results to a JSON file.
with open('av_status.json', 'w', newline='') as f:
    print(status, file=f)
