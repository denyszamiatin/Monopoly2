from flask import Flask, render_template, request
from player import CollectionPlayers

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def add_amount_players():
    if request.method == 'POST':
        CollectionPlayers.amount_players = request.form['amount_players']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)