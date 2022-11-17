from flask import Flask, render_template, request



import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "hdsXmmNhU2-d2w8TwwX-bnexosADc1_iUaR-04mPZU-q"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age']) 
    gender = float(request.form['gender'])
    tb = float(request.form['tb']) 
    db = float(request.form['db'])
    ap = float(request.form['ap'])
    aa1 = float(request.form['aa1'])
    aa2 = float(request.form['aa2'])
    tp = float(request.form['tp'])
    al = float(request.form['al'])
    agr = float(request.form['agr'])

    # converting data into float
    X = [[age,gender,tb,db,ap,aa1,aa2,tp,al,agr]]

    payload_scoring = {"input_data": [{"field": [['age','gender','tb','db','ap','aa1','aa2','tp','al','agr']], "values": X }]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7623d868-2b10-4b95-9354-0d13c356f5ab/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    print(response_scoring)
    predictions = response_scoring.json()
    predict = predictions['predictions'][0]['values'][0][0]
    print(f"Final prediction : {predict}")
    # prediction = model.predict(data)[0]

    return render_template('result.html',result = predict)

if __name__ == '__main__':
    app.run(debug=True)


# SVC from version 1.0.2 when using version 1.1.3.


# 2 - have disease      - 1
# 1 - Not have disease  - 0