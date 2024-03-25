from utils import Manager

# enter the username of the account you want to follow
username = input("Enter the username of the account you want to follow: ") or "wired"
amount = int(input("Enter the number of accounts you want to use to follow (-1 for all): ") or 1)
proxy = input("Enter the proxy you want to use (leave blank for no proxy): ")
if proxy:
    proxy = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
else:
    proxy = None

mgr = Manager(proxy=proxy)
mgr.follow(username=username, amount=amount)