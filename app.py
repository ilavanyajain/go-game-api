# CODE-1,
# make a file name app.py,

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Go Game Score Calculation API. Use the format /<p1>/<p2>/<p3> to calculate the maximum number of draws."

@app.route('/<int:p1>/<int:p2>/<int:p3>', methods=['GET'])
def calculate_draws(p1, p2, p3):
    # Ensure the points are in non-decreasing order
    if not (p1 <= p2 <= p3):
        return jsonify(max_draws=-1)
    
    # Calculate the total points
    total_points = p1 + p2 + p3
    
    # Calculate the number of games played
    total_games = total_points // 2

    # Check if the points can form a valid set of games
    if total_points % 2 != 0 or p3 > p1 + p2:
        return jsonify(max_draws=-1)

    # Calculate the maximum number of draws
    max_draws = total_games - (p3 - p2)

    return jsonify(max_draws=max(0, max_draws))

if __name__ == '__main__':
    app.run(debug=True)

