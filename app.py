import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv() 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

load_dotenv()  # Load environment variables from .env

# Read variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# URL-encode password
DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)

# ==============================
# Database Configuration
# ==============================

#postgres
#app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD_ENCODED}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

#sql
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD_ENCODED}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==============================
# Database Model
# ==============================
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Create tables if not exist
with app.app_context():
    db.create_all()

# ==============================
# Routes
# ==============================
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user_route():
    name = request.form['name']
    age = request.form['age']
    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user_route(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.age = request.form['age']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:id>', methods=['GET'])
def delete_user_route(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

# ==============================
# Run App
# ==============================
if __name__ == '__main__':
    app.run(debug=True)
