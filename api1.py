import pickle
#import numpy as np
from flask import Flask, request, jsonify
#model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
# Load the model
#model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def result():
    #data = request.get_json(force=True)
    model = pickle.load(open('model.pkl','rb'))
    #my_model = print(model)
    return model
if __name__ == '__main__':
    app.run(port=5000, debug=True)