// Fetch match updates from the server
fetch('/api/match-updates')
    .then(response => response.json())
    .then(data => {
        // Update the HTML content with match updates
        const matchUpdatesDiv = document.getElementById('match-updates');
        matchUpdatesDiv.innerHTML = `
            <h2>${data.tournament}</h2>
            <p><strong>Pitch Report:</strong> ${data.pitch_report}</p>
            <p><strong>Probability:</strong> ${data.probability}</p>
            <p><strong>Score:</strong> ${data.score}</p>
            <p><strong>Wickets:</strong> ${data.wickets}</p>
            <p><strong>Current Players:</strong> ${data.current_players.join(', ')}</p>
            <p><strong>Bowler:</strong> ${data.bowler}</p>
            <p><strong>Target:</strong> ${data.target}</p>
        `;
    })
    .catch(error => console.error('Error fetching match updates:', error));

