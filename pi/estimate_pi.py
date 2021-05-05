import random, math

## This script estimates pi by running a Monte Carlo simulation.
## A circle with radius = r is places inside a square with side = 2r
## so, A(square) = pi * r^2 and A(square) = 4 * r^2
## points are ramly plotted inside the square, some of which will also fall within the cirle (when x^2 + y^2 < 1)
## the probability that the point is within the cirle is A(circle) / A(square), which simplifies to pi / 4
## and pi = 4 * P(point falling within circle)
## to estimate pi: Randomly plot many points inside the square, calculate the proportion that also fall within the cirlce, multply by 4 

def main():
	num_points = int(10 ** 6) # number of points to plot


	in_circle = 0
	i = 0

	while i < num_points: 
		x, y = get_points()

		if x**2 + y**2 < 1: # determine if the point is in the cirlce
			in_circle += 1
		i += 1

	pi_est = 4 * (in_circle / num_points)
	err = abs(pi_est - math.pi) / math.pi
	
	# print results to screen
	print('{0:,} points plotted'.format(num_points))
	print('pi approximation: {0:.6f}'.format(pi_est))
	print('Percent error: {0:.2%}'.format(err))


def get_points():
	# randomly generate coordinates for point
	x = 2*random.uniform(0,1)-1
	y = 2*random.uniform(0,1)-1
	return x, y

if __name__ == '__main__':
	main()