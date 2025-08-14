# Twilio WhatsApp Service 
import os
from twilio.rest import Client
from app.config import Config
from typing import Optional

 # Get credentials from the config
account_sid = Config.TWILIO_ACCOUNT_SID
auth_token = Config.TWILIO_AUTH_TOKEN
twilio_number = Config.TWILIO_WHATSAPP_NUMBER

# This class is responsible for sending WhatsApp messages using Twilio API.
class TwilioWhatsAppService:

    @staticmethod
    def send_message(to: str, body: str) -> Optional[str]:
        """ Send a WhatsApp message to a specificed number."""
        client = Client(account_sid, auth_token)
        try:
            message = client.messages.create(
                body=body,
                from_=twilio_number,
                to=f'whatsapp:{to}',
            )
            print(twilio_number, f'whatsapp:{to}', body)
            return message.sid
        except Exception as e:
            print(f"Failed to send message: {e}")
            raise e

    @staticmethod
    def receive_message():
        return None