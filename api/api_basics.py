import requests

response = requests.get("https://tryhackme.com/room/metasploitthebasics")
print(response.status_code)

print(response.json())