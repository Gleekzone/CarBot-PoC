import time
from flask import Blueprint, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

from app.services.twilio_service import TwilioWhatsAppService
from app.agent.agents.sales_agent import agent_executor

bp = Blueprint('whatsapp', __name__)


@bp.route('/send_message', methods=['POST'])
def send_message():
    """Send a Whatsapp message."""
    # Get the message details from the request
    data = request.get_json()
    to = data.get('to')
    body = data.get('body')

    if not to or not body:
        return jsonify({"error": "Missing 'to' or 'body' in request"}), 400
  
    try:
        message_sid = TwilioWhatsAppService.send_message(to, body)
        return jsonify({"message_sid": message_sid}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/chatbot', methods=['POST', 'GET'])
def chatbot():
    """Handle incoming messages from WhatsApp."""
    try:
        incoming_msg = request.values.get('Body', '').lower()
        response = MessagingResponse()
        if incoming_msg:
            #Invocar el agente de ventas
            res = agent_executor.invoke({
                "input": incoming_msg
            })
            final_answer = res["output"] if isinstance(res, dict) else res.content
            response.message(final_answer)
            time.sleep(1.5)
        else:
            final_answer = "Lo siento, no entendí tu mensaje."
        # Get the incoming message
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")

    return str(response)
