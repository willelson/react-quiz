from flask import render_template, url_for
from app import app

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/leaderboard')
def leaderboard():
	return render_template('leaderboard.html')







