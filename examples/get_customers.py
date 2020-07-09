import json
import ninjarmmpy
import os

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
        AccessKeyID=os.environ.get('NRMM_KEY_ID'),
        SecretAccessKey=os.environ.get('NRMM_SECRET'),
        Europe=False
    )

# As of this moment, the NinjaRMMPy package does not automatically convert the JSON into Python objects
# So we need to do it ourselves.
organizations = json.loads(client.get_organizations())
# Now we can print the organizations out to the terminal.
print(organizations)