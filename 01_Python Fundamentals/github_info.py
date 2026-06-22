import requests

response = requests.get("https://api.github.com")

data = response.json()

print(data["current_user_url"])
print(data["repository_url"])
print(data["issues_url"])