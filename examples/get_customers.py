import ninjarmmpy
import os

# Create our client
# Assuming we are storing our keys in environment variables we can access
client = ninjarmmpy.Client(
    AccessKeyID=os.environ.get('NRMM_KEY_ID'),
    SecretAccessKey=os.environ.get('NRMM_SECRET'),
    Europe=False
)
# Get list of organizations!
organizations = client.getOrganizations()
# Now we can print the organizations out to the terminal.
print(organizations)
