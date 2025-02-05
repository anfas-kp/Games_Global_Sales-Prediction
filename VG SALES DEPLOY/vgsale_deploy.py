from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('vgsale_model.pkl', 'rb'))

# Load encoders
name_encoder = pickle.load(open('name_encoded.pkl', 'rb'))
platform_encoder = pickle.load(open('Platform_encoded.pkl', 'rb'))    
genre_encoder = pickle.load(open('Genre_encoded.pkl', 'rb'))    
publisher_encoder = pickle.load(open('Publisher_encoded.pkl', 'rb'))

# Load the feature list for reindexing
df = pd.read_csv("features_of_vgsale.csv")
columns_list = [col for col in df.columns if col != 'Unnamed: 0']

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST']) 
def predict():
    try:
        # Collect form data
        Rank = float(request.form['Rank'])
        Name = request.form['Name']
        Platform = request.form['Platform']
        Year = float(request.form['Year'])
        Genre = request.form['Genre']
        Publisher = request.form['Publisher']
        NA_Sales = float(request.form['NA_Sales'])
        EU_Sales = float(request.form['EU_Sales'])
        JP_Sales = float(request.form['JP_Sales'])
        Other_Sales = float(request.form['Other_Sales'])

        # Create DataFrame with column names
        new_data = pd.DataFrame([[Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales]],
                                columns=['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales'])

        # Apply encoding with error handling
        try:
            new_data['Name'] = name_encoder.transform(new_data['Name'])
        except ValueError:
            new_data['Name'] = -1  # Assign default value if unseen
        
        try:
            new_data['Platform'] = platform_encoder.transform(new_data['Platform'])
        except ValueError:
            new_data['Platform'] = -1
        
        try:
            new_data['Genre'] = genre_encoder.transform(new_data['Genre'])
        except ValueError:
            new_data['Genre'] = -1
        
        try:
            new_data['Publisher'] = publisher_encoder.transform(new_data['Publisher'])
        except ValueError:
            new_data['Publisher'] = -1

        # Reindex to match the original training features
        new_data = new_data.reindex(columns=columns_list, fill_value=0)

        # Make prediction
        prediction = model.predict(new_data)

        # Display the prediction
        prediction_text = f"PREDICTED GLOBAL SALES OF ' {Name.upper()} ' IS : $ {prediction[0]:.2f} million"

    except Exception as e:
        prediction_text = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
