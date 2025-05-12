from datetime import timedelta
from flask import (Flask, render_template, request,
                   redirect, url_for, session)
app = Flask(__name__)
app.secret_key = "verysecretkey"

app.permanent_session_lifetime = timedelta(hours=10)

book_list = [
    {"book_id": 1, "title": "ვეფხისტყაოსანი", "author": "შოთა რუსთაველი", "release_date": "1200"},
    {"book_id": 2, "title": "Harry Potter I", "author": "J.K.Rowling", "release_date": "1997"},
    {"book_id": 3, "title": "Idiot", "author": "Dostoevsky", "release_date": "1869"}
]

@app.route("/")
def home():
    return render_template("index.html", books=book_list)

@app.route("/profile")
def profile():
    if 'user' in session:
        username = session['user']
        return render_template("profile.html", user=username)
    else:
        return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for("profile"))
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        if len(book_list) > 0:
            last_id = book_list[-1]["book_id"]
            new_id = last_id + 1
        else:
            new_id = 1



        title = request.form["title"]
        author = request.form["author"]
        release_date = request.form["release_date"]



        new_book = {
            "book_id": new_id,
            "title": title,
            "author": author,
            "release_date": release_date
        }

        book_list.append(new_book)
        return redirect(url_for("home"))
    return render_template("add_book.html")


if __name__ == "__main__":
    app.run(debug=True)