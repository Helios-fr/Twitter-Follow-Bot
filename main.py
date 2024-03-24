from utils import Manager

'''
proxy = {
    "http": "http://username:password@proxy:port",
}
'''

mgr = Manager(proxy=None)

mgr.follow("wired", amount=1)