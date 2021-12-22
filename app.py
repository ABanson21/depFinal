import numpy as np
from werkzeug.wrappers import Request, Response
from PIL import Image
from flask import Flask, request, jsonify, render_template
import pickle
import io
import base64

app = Flask(__name__, template_folder='templates')
model = pickle.load(open('model.pkl', 'rb'))
data = io.BytesIO()
text = ""

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dtPredict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    if output == 1: 
        text = " not survive"
    else:
        text= "survive"
    
    return render_template("index.html", prediction_text='Based on the SVM model you most likely would {}'.format(text))


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, app)
