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
# Get drives and controllers as Python dictionaries
drives = client.get_raid_drives()
controllers = client.get_raid_controllers()
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
drives = json.dumps(drives)
controllers = json.dumps(controllers)
# Now we can write the drives and raid controllers to JSON files.
with open('drives.json', 'w', newline='') as f:
    print(drives, file=f)

with open('controllers.json', 'w', newline='') as f:
    print(controllers, file=f)
