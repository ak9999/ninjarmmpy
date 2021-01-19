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
# Get a list of computer systems for 5 devices as Python dictionaries
computer_systems = client.getComputerSystems(pageSize=5)
# For this example, we're just going to convert the dictionaries to JSON and write them to a file.
computer_systems = json.dumps(computer_systems)
# Now we can write the results to a JSON file.
with open('computer_systems.json', 'w', newline='') as f:
    print(computer_systems, file=f)
