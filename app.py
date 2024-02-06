# from flask import Flask, request, jsonify
# from flask_cors import CORS 
# import requests
# import json

# app = Flask(__name__)

# # Use Flask-CORS with default options
# CORS(app)

# # Replace with your Google Apps Script web app URL
# GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwT_caEFY2AZJHpyzviLNm0KJVEGtK35qA7fVWecXq9hslWj-fDwTcGMYfG0vfICyF3/exec"

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json  # Assuming the incoming data is in JSON format
    
#     # Extracting totalAmount from incoming data
#     totalAmount = data.get("totalAmount", 0)
    
#     # Fetching data from chargily API
#     myHeaders = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer test_sk_nu2KF22Dc60fD6LdkIoAwlp3WgfCj5rqn15atqeB"
#     }
#     raw = json.dumps({
#         "amount": totalAmount,
#         "payment_method": "edahabia",
#         "currency": "dzd",
#         "success_url": "https://hookfastfood22.onrender.com/payments/success"
#     })

#     requestOptions = {
#         "method": "POST",
#         "headers": myHeaders,
#         "body": raw,
#         "redirect": "follow"
#     }

#     # Sending request to chargily API
#     response = requests.post("https://pay.chargily.net/test/api/v2/checkouts", json=raw, headers=myHeaders)
#     chargily_data = response.json()

#     if response.status_code == 200:
#         checkout_id = chargily_data.get("id")
#         checkout_url = chargily_data.get("checkout_url")

#         # Adding checkout_id and checkout_url to the incoming data
#         data["checkout_id"] = checkout_id
#         data["checkout_url"] = checkout_url

#         # Send the combined data to Google Apps Script
#         google_script_response = requests.post(GOOGLE_SCRIPT_URL, json=data)

#         # Handle the response from the Google Apps Script if needed
#         if google_script_response.status_code == 200:
#             return "Data sent to Google Apps Script successfully"
#         else:
#             return "Failed to send data to Google Apps Script"
#     else:
#         return "Failed to fetch data from chargily API"

# @app.route('/payments/success', methods=['GET'])
# def payment_success():
#     # Add your logic for handling successful payments here
#     return jsonify({"message": "Payment Successful!"})
    
# if __name__ == '__main__':
#     app.run(debug=True)







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


