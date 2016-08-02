"""
Zonk is addictive dice game. In each round player rolls 6 dice.
Then (s)he composes combinations from them.
Each combination gives certain points.

Then player can take one or more dice combinations to his hand
and re-roll remaining dice or save his score.
Dice in player's hand won't be taken into account in subsequent rolls.

If no combinations can be composed - situation is called "zonk".
Player thrown zonk loses all points in this round and next player moves.
So it's player decision when to reroll and when to stop and save his score.

Your task is simple - just evaluate current roll
and return maximum number of points can be scored from it.
If no combinations can be made
 - function must return string "Zonk" (without quotes).

There are different variations of Zonk.
In this kata, we will use most common table of combinations:

Combination	Example roll	Points
Straight (1,2,3,4,5 and 6)	6 3 1 2 5 4	1000 points
Three pairs of any dice	2 2 4 4 1 1	750 points
Three of 1	1 4 1 1	1000 points
Three of 2	2 3 4 2 2	200 points
Three of 3	3 4 3 6 3 2	300 points
Three of 4	4 4 4	400 points
Three of 5	2 5 5 5 4	500 points
Three of 6	6 6 2 6	600 points
Four of a kind	1 1 1 1 4 6	2 × Three-of-a-kind score (in example, 2000 pts)
Five of a kind	5 5 5 4 5 5	3 × Three-of-a-kind score (in example, 1500 pts)
Six of a kind	4 4 4 4 4 4	4 × Three-of-a-kind score (in example, 1600 pts)
Every 1	4 3 1 2 2	100 points
Every 5	5 2 6	50 points
Each die cannot be used in multiple combinations the same time,
so three pairs of 2, 3 and 5 will worth you only 750 points
(for three pairs), not 850 (for three pairs and two fives).
But you can select multiple combinations, 2 2 2 1 6 will worth you 300 points
(200 for three-of-kind '2' plus 100 for single '1' die)
"""


def get_score(dice):
	score = 0
	numbers = [0,0,0,0,0,0]
	pairs = 0
	for die in dice:
		numbers[die-1] += 1
	print(numbers)
	for i, number in enumerate(numbers):
		if i == 0 and number > 2:
			score += (number-2) * 1000
		elif number == 6:
			score += (i+1)*100 * 4
		elif number == 5:
			score += (i+1)*100 * 3
		elif number == 4:
			score += (i+1)*100 * 2
		elif number == 3:
			score += (i+1)*100 * 1
		elif number == 2:
			pairs += 1
	if pairs == 3:
		score += 750
	if not pairs == 3 and numbers[0] <3:
		score += 100 * numbers[0]
	if not pairs == 3 and numbers[4] <3:
		score += 50 * numbers[4]
	if len(set(numbers)) == 1:
		score = 1000
	return score or "Zonk"

dice = [2,2,2,2,1,5]
print(get_score(dice))