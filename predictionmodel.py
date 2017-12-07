#!/Users/hparsons/anaconda/bin/python
'''
the aim of this code is to make predictions
as to the completion rae of the JCMT's Large
Programs
'''

# need to provide a starting point - date and status of the programs

# need to grab output from database and create 
# i: an object for each program
# ii: an object 
#


import predictions

# schedule object 


from predictions import schedule

# weather object

from predictions import weather

with open('data/weather-average.csv','r') as datain: # will close file once done

	line = datain.readline()			# read the data line by line
	while line[0] == '#':				# any line that is a heading
		line = datain.readline()		# readline and move on

	for line in datain:					# data is comma separated line is interpreted automatically as a lost
		print (line)					# line is a tuple, does not let me use .split()
#		values = line.split()			# and having hard time with REGEX
# 		values = re.match("([\S]+)\,([\S]+)\,([\S]+)\,([\S]+)\,([\S]+)\,([\S]+)\,([\S]+)",line)
# 		month = values[0]
# 		for x in (len(line)-1):
# 			completion = {x+1: ((line[x+1])/100.)} # so band 1 March completion = {1:0.235}
# 			print (completion)

# once I am able to ... :
		keys = ["a", "b"]
		values = [1,2]
		zip(keys,values)
		for item in zip(keys,values):
			print (item)
			# output: ('a', 1) , ('b', 2)

# what targets/projects are available

from predictions import availability
