from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime', methods=['GET'])
def current_datetime():
    datetime_now = datetime.now()
    date_return = dict()
    date_return['current_datetime'] = f'{datetime_now.strftime("%d/%m/%Y %H:%M:%S %p")}'
    if datetime_now.hour < 12:
        date_return['message'] = 'Bom dia!'
    if datetime_now.hour >= 12 and datetime_now.hour < 18:
        date_return['message'] = 'Boa tarde!'
    if datetime_now.hour > 18:
        date_return['message'] = 'Boa noite!'
    return date_return