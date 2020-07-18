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
# Get a list of device health reports for all devices as Python dictionaries
device_health = client.get_device_health()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
device_health = json.dumps(device_health)
# Now we can write the results to a JSON file.
with open('device_health.json', 'w', newline='') as f:
    print(device_health, file=f)
