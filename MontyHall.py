import random

num_games = 1000
n = 0
swap_results = {'car': 0, 'goat': 0}
keep_results = {'car': 0, 'goat': 0}

while n < num_games:
	prizes = ['goat','goat','car']
	available_doors = ['1','2','3']

	random.shuffle(prizes)

	doors = {}

	for i in range(3):
		doors[str(i+1)] = prizes[i]

	first_choice = str(random.randint(1,3))

	available_doors.remove(first_choice)

	for i in available_doors:
		if doors[i] == 'goat':
			host_reveal = i

	available_doors.remove(host_reveal)

	player_choices = [available_doors[0], first_choice]

	swap = random.choice([True, False])

	if swap:
		prize = doors[available_doors[0]]
		swap_results[prize] += 1
	else:
		prize = doors[first_choice]
		keep_results[prize] += 1
	

	n += 1

print('results from swapping:')
print(swap_results)

print('results from keeping:')
print(keep_results)

print('odds of swapping to car:')
print(swap_results['car'] / num_games)

print('odds of keeping to car:')
print(keep_results['car'] / num_games)
