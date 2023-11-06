import requests

api_key = 'da48b364-8861-4ada-a70e-8d0bdf180630'
word = 'voluminous'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
