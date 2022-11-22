import json
import subprocess


def run_games(game_count):
    command = ['./battlesnake ', 'play', '--width', '11', '--height', '11', '--name', 'Bayesian', '--url', 'http://0.0.0.0:8000', '--name', 'Baseline', '--url', 'http://0.0.0.0:8080', '--output', 'out.log', '-g', 'wrapped', '-m', 'hz_islands_bridges']
    """Run a number of games and return the results."""
    game_stats = {'Bayes_wins':0, 'Baseline_wins':0, 'Bayes_win_rate':0, 'Baseline_win_rate':0, 'Average_game_duration':0}
    for i in range(game_count):
        #run bash command to run game
        result = subprocess.run(command, capture_output=True)
        #load logged game data
        with open('out.log') as f:
            game_data = f.readlines()
        #get game stats
        winner = game_data[-1].strip().split(',')[1].split(':')[1].strip('"')
        length = len(game_data) - 2
        #update game_stats
        if winner == 'Bayesian':
            game_stats['Bayes_wins'] += 1
        else:
            game_stats['Baseline_wins'] += 1
        game_stats['Average_game_duration'] += length
    #calculate win rates
    game_stats['Bayes_win_rate'] = game_stats['Bayes_wins'] / game_count
    game_stats['Baseline_win_rate'] = game_stats['Baseline_wins'] / game_count
    game_stats['Average_game_duration'] = game_stats['Average_game_duration'] / game_count
    #write game_stats to file
    with open('game_stats.json', 'w') as f:
        json.dump(game_stats, f)




run_games(20)
    