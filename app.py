from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# API route to fetch match updates
@app.route('/api/match-updates')
def match_updates():
    # Code to fetch match updates from the external source goes here
    # Replace the sample data with actual match updates
    match_updates_data = {
        'tournament': 'IPL 2024',
        'pitch_report': 'Pitch is dry with cracks, good for spinners.',
        'probability': '70%',
        'score': '160/4',
        'wickets': '4',
        'current_players': ['Kohli', 'Rohit', 'Dhoni', 'Pandya'],
        'bowler': 'Bumrah',
        'target': '250'
    }
    return jsonify(match_updates_data)

if __name__ == '__main__':
    app.run(debug=True)
