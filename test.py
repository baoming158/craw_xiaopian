import requests
proxies = { "http": "http://113.78.64.133:9797" }
res = requests.get("http://example.org", proxies=proxies)
print(res)
