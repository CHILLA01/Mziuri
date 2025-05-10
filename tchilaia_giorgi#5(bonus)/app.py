from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'secret123'
app.permanent_session_lifetime = timedelta(minutes=5)


users = {
    'admin': 'admin123'
}


movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "description": "A dream within a dream.",
     "year": 2010},
    {"id": 2, "title": "The Matrix", "director": "Lana Wachowski", "description": "What is real?", "year": 1999}
]


@app.route('/')
def index():
    return render_template('index.html', movies=movies)


@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return render_template('movie.html', movie=movie)
    return "Movie not found", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session.permanent = True
            session['user'] = username
            return redirect(url_for('index'))
        return "Invalid credentials"
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_id = max([m['id'] for m in movies]) + 1 if movies else 1
        new_movie = {
            'id': new_id,
            'title': request.form['title'],
            'director': request.form['director'],
            'description': request.form['description'],
            'year': int(request.form['year'])
        }
        movies.append(new_movie)
        return redirect(url_for('index'))

    return render_template('add_movie.html')


if __name__ == '__main__':
    app.run(debug=True)
