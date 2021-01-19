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
# Get a list of os patches for 5 devices as Python dictionaries
os_patches = client.getPendingFailedRejectedOSPatches(pageSize=5)
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
os_patches = json.dumps(os_patches)
# Now we can write the results to a JSON file.
with open('os_patch_installs.json', 'w', newline='') as f:
    print(os_patches, file=f)
