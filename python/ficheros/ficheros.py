# -*- coding: utf-8 -*-

# Mi tercer programa en Phyton

# Manejo de ficheros y otras cosas

def count_char(text, char):
	count = 0
	for c in text:
		if c == char:
			count +=1
	return count
	
# filename = input("Introduce nombre del fichero: ")

with open("prueba.txt") as f:
	text = f.read()

for char in "abcdefghijklmnopqrstuvwxz":
	perc = 100 * count_char(text, char)/len(text)
	print ("{0} - {1}%".format(char, round(perc, 2)))

