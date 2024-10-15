from flask import Flask
import logging

# Initialize the app and logger
def create_app():
    app = Flask(__name__)
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    with app.app_context():
        # Import routes
        from .views import receive_heartbeat
        app.add_url_rule('/heartbeat', 'receive_heartbeat', receive_heartbeat, methods=['POST'])

    return app
