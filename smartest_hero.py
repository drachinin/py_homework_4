import requests
from pprint import pprint


def hero_intelligence(hero_name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{hero_name}'
    res = requests.get(url).json()
    return res['results'][0]['powerstats']['intelligence']

def smartest_hero(superheroes):
    heroes = {}
    for hero in superheroes:
        heroes[int(hero_intelligence(hero))] = hero
    return heroes[sorted(heroes)[-1]]

pprint(smartest_hero(['Hulk', 'Captain America', 'Thanos']))

