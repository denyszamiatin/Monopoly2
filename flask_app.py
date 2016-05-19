from flask import Flask, render_template, request
from player import CollectionPlayers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def add_amount_players():
    if request.method == 'POST':
        try:
            player_quantity = int(request.form['amount_players'])
            if not 2 < player_quantity < 6:
                raise ValueError
        except ValueError:
            return render_template('index.html')
        CollectionPlayers.amount_players = request.form['amount_players']
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)