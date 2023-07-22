# app.py

from flask import Flask, render_template
from get_train_data import get_details

app = Flask(__name__)

@app.route('/')
def display_train_information():
    trains = get_details()
    return render_template('index.html', trains=trains)

if __name__ == '__main__':
    app.run(debug=True)
