import requests


url = str(input("Enter the URL you want to check the status of (including the):\t"))
response = requests.get(url)

if response.status_code == 200:
    statusCode = "successful"
elif response.status_code == 404:
    statusCode = "not found"
else:
    statusCode = "UNSUCCESSFUL"

print(f"Your request to {url} is {statusCode.upper()}.") 