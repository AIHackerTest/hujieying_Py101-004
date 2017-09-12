import os

#定义一个字典，然后将文件读出的内容存入到字典中。
weather_dic = {}
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
weather_file = root_dir + '/resource/weather_info.txt'

with open(weather_file) as f:
    for line in f:
        (key_info, value_info) = line.split(',')
        weather_dic[key_info] = value_info

history_info = ''

while True:
    print('请输入城市名称查询天气。如果需要帮助，请输入help获得帮助。')
    user_city = input('>>>')

#查询天气
    if user_city in weather_dic:
        user_weather = weather_dic[user_city]
        print(user_city + '的天气是：' + user_weather)
        history_data = user_city + ',' + user_weather + '\n'
        history_info = history_info + history_data

#显示查询历史
    elif user_city in ['history', 'his', 'History']:
        print('这是你的搜索记录：')
        print(history_info)

#显示帮助
    elif user_city in ['help', 'Help', 'h', '-h']:
        print(
        '''
        输入城市名，查询该城市的天气；
        输入help，获取帮助文档；
        输入history，获取查询历史；
        输入quit，退出天气查询系统。
        '''
        )

#退出
    elif user_city in ['quit', 'q', 'Q', 'Quit']:
        print("退出程序，以下是你的查询历史：")
        print(history_info)
        break

    else:
        print('你输入的值有误，请重新输入')
