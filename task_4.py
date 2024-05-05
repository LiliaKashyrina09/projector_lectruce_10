import csv
import operator

high_scores = {}

with open('game_scores.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        player, score = row
        score = int(score)
        if player in high_scores:
            if score > high_scores[player]:
                high_scores[player] = score
        else:
            high_scores[player] = score

sorted_high_scores = sorted(high_scores.items(), key=operator.itemgetter(1), reverse=True)

with open('high_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Highest score'])
    writer.writerows(sorted_high_scores)

