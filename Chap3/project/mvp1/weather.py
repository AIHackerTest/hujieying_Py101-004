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
    location = w['location']['name']
    text_day = w['daily'][0]['text_day']
    text_night = w['daily'][0]['text_night']
    high = w['daily'][0]['high']
    low = w['daily'][0]['low']
    wind_direction = w['daily'][0]['wind_direction']
    last_update = w['last_update']
    sport = l['sport']['brief']
    uv = l['uv']['brief']
    weather_info = '{}今日天气：白天{}，晚间{}，最高气温{}℃，最低气温{}℃，{}，'.format(
        location, text_day, text_night, high, low, wind_direction)
    life_info = '运动适宜度：{}，紫外线强度：{}，更新时间{}'.format(sport, uv, last_update)

    user_info = weather_info + life_info
    return user_info
