from twitter.account import Account
from utils import read_secret, get_id, read_secrets

# Authenticate to Twitter
secret = read_secrets()
accounts = {}
for id in secret:
    accounts[id] = Account(cookies={"ct0": secret[id]["ct0"], "auth_token": secret[id]["auth_token"]})
print(accounts)

# get the user id of @wired
id = get_id("wired")
for account in accounts.values():
    account.follow(id)
    print(f"Followed @wired from @{list(accounts.keys())[list(accounts.values()).index(account)]}")

