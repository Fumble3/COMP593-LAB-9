import requests


def get_pokemon_info(name):
    '''
    Gets a dictionary of information from the POKEAPI for a specified pokemon
    
    :param name: Pokemons name
    '''

    print('Getting Pokemon Information...', end='')

    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
    response = requests.get(URL)

    if response.status_code == 200:
            print('Success')
            return response.json() # Convert response body to a dictionary
    else:
        print('Failed. Response code:', response.status_code)
        return
    
def get_pokemon_list(limit=20, offset=0):
    
    print('Getting list of Pokemon...', end='')
    URL = 'https://pokeapi.co/api/v2/pokemon/'
    params = {
        'offset': offset,
        'limit': limit
    }
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        print('Success!')
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']]
    else:
        print('Failed. Response code: ', response.status_code)


def get_pokemon_image_url(name):
    poke_dict = get_pokemon_info(name)
    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url
    