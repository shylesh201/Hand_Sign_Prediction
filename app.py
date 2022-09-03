from flask import Flask, render_template, request
import pickle
import numpy as np
from tensorflow import keras



app = Flask(__name__)





@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    model = pickle.load(open('model.pkl', 'rb'))
   
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















