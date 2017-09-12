# -*-coding:utf-8-*-
from flask import Flask, request, render_template
from weather import show_weather

app = Flask(__name__)
history_info = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user_request')
def weather():
    while True:
        location = request.args.get('city')
        if request.args.get('help') == '帮助':
            return render_template('help.html')
        elif request.args.get('history') == '历史':
            return render_template('history.html', history_info = history_info)
        elif request.args.get('query') == '查询':
            try:
                history_data = show_weather(location)
                history_info.append(history_data)
                return render_template('result.html', history_data = history_data)
            except:
                return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
