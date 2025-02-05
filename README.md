# Video Game Global Sales Prediction

This project predicts global sales for video games using machine learning techniques. The application is deployed via a Flask web interface, allowing users to input game details and receive sales predictions.

## Project Structure

```
Games_Global_Sales-Prediction-main/
└── VG SALES DEPLOY/
    |
    |── vgsale_deploy.py            # Flask application for deployment
    |── vgsale.ipynb                 # Jupyter notebook for data analysis and model training
    |── vgsale_model.pkl             # Trained machine learning model
    |── vgsales.csv                  # Dataset containing video game sales data
    |── features_of_vgsale.csv       # Features used in the model
    |── Genre_encoded.pkl            # Encoded genre features
    |── Platform_encoded.pkl         # Encoded platform features
    |── Publisher_encoded.pkl        # Encoded publisher features
    |── name_encoded.pkl             # Encoded game name features
    |── requirements.txt             # Required Python packages
    |── templates/                   # HTML templates for the web app
    |── static/                      # Static files (CSS, JS, images)
```

## Getting Started

### Prerequisites
Ensure you have Python installed. Install the required packages using:

```bash
pip install -r requirements.txt
```

### Running the Application

1. Navigate to the project directory:

```bash
cd 'VG SALES DEPLOY'
```

2. Run the Flask application:

```bash
python vgsale_deploy.py
```

3. Open your browser and go to `http://127.0.0.1:5000/` to access the web interface.

## Features
- Predicts global sales based on input features such as genre, platform, publisher, and game name.
- Simple and intuitive web interface for easy predictions.

## Files Explained
- **vgsale.ipynb**: Contains data preprocessing, exploratory data analysis, and model training steps.
- **vgsale_model.pkl**: The saved machine learning model used for making predictions.
- **vgsale_deploy.py**: Flask script to deploy the model as a web application.
- **requirements.txt**: Lists all Python libraries required to run the project.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or issues, please contact [ANFAS KP] at [anfasanu178@gmail.com].

