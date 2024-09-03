from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkeyyoucanmakeitwhateveryouwant'

# Initialize database
def init_db():
    conn = sqlite3.connect('basic_flask.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        age INTEGER NOT NULL
    )''')
    conn.commit()
    conn.close()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        conn = sqlite3.connect('basic_flask.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password, age) VALUES (?, ?, ?)', (username, password, age))
            conn.commit()
            flash('User registered successfully!', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already taken, try another one.', 'danger')
        finally:
            conn.close()
    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('basic_flask.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session['user'] = user[1]
            session['age'] = user[3]
            return redirect(url_for('welcome'))
        else:
            flash('Login failed. Check your username and password.', 'danger')
    return render_template('login.html')

# Welcome Page (After Login)
@app.route('/welcome')
def welcome():
    if 'user' in session:
        user = session['user']
        age = session['age']
        return render_template('welcome.html', user=user, age=age)
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('age', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)


# Calculator page route

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operator = request.form['operator']
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero is undefined"
        else:
            result = "Invalid operator"
    return render_template('calculator.html', result=result)



