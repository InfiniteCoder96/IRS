from flask import Flask,request,jsonify
from flask_cors import CORS

from ques import QA

app = Flask(__name__)
CORS(app)

model = QA()

@app.route("/",methods=['GET'])
def test():
    return "Application deployed"
    

@app.route("/predict",methods=['POST'])
def predict():
    q = request.json["question"]
    try:
        out = model.qa_func(q)
        return jsonify({"result":out})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run('0.0.0.0')