from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved model
model = joblib.load('model.pkl')

# Feature names based on your model: ['City', 'Product', 'Unit Price', 'Quantity']
# We'll need to map these to meaningful labels

@app.route('/')
def home():
    return render_template('html.html')  # Fix: use correct template filename

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        city = request.form['city']
        product = request.form['product']
        unit_price = float(request.form['unit_price'])
        quantity = float(request.form['quantity'])
        
        # Convert city and product to numerical values (same encoding as in your notebook)
        # This should match the encoding you used during training
        city_mapping = {'Riyadh': 7, 'Abha': 0, 'Tabuk': 8, 'Hail': 3, 
                       'Mecca': 5, 'Medina': 6, 'Dammam': 1, 'Jeddah': 4, 
                       'Buraidah': 2, 'Khobar': 9}
        product_mapping = {'Colombian': 1, 'Costa Rica': 2, 'Ethiopian': 3, 
                          'Brazilian': 0, 'Guatemalan': 4}
        
        city_encoded = city_mapping.get(city, 0)
        product_encoded = product_mapping.get(product, 0)
        
        # Create feature array in the same order as training
        features = np.array([[city_encoded, product_encoded, unit_price, quantity]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        return render_template('html.html',  # Fix: use correct template filename
                             prediction_text=f'Predicted Final Sales: SAR {prediction:.2f}',
                             city=city,
                             product=product,
                             unit_price=unit_price,
                             quantity=quantity)
    
    except ValueError:
        return render_template('html.html',  # Fix: use correct template filename
                             prediction_text="Please enter valid numbers for Unit Price and Quantity.")

if __name__ == "__main__":
    app.run(debug=True)