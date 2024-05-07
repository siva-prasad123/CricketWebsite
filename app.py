from flask import Flask
import requests
import time

app = Flask(__name__)

# Define your alert conditions
# For example, alert when a wicket falls or a boundary is hit
def check_alert_conditions(match_data):
    if match_data.get('wicket') or match_data.get('boundary'):
        return True
    return False

# Function to send alert message
def send_alert(message):
    # Replace this with your actual alerting mechanism
    print("Sending alert message:", message)

# Function to fetch match updates from the cricket website
def fetch_match_updates():
    # Replace 'match_website_url' with the actual URL of the cricket match website
    match_website_url = 'https://example.com/match-updates'
    
    while True:
        try:
            response = requests.get(match_website_url)
            match_data = response.json()
            
            # Check if alert conditions are met
            if check_alert_conditions(match_data):
                send_alert("Alert: Something happened in the match!")
                
        except Exception as e:
            print("Error fetching match updates:", e)
        
        # Fetch updates every 5 minutes (adjust as needed)
        time.sleep(300)

# Entry point for the Flask application
if __name__ == '__main__':
    # Start a separate thread to fetch match updates periodically
    import threading
    update_thread = threading.Thread(target=fetch_match_updates)
    update_thread.daemon = True
    update_thread.start()
    
    # Run the Flask application
    app.run(debug=True)

