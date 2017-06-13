#!/usr/bin/python

import matplotlib.pyplot as plt

file = open("Limerick 2/limerick_x100_iter_loss.txt", "r")

numbers = []

for line in file:
	try:
		numbers.append(float(line))
	except ValueError as e:
		print e

plt.plot(numbers)
plt.ylabel('Loss')
plt.show()