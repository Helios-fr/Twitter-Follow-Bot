class Manager:
    def __init__(self, keys_dir="keys", proxy=None):
        from . import read_secrets
        from .twitter.account import Account
        self.secrets = read_secrets(keys_dir)
        self.accounts = {}
        for id in self.secrets:
            self.accounts[id] = Account(cookies=self.secrets[id], proxy=proxy)
        
    def follow(self, username=None, id=None, amount=-1):
        if amount == -1:
            accounts = self.accounts
        else:
            from random import sample
            s = sample(sorted(self.accounts), amount)
            accounts = {k: self.accounts[k] for k in s}
        if id is None and username is not None:
            from . import get_id
            id = get_id(username)
        elif id is None and username is None:
            raise ValueError("Either username or id must be provided")

        accounts = {}
        for i in range(amount):
            accounts[list(self.accounts.keys())[i]] = list(self.accounts.values())[i]

        for account in self.accounts.values():
            account.follow(id)
            print(f"Followed {username} from @{list(self.accounts.keys())[list(self.accounts.values()).index(account)]}")

if __name__ == "__main__":
    # run main.py instead
    import os
    os.system("python main.py")
        
        