# -*- coding:utf-8 -*-
import requests
import json

def show_weather(location):
    result1 = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={
        'key': 'mbghskqqeagdjdqt',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=60)
    result2 = requests.get(
        'https://api.seniverse.com/v3/life/suggestion.json',
        params={
        'key': 'mbghskqqeagdjdqt',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=60)
    weather_data = result1.json()
    life_data = result2.json()
    w = weather_data['results'][0]
    l = life_data['results'][0]['suggestion']
    result_dic = {}
    result_dic['location'] = w['location']['name']
    result_dic['text_day'] = w['daily'][0]['text_day']
    result_dic['text_night'] = w['daily'][0]['text_night']
    result_dic['high'] = w['daily'][0]['high']
    result_dic['low'] = w['daily'][0]['low']
    result_dic['wind_direction'] = w['daily'][0]['wind_direction']
    result_dic['last_update'] = w['last_update'][:-6].replace('T', ' ')
    result_dic['sport'] = l['sport']['brief']
    result_dic['uv'] = l['uv']['brief']
    return result_dic
