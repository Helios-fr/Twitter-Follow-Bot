class Manager:
    def __init__(self, keys_dir):
        self.keys_dir = keys_dir
        self.accounts = {}
        self.load_accounts()
        