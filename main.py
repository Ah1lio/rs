import requests
import json

url = 'https://akabab.github.io/superhero-api/api/all.json'
# resp = requests.get(url)

# print(resp.json)

names_of_characters = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
intelligence = {}

for names in names_of_characters:
    response = requests.get(url)
    # print(response.status_code)
    if response == 'success':
        intelligence[names] = intelligence.update(int(response['results'][0]['powerstats']['intelligence']))
    print(intelligence)



