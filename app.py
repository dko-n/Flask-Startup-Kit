'''
    name: app.py
    description: Application file.
    author: On Kato
'''

import sys
from datetime import timedelta
import flask
from flask import Flask, session, flash, render_template, abort, request, redirect, url_for
from jinja2 import TemplateNotFound
import sqlalchemy
from database import Database, URL
from config import configuration

from forms import SignInForms, SignUpForms

db = Database(URL)
db.setup()

app = Flask(__name__)

config = configuration(production=False)
app.config.update(config)

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
    form = SignInForms.SignInForm(request.form)
    if request.method == "GET":
        username = session["username"] if "username" in session else None
        try:
            return render_template('{}.html'.format(page), username=username, form=form)
        except TemplateNotFound:
            abort(404)

    elif request.method == "POST" and form.validate():
        name = request.form['name']
        password = request.form['password']
        
        try:
            is_user = db.session.query(db.model_class["User"]).filter(sqlalchemy.and_(db.model_class["User"].name == name, db.model_class["User"].password == password)).first()
        except sqlalchemy.exc.OperationalError as e:
            abort(500)            

        if is_user is None:
            flash("Invalid credentials")
            return redirect(url_for('signin'))

        session["username"] = name
        return redirect(url_for('index'))

    else:
        flash("Invalid Inputs")
        return redirect(url_for('signin'))

@app.route('/signup', methods=["GET", "POST"], defaults={'page': 'signup'})
def signup(page):
    form = SignUpForms.SignUpForm(request.form)
    if request.method == "GET":
        try:
            username = session["username"] if "username" in session else None
            return render_template('{}.html'.format(page), username=username, form=form)
        except TemplateNotFound:
            abort(404)

    elif request.method == "POST" and form.validate():
        name = request.form['name']
        password = request.form['password']

        try:
            is_user = db.session.query(db.model_class["User"]).filter(sqlalchemy.and_(db.model_class["User"].name == name, db.model_class["User"].password == password)).first()
        except sqlalchemy.exc.OperationalError as e:
            abort(500)

        if is_user is None:
            user = db.model_class["User"](name, password)
            db.session.add_all([user])
            db.session.commit()
            session["username"] = name
            return redirect(url_for('index'))

        flash("User name already exists")
        return redirect(url_for('signup'))

    else:
        flash("Invalid Inputs")
        return redirect(url_for('signup'))        

@app.route('/signout', methods=["GET"])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

# 共通エラーページ
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html', code=404, message="Page Not Found", error_message="お探しのページは存在しません。")

# 共通エラーページ
@app.errorhandler(500)
def server_error(e):
    return render_template('error/500.html', code=500, message="Internal Server Error", error_message="エラーが発生しました。")

if __name__ == "__main__":
    app.run()