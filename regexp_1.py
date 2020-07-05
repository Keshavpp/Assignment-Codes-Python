#Course- Using Python to access web data
#Week 2 ; Assignment 
#Use http://py4e-data.dr-chuck.net/regex_sum_42.txt  \\ or \\ http://py4e-data.dr-chuck.net/regex_sum_582926.txt 
import re
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
	print('File cannot be opened:',fname)
	quit()

numlist = list()

for line in fh:
	line = line.rstrip()
	play = re.findall('[0-9]+',line)
	for i in range(0, len(play)):
		play[i]=int(play[i]) 
    	
	#number = float(play[0])
	add = sum(play)
	numlist.append(add)

adsum = sum(numlist)
print(adsum)