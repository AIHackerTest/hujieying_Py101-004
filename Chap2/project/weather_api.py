# -*- coding:utf-8 -*-
import requests
import json
from textwrap import dedent

# 通过两个API获取信息。
# 获取基础天气信息
def fetch_weather(location):
    result = requests.get(
        'https://api.seniverse.com/v3/weather/daily.json',
        params={
        'key': 'mbghskqqeagdjdqt',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=60)
    return result.text

# 获取基于天气状况的关于生活的信息
def fetch_life(location):
    result = requests.get(
        'https://api.seniverse.com/v3/life/suggestion.json',
        params={
        'key': 'mbghskqqeagdjdqt',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=60)
    return result.text

# 对获取的天气信息进行解析
def process_weather(result):
    weather_data = json.loads(result)
    location = weather_data['results'][0]['location']['name']
    date = weather_data['results'][0]['daily'][0]['date']
    text_day = weather_data['results'][0]['daily'][0]['text_day']
    text_night = weather_data['results'][0]['daily'][0]['text_night']
    wind_direction = weather_data['results'][0]['daily'][0]['wind_direction']
    high = weather_data['results'][0]['daily'][0]['high']
    low = weather_data['results'][0]['daily'][0]['low']
    weather_info = '{}{}的天气情况如下：\n白天天气：{}，晚间天气：{}，最高气温：{}摄氏度，最低气温：{}摄氏度，风向：{}\n'.format(
        location, date, text_day, text_night, high, low, wind_direction)
    return weather_info

# 对获取的生活信息进行解析
def process_life(result):
    life_data = json.loads(result)
    sport = life_data['results'][0]['suggestion']['sport']['brief']
    uv = life_data['results'][0]['suggestion']['uv']['brief']
    life_info = '运动适宜度：{}，紫外线强度：{}\n'.format(sport, uv)
    return life_info

# 合并从多个API获取的信息
def show_info(user_input):
    user_info = process_weather(fetch_weather(user_input)) + process_life(
        fetch_life(user_input))
    return(user_info)

# 定义退出程序函数
def out(history_info):
    if len(history_info) > 0:
        print('即将退出本程序，谢谢使用，以下是你的查询历史：')
        print(history_info)
    else:
        print('你没有进行城市查询，即将退出本程序，谢谢使用')

    quit(0)

# 主函数
def main():
    history_info = ''
    help_doc = dedent('''
        输入城市名或拼音，查询该城市的天气情况；
            比如：北京，四川成都，beijing，sichuan chengdu
        输入help或h，获取帮助文档；
        输入history或his，获取查询历史；
        输入quit或q，退出天气查询系统。''')
    print('----该程序数据由心知天气提供----')
    while True:
        print('请输入城市名称或拼音查询天气；如需获取帮助，请输入help或h。')
        user_input = input('>>>')
        if user_input in ['help', 'h']:
            print(help_doc)
        elif user_input in ['quit', 'q']:
            out(history_info)
        elif user_input in ['history', 'his']:
            if len(history_info) > 0:
                print('这是你的搜索记录：')
                print(history_info)
            else:
                print('你还没有查询过天气')
        else:
            try:
                history_data = show_info(user_input)
                print(history_data)
                history_info += '\n' + history_data
            except Exception as exc:
                print('你输入的城市名有误或包含多余空格，或暂不能提供该城市天气信息，请重新输入\n')

if __name__ == '__main__':
    main()
