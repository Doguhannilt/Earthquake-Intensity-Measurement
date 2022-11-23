from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    enlem = float(request.form["Enlem"])
    boylam = float(request.form["Boylam"])
    derinlik = float(request.form["Derinlik"])
    xm = float(request.form["Xm"])
    ms = float(request.form["Ms"])
    mb = float(request.form["Mb"])
    yil = int(request.form["Yil"])
    ay = int(request.form["Ay"])
    gun = int(request.form["Gun"])
    prediction = model.predict([[enlem,boylam, derinlik, xm, ms, mb, yil, ay,gun]])
    return render_template('index.html' , prediction = prediction)

  

if __name__ == "__main__":
    app.run()

