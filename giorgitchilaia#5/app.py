from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'my_secret_key'


users = {}


tasks = ["Buy groceries", "Complete homework", "Go for a walk"]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks, username=session.get('username'))

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'username' not in session:
        flash("გთხოვთ გაიაროთ ავტორიზაცია თასქის დასამატებლად", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('home'))
    return render_template('add_task.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('მომხმარებელი უკვე არსებობს!', 'danger')
            return redirect(url_for('register'))

        users[username] = generate_password_hash(password)
        session['username'] = username
        flash('წარმატებით გაიარეთ რეგისტრაცია!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash('წარმატებით შეხვედი!', 'success')
            return redirect(url_for('home'))
        else:
            flash('არასწორი მონაცემები', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('თქვენ გამოხვედით სისტემიდან.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

