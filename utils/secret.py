def read_secret(id):
    import os
    with open(os.path.join("keys", f"{id}.secret")) as f:
        return dict(line.strip().split(" = ") for line in f)

def read_secrets(keys_dir="keys"):
    import os
    secrets = {}
    for file in os.listdir(keys_dir):
        if file.endswith(".secret"):
            id = file.removesuffix(".secret")
            secrets[id] = read_secret(id)
    return secrets
if __name__ == "__main__":
    print(read_secret("T34013441088"))