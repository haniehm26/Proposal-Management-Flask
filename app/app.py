from flask import Flask, redirect, render_template
from forms import LoginForm
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'f8a184aad925228fe58bf94ceea9f20f'
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/proposal-management'}

initialize_db(app)


@app.route('/')
def hello():
    return "Home Page"


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template('login.html', form=form)


initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
