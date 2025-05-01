from idk import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Home Page</h1>"


@app.route('/about')
def about():
    return '<p>This is about us page</p>'


@app.route('/<name>/<int:age>/')
def profile(name, age):
    return render_template("user.html", user_name=name, user_age=age)


@app.route('/admin')
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

    < script
    src = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
    integrity = "sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin = "anonymous" > < / script >

    < button
    type = "submit"


    class ="btn btn-primary" > Submit < / button >