import sys
import flask
from flask import Flask, session, flash, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
import sqlalchemy
from database import Database, URL

db = Database(URL)
db.setup()

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/', defaults={'page': 'index'})
def index(page):
    username = session["username"] if "username" in session else None

    try:
        test_recode = db.session.query(db.model_class["Test"]).filter(db.model_class["Test"].id == "1").first()
        user_recode = db.session.query(db.model_class["User"]).filter(db.model_class["User"].name == "Panda").first()
    except sqlalchemy.exc.OperationalError:
        test_recode = None
        user_recode = None

    try:
        return render_template('{}.html'.format(page), 
                python_ver=sys.version, 
                flask_ver=flask.__version__, 
                sql_alchemy_ver=db.sqlalchemy_ver, 
                database_info=test_recode,
                user_info=user_recode,
                username = username
            )
    except TemplateNotFound:
        abort(404)

@app.route('/about', defaults={'page': 'about'})
def about(page):
    username = session["username"] if "username" in session else None
    try:
        return render_template('{}.html'.format(page), username=username)
    except TemplateNotFound:
        abort(404)

@app.route('/signin', methods=["GET", "POST"], defaults={'page': 'signin'})
def signin(page):
    if request.method == "GET":
        username = session["username"] if "username" in session else None
        try:
            return render_template('{}.html'.format(page), username=username)
        except TemplateNotFound:
            abort(404)

    elif request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        is_user = db.session.query(db.model_class["User"]).filter(sqlalchemy.and_(db.model_class["User"].name == name, db.model_class["User"].password == password)).first()

        if is_user is None:
            flash("Invalid credentials")
            return redirect(url_for('signin'))

        session["username"] = name
        return redirect(url_for('index'))

@app.route('/signup', methods=["GET", "POST"], defaults={'page': 'signup'})
def signup(page):
    if request.method == "GET":
        try:
            username = session["username"] if "username" in session else None
            return render_template('{}.html'.format(page), username=username)
        except TemplateNotFound:
            abort(404)

    elif request.method == "POST":
        name = request.form['name']
        password = request.form['password']
        is_user = db.session.query(db.model_class["User"]).filter(sqlalchemy.and_(db.model_class["User"].name == name, db.model_class["User"].password == password)).first()

        if is_user is None:
            user = db.model_class["User"](name, password)
            db.session.add_all([user])
            db.session.commit()
            session["username"] = name
            return redirect(url_for('index'))

        flash("User name already exists")
        return redirect(url_for('signup'))      

@app.route('/signout', methods=["GET"])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5001)
