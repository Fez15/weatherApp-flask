import requests
from flask import Flask, render_template, request
#import flask_monitoringdashboard as dashboard

app = Flask(__name__)

#dashboard.bind(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
    else:
        city = 'Melbourne'

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=718c1bc1f10f39fa695cfdc69b08e3f8'

    r = requests.get(url.format(city)).json()

    weather = {
        'city' : r['name'],
        'country' : r['sys']['country'],
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon']
    }

    return render_template('weather.html', weather=weather)

# run app
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)
