import json
from datetime import datetime
from twilio.rest import Client

def load_contacts(filename='contacts.json'):
    with open(filename, 'r') as file:
        return json.load(file)
    
def check_events(contacts):
    today = datetime.today().strftime('%Y-%m-%d')
    today_events = []

    for contact in contacts:
        try:
            # Check if the 'event_date' field exists
            if 'event_date' not in contact:
                raise KeyError(f"Missing 'event_date' for contact: {contact.get('name', 'Unknown Contact')}")
            
            # Validate the 'event_date' format
            try:
                event_date = datetime.strptime(contact['event_date'], '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                raise ValueError(f"Invalid date format for contact: {contact.get('name', 'Unknown Contact')}. Expected format: YYYY-MM-DD")

            # Check if 'event_type' field exists and is not empty
            if not contact.get('event_type') or contact['event_type'].strip() == "":
                raise ValueError(f"Missing or invalid 'event_type' for contact: {contact.get('name', 'Unknown Contact')}")

            # Add the contact to today's events if the date matches
            if event_date == today:
                today_events.append(contact)
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    return today_events

def send_sms(account_sid, auth_token, twilio_number, to_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )
    print(f'Your special message has been sent to {to_number}: {message.sid}. Way to go, they are going to be so happy you remembered them!')