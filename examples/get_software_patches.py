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
# Get a list of software patches for all devices as Python dictionaries
software_patches = client.get_software_patches()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
software_patches = json.dumps(software_patches)
# Now we can write the results to a JSON file.
with open('software_patches.json', 'w', newline='') as f:
    print(software_patches, file=f)
