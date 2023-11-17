import requests

url = "https://pokeapi.co/api/v2/pokemon/"
params = {'limit': 100}

for offset in range(0, 1000, 100):
    params['offset'] = offset  # add new value to dict with `limit`
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print('Error: ' + str(response.status_code) + ' - ' + response.text + '\n' + response.url)
    else:
        data = response.json()

        for item in data['results']:
            print(item['name'] + ' - ' + item['url'])
