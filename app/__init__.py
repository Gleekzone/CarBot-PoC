from flask import Flask
from app.config import Config
from app.api import whatsapp, health_check
from openinference.instrumentation.langchain import LangChainInstrumentor
from phoenix.otel import register
import phoenix as px

from dotenv import load_dotenv

load_dotenv()

tracer_provider = register(endpoint=Config.PHOENIX_COLLECTOR_ENDPOINT)
LangChainInstrumentor(tracer_provider=tracer_provider).instrument(skip_dep_check=True)


# Create a Flask application instance
def create_app():
    """Create a Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(whatsapp.bp)
    app.register_blueprint(health_check.bp)

    return app
