from flask import Flask, render_template,request
import numpy as np

import pickle

app=Flask(__name__)

#with open('../models/lr_model_v1.pkl', 'rb') as model_file:
#model_file=open('../models/lr_model.pkl', 'rb')

#model = pickle.load(model_file)

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict():
    kms=float(request.form.get("kms"))
    price=float(request.form.get("original_price"))
    car_age=float(request.form.get("car_age"))
    fuel=request.form.get("fuel_type")
    transmission=request.form.get("transmission_type")
    """final_features = [np.array([km,car_age])]
    car_price = model.predict(final_features)

    output = round(car_price[0], 2)

    return render_template('index.html', prediction_text='Car price should be  {}'.format(output))
    """
    return render_template('home.html',prediction_text='Fuel  '+fuel)


if __name__=='__main__':
    app.run(debug=True)