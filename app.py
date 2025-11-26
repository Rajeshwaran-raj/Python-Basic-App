import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# =====================================
# In-Memory SQLite Database
# =====================================
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # RAM only
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =====================================
# Database Model
# =====================================
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# =====================================
# Seed Default Data
# =====================================
def seed_default_data():
    if User.query.count() == 0:
        default_users = [
            User(name="Rajesh", age=23),
            User(name="Priya", age=27),
            User(name="Kumar", age=30),
            User(name="Meena", age=22),
            User(name="Vijay", age=29)
        ]
        db.session.bulk_save_objects(default_users)
        db.session.commit()

with app.app_context():
    db.create_all()
    seed_default_data()


# =====================================
# Routes
# =====================================
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

# =====================================
# Run App
# =====================================
if __name__ == '__main__':
    app.run(debug=True)
