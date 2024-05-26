import requests
import json

# WhatsApp API endpoint and access token
api_url = "https://graph.facebook.com/v15.0/<phone_number_id>/messages"
access_token = "YOUR_ACCESS_TOKEN"

# Header for the HTTP request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# List of phone numbers to send the message to
phone_numbers = ["<recipient_phone_number_1>", "<recipient_phone_number_2>", "<recipient_phone_number_3>"]

# Template details
template_name = "<your_template_name>"
template_language = "en_US"
# template_parameters = [
#     {"type": "text", "text": "<variable_1_value>"},
#     {"type": "text", "text": "<variable_2_value>"}
# ]

# Function to send template message
def send_template_message(phone_number):
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {
                "code": template_language
            },
            "components": [
                {
                    "type": "body",
                    # "parameters": template_parameters
                }
            ]
        }
    }

    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print(f"Message sent successfully to {phone_number}!")
    else:
        print(f"Failed to send message to {phone_number}. Status code: {response.status_code}, Response: {response.text}")

# Send messages to all phone numbers in the list
for number in phone_numbers:
    send_template_message(number)
