import os


# This class is responsible for loading and managing configuration settings.
class Config:
    """Configuration settings for the application."""
    # Flask
    FLASK_EN = os.getenv('FLASK_ENV', 'development')  # Default to development if not se
    FLASK_APP = os.getenv('FLASK_ENV', 'development')

    # Twilio configuration
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')  # Default Twilio WhatsApp number

    # OpenAI API Key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

    # CSV File Path
    CSV_FILE_PATH = os.getenv('CSV_FILE_PATH')  # Default path to the CSV file

    # URL website search
    WEBSITE_SEARCH_URL = os.getenv('WEBSITE_SEARCH_URL')

    # Phoenix Configuration
    PHOENIX_API_KEY = os.getenv("PHOENIX_API_KEY")
    PHOENIX_CLIENT_HEADERS = os.getenv(f"api_key={PHOENIX_API_KEY}")
    PHOENIX_COLLECTOR_ENDPOINT = os.getenv("PHOENIX_COLLECTOR_ENDPOINT")
