import requests
import json
import time

# WhatsApp API endpoint and access token
api_url = "https://graph.facebook.com/v19.0/112307325194751/messages"
access_token = "ACCESS_TOKEN"

# Header for the HTTP request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# List of phone numbers to send the message to
phone_numbers = ['', '']

# Template details
template_name = "TEMPLATE_NAME"
template_language = "en"
image_url = "IMAGE_URL"  # Replace with the public URL of your image

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
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": {
                                "link": image_url
                            }
                        }
                    ]
                },
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
    time.sleep(1)
