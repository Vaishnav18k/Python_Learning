from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # You can send this data to FastAPI backend
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Signup: {username}, {email}, {password}")
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This will be sent to FastAPI later
        email = request.form['email']
        password = request.form['password']
        print(f"Login: {email}, {password}")
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
