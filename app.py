from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the phishing model
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input from the form
        features = request.form['features']
        
        # Create a list with the feature for prediction
        X_predict = [features]
        
        try:
            # Make prediction
            y_Predict = phish_model_ls.predict(X_predict)
            
            # Determine the result
            if y_Predict[0] == 'bad':
                result = "This is a Phishing Site"
                color = "red"
            else:
                result = "This is NOT a Phishing Site"
                color = "green"
            
            return render_template('index.html', prediction=result, color=color)
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {e}", color="orange")

if __name__ == '__main__':
    app.run(debug=True)
