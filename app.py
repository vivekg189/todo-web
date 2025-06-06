from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
