import os
from flask import Flask, request, redirect, flash, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'
<<<<<<< HEAD

@app.route('/hello')
def hello2():
    return 'Hello from the other side'

@app.route('/view')
def view():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

=======
#hi
>>>>>>> 3205c6b6636df386872d179d707b8c628da9b584
