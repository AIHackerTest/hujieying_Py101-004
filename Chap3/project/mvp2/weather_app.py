# -*-coding:utf-8-*-
from flask import Flask,render_template,flash
from flask_wtf import FlaskForm #导入FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from weather import show_weather

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
history_info = []

class WeatherForm(FlaskForm): #继承FlaskForm表单
    city = StringField('请输入城市进行查询：', validators=[DataRequired()])
    query = SubmitField('查询')
    history = SubmitField('历史')
    help_info = SubmitField('帮助')

@app.route('/',methods=['GET','POST'])
def index():
    form = WeatherForm()
    while True:
        if form.help_info.data:
            return render_template('index.html', form=form)
        elif form.history.data:
            return render_template('index.html', form=form, history_info=history_info)
        elif form.query.data:
            location = form.city.data
            try:
                history_data = show_weather(location)
                history_info.append(history_data)
                return render_template('index.html', form=form, history_data=history_data)
            except:
                flash('你的输入有误，请重新输入')
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
