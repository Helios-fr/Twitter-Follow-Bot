from utils import Manager

'''
proxy = {
    "http": "http://username:password@proxy:port",
}
'''

mgr = Manager(proxy=None)

# enter the username of the account you want to follow
username = input("Enter the username of the account you want to follow: ") or "wired"
amount = int(input("Enter the number of accounts you want to use to follow (-1 for all): ") or 1)

mgr.follow(username=username, amount=amount)