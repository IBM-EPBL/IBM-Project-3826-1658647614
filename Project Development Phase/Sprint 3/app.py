from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age'] 
    gender = request.form['gender']
    tb = request.form['tb'] 
    db = request.form['db']
    ap = request.form['ap']
    aa1 = request.form['aa1']
    aa2 = request.form['aa2']
    tp = request.form['tp']
    al = request.form['al']
    agr = request.form['agr']

    # converting data into float
    data = [[float(age),float(tb),float(db),float(ap),float(aa1),float(aa2),float(tp),float(al),float(agr),float(gender)]]

    # Loading the model
    # using pickle
    model = pickle.load(open('liver.pkl','rb'))

    prediction = model.predict(data)[0]

    # if prediction == 1:
    #     return f"You have liver disease Result : {prediction}"
    # else:
    #     return f"You are healthy Result : {prediction}"
    return render_template('result.html',result = prediction)

if __name__ == '__main__':
    app.run(debug=True)


# SVC from version 1.0.2 when using version 1.1.3.


# 2 - have disease      - 1
# 1 - Not have disease  - 0