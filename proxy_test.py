import requests
# post with proxy and check ip
with open("proxy.secret") as f:
    proxy = f.read()
print(proxy)
r = requests.get("https://api.ipify.org", proxies={"https": proxy})
print(r.text)