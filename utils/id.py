def get_id(username: str) -> str:
    import requests
    response = requests.post('https://tweeterid.com/ajax.php', data={'input': username})
    return response.text

if __name__ == "__main__":
    print(get_id("wired"))