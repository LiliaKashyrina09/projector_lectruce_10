import random
import csv

players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']

results = []
for _ in range(100):
    for player in players:
        score = random.randint(0, 1000)
        results.append((player, score))

with open('game_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(results) 


