from threading import Thread
from app import create_app
from app.heartbeat_monitor import monitor_heartbeat

# Function to run the heartbeat monitor in a separate thread
def run_heartbeat_monitor():
    monitor_heartbeat()

if __name__ == '__main__':
    # Start the heartbeat monitor in a separate thread
    heartbeat_thread = Thread(target=run_heartbeat_monitor)
    heartbeat_thread.daemon = True
    heartbeat_thread.start()

    # Run Flask app in the main thread
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
