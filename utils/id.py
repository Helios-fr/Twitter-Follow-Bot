def get_id(username: str) -> str:
    import requests
    response = requests.get('https://twitvd.com/twuserid.php', params={'username': 'DrDemography'})
    return response.json()["data"]["user_id"]