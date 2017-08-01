from flask import render_template, url_for, request, abort, redirect, jsonify
from app import app, db 
from .models import Score
import json

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/leaderboard')
def leaderboard():
	leaderboard = Score.query.order_by(Score.points.desc())
	return render_template('leaderboard.html', leaderboard=leaderboard)



@app.route('/submit', methods=["POST"])
def submitScore():
	data = json.loads(request.data)
	new_score = Score(data['name'], data['score'])

	db.session.add(new_score)
	db.session.commit()

	return jsonify(data), 200



