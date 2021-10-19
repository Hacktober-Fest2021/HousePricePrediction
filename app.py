from flask import Flask, render_template, request
from joblib import load
import numpy as np
import pandas as pd

app = Flask(__name__)

#load model
model = load('model')

@app.route('/', methods = ['POST','GET'])
def home():
    price = 0
    error = ''

    if request.method == 'POST':
        try:
            X = pd.DataFrame(np.array([[
                float(request.form['avg area income']),
                float(request.form['avg area house age']),
                float(request.form['avg area number of rooms']),
                float(request.form['avg area number of bedrooms']),
                float(request.form['area population']),
            ]]))

            X.columns = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']

            price = model.predict(X)[0]
            error = "Suggested Houses"

            return render_template('home.html', price = price, error = error)
        
        except:
            error = 'Error Occured'
            return render_template('home.html', price = price, error = error)

            
    return render_template('home.html', price = price, error = error)

if __name__ == '__main__':
    app.run(debug=True)