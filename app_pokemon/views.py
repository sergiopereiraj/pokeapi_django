from django.shortcuts import render
import requests

def pokemon_view(request, pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(response.text)
    else:
        pokemon_data = None
    return render(request, 'app_pokemon\pokemon_template.html', {'pokemon_data': pokemon_data})

#fetch_api_pokemon\app_pokemon\templates\app_pokemon\pokemon_template.html