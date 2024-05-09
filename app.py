import requests
from bs4 import BeautifulSoup

# Function to fetch live cricket data from the website
def fetch_live_cricket_data(url):
    try:
        # Send GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract relevant information
        runs_in_over = []
        over_elements = soup.find_all("div", class_="over")
        for over_element in over_elements:
            runs = int(over_element.find("span", class_="runs").text)
            runs_in_over.append(runs)
        
        wickets_element = soup.find("div", class_="wickets")
        wickets = int(wickets_element.text)
        
        players_scores = {}
        player_elements = soup.find_all("div", class_="player-score")
        for player_element in player_elements:
            player_name = player_element.find("div", class_="player-name").text
            player_score = int(player_element.find("div", class_="score").text)
            players_scores[player_name] = player_score
        
        # Create a dictionary to store the extracted data
        live_cricket_data = {
            "runs_in_over": runs_in_over,
            "wickets": wickets,
            "players_scores": players_scores
        }
        
        return live_cricket_data
    
    except Exception as e:
        print("Error fetching live cricket data:", e)
        return None

# Test the function
url = "https://crex.live/scoreboard/PBV/1L8/1st-Match/MP/MQ/fr-vs-mlt-1st-match-mdina-cup-t20-2024/live"
data = fetch_live_cricket_data(url)
print(data)
