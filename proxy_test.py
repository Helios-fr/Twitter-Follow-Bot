import requests
from requests.auth import HTTPProxyAuth
# post without proxy
r = requests.get("https://api.ipify.org")
print(r.text)
# post with proxy and check ip
with open("proxy.secret") as f:
    proxy = f.read()
print(proxy)
r = requests.get("http://api.ipify.org", proxies={"http": f"http://{proxy}", "https": f"https://{proxy}"})
print(r.text)