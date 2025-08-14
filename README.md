# 🚀 IA SALES AGENTE
POC: AI-powered sales assistant using LangChain, OpenIA and Phoenix.
This POC creates an intelligent commercial chatbot with GPT-4 that communicates via WhatsApp using Flask and Twilio. It answers questions using product information, financing plans, and the company’s value proposition, leveraging RAG to provide more accurate responses. Additionally, it corrects user input errors and is monitored in real time with Phoenix from Arize AI. 
**This project is intended for educational and experimental purposes only, and is used solely for a personal portfolio.**

## Dataset

The dataset used for this project was downloaded from Kaggle: [Cars Datasets (2025) by Abdul Malik](https://www.kaggle.com/datasets/abdulmalik1518/cars-datasets-2025?resource=download)  
*Note: The dataset is used only for educational and personal portfolio purposes, and is not being sold or redistributed.*

## Technologies

- Python
- Flask
- Twilio API (WhatsApp)
- GPT-4 via OpenAI
- LangChain (RAG)
- Phoenix from Arize AI

## Step 1: Clone the Repository

```bash
git clone https://github.com/Gleekzone/ia_agent.git
cd your-repo
```

## Step 2: Create Required Accounts

| Service  | Purpose              | Sign Up URL                                 |
|----------|----------------------|---------------------------------------------|
| OpenAI   | LLM capabilities     | https://platform.openai.com/signup          |
| Twilio   | WhatsApp integration | https://www.twilio.com/try-twilio           |
| Ngrok    | Public URL tunneling | https://dashboard.ngrok.com/signup          |
| Phoenix  | Observability        | https://app.phoenix.arize.com/login/sign-up |


## Step 3: Set Up API Keys

- After signing up, retrieve your API keys from each platform.
- Create a .env file in the root directory:
```
    touch .env
```
- Add your keys:
```
    # Flask
    FLASK_ENV=development
    FLASK_APP=name_app

    # CSV File Path
    CSV_FILE_PATH=./data/cars_datasets_2025.csv

    # OpenAI API Key
    OPENAI_API_KEY=your_openai_api_key

    # NGROK token
    NGROK_AUTH_TOKEN=your_ngrok_token

    # Twilio Credentials
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_token
    TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886  # Número del sandbox de Twilio para WhatsApp

    # Phoenix Configuration
    PHOENIX_API_KEY=your_phoenix_api_key
    PHOENIX_CLIENT_HEADERS=api_key={PHOENIX_API_KEY}
    PHOENIX_COLLECTOR_ENDPOINT=arize_phoenix_url
```

## Step 4: Create Python enviroment
This project uses Poetry for dependency management

```
    # Create Python enviroment
    $ Poetry install
```

## Step 5: Set Up Ngrok for Local Testing

```
    # Authenticate your Ngrok account:
    ngrok config add-authtoken your_ngrok_token

    In a new terminal, start Ngrok on the same port: 5001 
    ngrok http 5000

    # Copy the generated HTTPS URL (e.g., https://abc123.ngrok-free.app ) — use this as your webhook or public endpoint in Twilio or external services.
```

## Step 6: Run the Project
```
    python app.py
    # or if Flask
    flask run --port=5001 
```

### 📱 WhatsApp Integration with Twilio (Sandbox Mode)

    This project is a proof of concept (POC), so it uses the **Twilio WhatsApp sandbox** for sending and receiving messages.

    To configure the WhatsApp sandbox, follow the official Twilio Quickstart:

    👉 [Twilio WhatsApp Quickstart (Python)](https://www.twilio.com/docs/whatsapp/quickstart/python)

    #### 🛠 Steps to Set Up:

    1. **Create a Twilio account** at [twilio.com](https://www.twilio.com/).
    2. **Go to the WhatsApp Sandbox** section in your Twilio Console.
    3. **Follow the instructions** to join the sandbox using your phone number (send the code to `+14155238886`).
    4. **Note your sandbox credentials**:
    - `TWILIO_ACCOUNT_SID`
    - `TWILIO_AUTH_TOKEN`
    - `TWILIO_WHATSAPP_NUMBER` (e.g., `whatsapp:+14155238886`)
    5. **Set these variables in your `.env` file**:

        ```env
        TWILIO_ACCOUNT_SID=your_account_sid
        TWILIO_AUTH_TOKEN=your_auth_token
        TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
        ```

    This setup allows you to simulate WhatsApp conversations during development without requiring business approval.


## Step 7: Access the Phoenix Dashboard

https://app.phoenix.arize.com/login

## Step 7: Run Tests (In this POC is pending)
 ```
    pytest  
```
