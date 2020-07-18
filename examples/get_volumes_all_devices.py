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
# Get a list of volumes for all devices as Python dictionaries
volumes = client.get_volumes()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
volumes = json.dumps(volumes)
# Now we can write the results to a JSON file.
with open('volumes.json', 'w', newline='') as f:
    print(volumes, file=f)
