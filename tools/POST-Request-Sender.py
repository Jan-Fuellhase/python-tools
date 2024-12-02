import requests

# API URL
url = "https://pastebin.com/api/api_login.php"

# Your credentials
payload = {
    "api_dev_key": "kinder123",
    "api_user_name": "Jan_Boyega",
    "api_user_password": "kinderkinder123"
}

# Sending POST request
response = requests.post(url, data=payload)

# Checking response
if response.status_code == 200:
    print(f"User Key: {response.text}")
else:
    print(f"Error: {response.status_code} - {response.text}")
