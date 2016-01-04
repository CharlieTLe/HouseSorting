# This script should take a group of people with their house preferences and 
# place them into houses. Each house should have the same amount of people.

import csv
import sys
import pprint
import random

assert len(sys.argv) == 4, "Incorrect number of arguments."

candidate_filename = sys.argv[1]
houses_filename = sys.argv[2]
MAX_HOUSE_CAPACITY = int(sys.argv[3])

pp = pprint.PrettyPrinter(indent=4)


# Create the houses from a CSV File
houses = []
with open(houses_filename) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		row['members'] = []
		houses.append(row)

# Place each candidate into a house based on their preferences
with open(candidate_filename) as csvfile:
	people = csv.DictReader(csvfile)
	for person in people.shuffle():
		# Flag whether person got placed into a house or not.
		foundHouse = False
		# The preference of the choice. The lower the better.
		choiceRank = 0

		# Try each choice the person has to place them into a house
		for choice_str in person['choices'].split(' '):
			choice = int(choice_str)

			# Don't put person in house if it's full!
			if len(houses[choice]['members']) < MAX_HOUSE_CAPACITY:
				assert houses[choice]['id'] == choice, "Bad houses"
				person['choice_rank'] = choiceRank
				houses[choice]['members'].append(person)
				foundHouse = True
				break
			choiceRank += 1
		assert foundHouse, "Couldn't find house for" + person['name']\
				+ "\nHouses:" + pp.pformat(houses)

# Prints the houses out with their members
for house in houses:
	print "House Number:\t", house['id']
	print "House:\t\t", house['house_name']
	print "Leader:\t\t", house['leader_name']
	print "Members:", len(house['members'])
	for member in house['members']:
		print "\t\t" + member['name'], "\tChoice Rank:", \
				member['choice_rank']
	print

