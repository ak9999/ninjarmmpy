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
# Get Windows Services for all devices as Python dictionaries
services = client.get_windows_services()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
services = json.dumps(services)
# Now we can write the results to a JSON file.
with open('services.json', 'w', newline='') as f:
    print(services, file=f)
