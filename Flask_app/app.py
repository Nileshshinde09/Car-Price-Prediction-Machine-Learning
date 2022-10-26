from distutils.log import error
from flask import Flask,render_template,request
from logging import exception
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load("model.joblib")
@app.route('/',methods = ['GET', 'POST'])
def index_page():
    try:
            if request.method == 'POST':
                year = request.form.get('year')
                Present_Price = request.form.get("Present_Price")
                KMs = request.form.get("KMs")
                fuel_type = request.form.get("fuel_type")
                seller_type = request.form.get("seller_type")
                transmission = request.form.get("transmission")
                owner_type = request.form.get("owner_type")
                input_data = [year,Present_Price,KMs,fuel_type,seller_type,transmission,owner_type]
                input_data= np.array(input_data)
                predict =model.predict([input_data])
                return render_template("index.html",data =str(predict[0]))
    except exception:
        pass
    except error:
        pass
        


if __name__=="__main__":
    app.run(debug=True)
