import ipfshttpclient

# Connect to the IPFS daemon
client = ipfshttpclient.connect()

# Specify the IPFS hash of the file you want to retrieve
ipfs_hash = "QmZPsryoJrNKbk1T8SyWHpr22c3AGczHkJY1cKJh8VMzs8"

# Retrieve the file using a HTTP GET request
response = client.cat(ipfs_hash)

# Print the contents of the file
print(response.decode())
