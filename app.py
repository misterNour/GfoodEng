
from flask import Flask, request, jsonify
from flask_cors import CORS 
import requests

app = Flask(__name__)

# Use Flask-CORS with default options
CORS(app)

# Replace with your Google Apps Script web app URL
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwT_caEFY2AZJHpyzviLNm0KJVEGtK35qA7fVWecXq9hslWj-fDwTcGMYfG0vfICyF3/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Assuming the incoming data is in JSON format
    
    # Send the data to Google Apps Script
    response = requests.post(GOOGLE_SCRIPT_URL, json=data)
    
    # Handle the response from the Google Apps Script if needed
    if response.status_code == 200:
        return "Data sent to Google Apps Script successfully"
    else:
        return "Failed to send data to Google Apps Script"

@app.route('/payments/success', methods=['GET'])
def payment_success():
    # Add your logic for handling successful payments here
    return jsonify({"message": "Payment Successful!"})
    
if __name__ == '__main__':
    app.run(debug=True)


