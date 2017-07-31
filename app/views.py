from flask import render_template, url_for
from app import app, db 
from models import Score

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/leaderboard')
def leaderboard():
	leaderboard = Score.query.order_by(Score.points.desc())
	return render_template('leaderboard.html', leaderboard=leaderboard)







