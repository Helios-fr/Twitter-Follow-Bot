'''
This file was used to workshop the base features of the bot before it was implemented into the main program
'''
from utils.twitter.account import Account
from utils import read_secret, get_id, read_secrets
from httpx import Client

# Authenticate to Twitter
secret = read_secrets()
with open("proxy.secret") as f:
    proxy = f.read()
accounts = {}
for id in secret:
    accounts[id] = Account(cookies={"ct0": secret[id]["ct0"], "auth_token": secret[id]["auth_token"]}, session=Client())
print(accounts)

# get the user id of @wired
id = get_id("DrDemography")
print(id)
for account in accounts.values():
    r = account.follow(id)
    print(r)
    print(f"Followed @wired from @{list(accounts.keys())[list(accounts.values()).index(account)]}")
