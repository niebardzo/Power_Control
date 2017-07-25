import requests


def request(line):
    buffer = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for i in range(5):
        buffer[i + 1] = line[i]
    r = requests.get('http://127.0.0.1:8000', params=buffer)
    if r.status_code != 200:
        raise ConnectionError