file1 = open('/Users/Barrob16/Documents/Project/htweet.txt')
file2 = open('/Users/Barrob16/Documents/Project/hhashtag.txt')

import markovgen
import hashtaggen
import time

markov = markovgen.Markov(file1)
markov2 = hashtaggen.Hashtag(file2)

for i in range(1):
	print ''
	print markov.generate_markov_text() + ".", '#', markov2.generate_markov_text() 
	print ''

 
