import datetime

from flask import Flask, request, render_template

from database import Database
from game import Game

app = Flask(__name__)
db = Database()
db.create_tables()
current_game = Game()


@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        username = request.form['username']
        if request.form['username'] != '':
            return render_template('user.html', name=username)
        else:
            return render_template('start.html', error="Geef een geldige naam in")
    else:
        return render_template('start.html')


@app.route('/leaderboard/<username>', methods=['POST'])
def leaderboard(username):
    if request.method == 'POST':
        db = Database()
        user = db.get_user(username)
        if user is None:
            return render_template('usernotfound.html', name=username)
        result = db.get_scores(username)
        scores = []
        for row in result:
            scores.append(
                {'date': datetime.datetime.strptime(row[0], '%Y-%m-%d').strftime('%d-%m-%Y'), 'guesses': row[1], 'godmode': row[2]})
        return render_template('leaderboard.html', name=user[0], scores=scores, times_played=len(scores))


@app.route('/startgame/', methods=['GET', 'POST'])
def start():
    amount_of_boxes = request.form['amount_of_boxes']
    amount_of_colors = request.form['amount_of_colors']
    multiple_colors = request.form['multiple_colors']
    godmode = request.form['toggle_godmode']
    username = request.form['username']
    current_game.setColorAmount(int(amount_of_colors))
    current_game.setBoxAmount(int(amount_of_boxes))
    current_game.createCode(multiple_colors)
    current_game.setGodmode(godmode)
    code = current_game.getCode()
    if request.method == 'POST':
        if amount_of_boxes == '4':
            return render_template('gamefour.html', guesses=current_game.getGuesses(),
                                   name=username, colors=current_game.getColors(), code=code,
                                   godmode=current_game.godmode)
        else:
            return render_template('gamesix.html', guesses=current_game.getGuesses(),
                                   name=username, colors=current_game.getColors(), code=code,
                                   godmode=current_game.godmode)
    else:
        return render_template('start.html')


@app.route('/guess/', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        if current_game.getBoxAmount() == 4:
            guessed = [request.form['first'], request.form['second'], request.form['third'], request.form['fourth']]
        else:
            guessed = [request.form['first'], request.form['second'], request.form['third'], request.form['fourth'],
                       request.form['fifth'], request.form['sixth']]
        username = request.form['username']
        check = current_game.addGuess(guessed)
        code = current_game.getCode()
        if check[0] == current_game.getBoxAmount():
            guesses = current_game.getTimesGuessed()
            db = Database()
            now = datetime.datetime.today().date()
            if current_game.godmode:
                godmode = 1
            else:
                godmode = 0
            db.save_user(request.form['username'], now, guesses, godmode)
            return render_template('winner.html', code=code, username=username, guesses=guesses)
        if current_game.getTimesGuessed() == 10:
            return render_template('loser.html', code=code, username=username)
        else:
            checklist = current_game.addCheck(check[0], check[1])
            if current_game.getBoxAmount() == 4:
                return render_template('gamefour.html', guesses=current_game.getGuesses(),
                                       name=username, colors=current_game.getColors(), checklist=checklist, code=code,
                                       godmode=current_game.godmode)
            else:
                return render_template('gamesix.html', guesses=current_game.getGuesses(),
                                       name=username, colors=current_game.getColors(), checklist=checklist, code=code,
                                       godmode=current_game.godmode)
