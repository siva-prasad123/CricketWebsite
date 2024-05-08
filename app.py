# serverless_functions/get_tournaments.py
import json

def handler(event, context):
    # Fetch tournament data from wherever you're sourcing it
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
    return {
        'statusCode': 200,
        'body': json.dumps(tournaments_data)
    }
