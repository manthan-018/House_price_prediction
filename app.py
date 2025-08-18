from flask import Flask, request, render_template

import pickle

regressor_model = pickle.load(open('regressor_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/',methods =['GET','POST'])

def sales_view():
    if request.method == 'GET':
        return render_template("first.html")
    elif request.method == 'POST':
        s = float(request.form["Size_sqft"])
        b = float(request.form["Bedrooms"])
        a= float(request.form["Age_years"])
        op_array = regressor_model.predict([[s,b,a]])
        y_pred = round(op_array[0], 2)
        return render_template("output.html", predicted_house_price = y_pred )

if __name__ == '__main__':
    app.run(debug=True)
