from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    with open('gaming_products.pkl', 'rb') as f:
        soup_obj = pickle.load(f)
    return soup_obj

if __name__ == '__main__':
    app.run(debug=True)