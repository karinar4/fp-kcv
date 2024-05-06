from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    features = [x for x in request.form.values()]
    print('Features :', features)
    
    num_features = scaler.transform([[int(features[1]), float(features[5]), float(features[6]), float(features[7])]])
    print('Number features :', num_features)

    x = [[int(features[0]), num_features[0][0], int(features[2]), int(features[3]), int(features[4]), num_features[0][1], num_features[0][2], num_features[0][3]]]
    prediction = model.predict(x)
    print('Prediction :', prediction)

    if prediction:
        return render_template("result.html", prediction_text = "The prediction indicates that the person <strong>may have diabetes</strong>.")
    else:
        return render_template("result.html", prediction_text = "The prediction indicates that the person is <strong>not expected to have diabetes</strong>.".format(prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)