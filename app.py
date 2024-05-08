from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
tournaments_data = {
    'IPL 2024': {
        'matches': [
            {
                'match_id': 1,
                'pitch_report': 'Pitch is dry with cracks, good for spinners.',
                'toss_status': 'Mumbai Indians won the toss and elected to bat.',
                'current_players': ['Kohli', 'Rohit', 'Dhoni', 'Pandya'],
                'bowler': 'Bumrah',
                'target': '250'
            }
        ]
    }
}

# Route to serve the index page
@app.route('/')
def index():
    return render_template('index.html')

# API route to fetch tournament data
@app.route('/api/tournaments')
def get_tournaments():
    return jsonify(tournaments_data)

# API route to fetch match data for a specific tournament
@app.route('/api/matches/<tournament_name>')
def get_matches(tournament_name):
    if tournament_name in tournaments_data:
        return jsonify(tournaments_data[tournament_name]['matches'])
    else:
        return jsonify({'error': 'Tournament not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
