''' Contains all routes and backend logic in the web application '''

from flask import request, url_for, redirect, render_template, flash, g, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from app.constants import *
from app.forms import *
from app.models import *
from app.utils import *
from app.puzzle import Puzzle
import json

@app.route('/')
def index():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('home'))
	return redirect(url_for('register'))

@app.route('/rules')
def rules():
	return render_template('rules.html', title='Rules')


# === User login methods ===

@app.before_request
def before_request():
	g.user = current_user

@lm.user_loader
def load_user(id):
	return User.query.get(id)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(id=form.id.data.upper().strip()).first()
		if user is not None and user.check_password(form.password.data):
			login_user(user)
			return redirect(url_for('home'))
		else:
			flash('Invalid username or password.')
	return render_template('login.html', title='Login', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User.query.filter_by(id=form.id.data).first()
		if user:
			flash('ID already taken!')
			return render_template('register.html', title='Register', form=form)
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			flash('Username already taken!')
			return render_template('register.html', title='Register', form=form)
		email = generate_email(form.id.data.upper().strip())	
		user = User(id=form.id.data, email=email, username=form.username.data, language=form.language.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/logout/')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

# ========================

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
	if request.method == 'GET':
		user = User.query.filter_by(id=g.user.id).first()
		if user.completed:
			return redirect(url_for('game_over'))
		return render_template(
			'home.html',
			title='Home',
			lang=user.language,
			game_mode=GAME_MODE.value,
			total_puzzles=MAX_PUZZLES,
			duration=GAME_DURATION
		)
	
	if request.method == 'POST':
		user_info = User.query.filter_by(id=g.user.id).first()
		puzzles = Puzzle.get_puzzles(user_info.language)
		session['puzzles'] = [puzzle.__dict__ for puzzle in puzzles]
		session['index'] = 0
		return redirect(url_for('play'))

@app.route('/play', methods=['GET', 'POST'])
@login_required
def play():
	if request.method == 'GET':
		user = User.query.filter_by(id=g.user.id).first()
		if user.completed:
			return redirect(url_for('game_over'))
		
		index = session['index']
		# Check for both: All puzzles completed OR Entire Puzzle set completed in given time
		if (index >= MAX_PUZZLES):
			user = User.query.filter_by(id=g.user.id).first()
			user.completed = True
			user.puzzles_solved = session['index']
			user.time_taken = session['time_taken']
			db.session.commit()
			return redirect(url_for('game_over'))
		
		return render_template(
			'play.html',
			puzzle=session['puzzles'][index],
			index=index,
			total=MAX_PUZZLES,
			game_duration=GAME_DURATION,
			game_mode=GAME_MODE.value
		)
	
	if request.method == 'POST':
		index = session['index']
		puzzle = session['puzzles'][index]
		lang = puzzle['lang']
		puzzle_name = puzzle['puzzle_name']
		solution = json.loads(request.form['codeArray'])
		session['time_taken'] = request.form['timeTaken']
		solved = Puzzle.check_puzzle(lang, puzzle_name, solution)
		if solved:
			session['index'] += 1
		else:
			flash("Try Again! Demogorgans are getting closer!")
		return redirect(url_for('play'))
	
@app.route('/set-game-over', methods=['GET', 'POST'])
def set_game_over():
	''' Used for setting game as over if time limit exceeds '''
	if request.method == 'POST':
		time_out = request.form.get('timeOut')
		print("Time out:", time_out)
		if (GAME_MODE == GameMode.SOLVE_MAXIMUM_PUZZLES and time_out):
			user = User.query.filter_by(id=g.user.id).first()
			user.completed = True
			user.puzzles_solved = session['index']
			user.time_taken = f"{GAME_DURATION//60}:{GAME_DURATION%60}"
			db.session.commit()
			return redirect(url_for('game_over'))
		return redirect(url_for('play'))

@app.route('/game-over')
@login_required
def game_over():
	user = User.query.filter_by(id=g.user.id).first()
	time_taken = user.time_taken
	n_puzzles = user.puzzles_solved

	if GAME_MODE == GameMode.MINIMUM_TIME_TAKEN:
		score = time_taken
		winners = User.query.filter(
			User.time_taken.isnot(None)
		).order_by(User.time_taken, User.created_at).limit(3).all()

	elif GAME_MODE == GameMode.SOLVE_MAXIMUM_PUZZLES:
		score = n_puzzles
		winners = User.query.filter(
			User.puzzles_solved.isnot(None)
		).order_by(User.puzzles_solved, User.created_at).limit(3).all()

	players_count = User.query.count()

	return render_template(
		'gameover.html',
		time_taken=time_taken,
		n_puzzles=n_puzzles,
		user=user.__dict__,
		score=score, 
		winners=winners,
		game_mode=GAME_MODE.value,
		players_count=players_count
	)

@app.route('/test')
def test():
	return render_template('test.html')
# ====================