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
# Get a list of software for all devices as Python dictionaries
software_list = client.get_software_list()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
software_list = json.dumps(software_list)
# Now we can write the results to a JSON file.
with open('software_list.json', 'w', newline='') as f:
    print(software_list, file=f)
