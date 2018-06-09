from flask import Flask, render_template, url_for, request
app = Flask(__name__)
from src.utils import Utils
import json
# from src.position import Positioner


data = open('../data/data.json', 'r')
data = json.load(data)
utils = Utils()


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/participants', methods=['GET', 'POST'])
def get_participants():
    print("/participants")
    # TODO: /participantsへのpostの参加人数を受け取って、jsonに入れる
    num_p = 3
    data[0]["participant"] = str(num_p)
    print(data)

    # TODO: num_pの値から、プレイヤーの役職を決める
    utils.decide_positions(num_p)
    return render_template('play_position.html', num_p=num_p)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=80)
    # app.run(host='0.0.0.0', port=5000)
