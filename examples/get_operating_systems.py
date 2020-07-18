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
# Get operating systems for all devices as Python dictionaries
operating_systems = client.get_operating_systems()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
operating_systems = json.dumps(operating_systems)
# Now we can write the results to a JSON file.
with open('os.json', 'w', newline='') as f:
    print(operating_systems, file=f)
