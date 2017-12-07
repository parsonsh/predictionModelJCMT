#!/Users/hparsons/anaconda/bin/python
'''
This wil contain all classes that pertain
to weather for the prediction models
'''

class weather(object):
	print ('loaded class: weather')
	'''
	what does this class do/what does
	the object this class makes contain?
	'''
	def __init__(self):
		'''
		defining for month the likelyhood
		for each weather band occuring
		throughout the enitre year
		'''
		self.month = None
		# want to make chance a dictionary with chance and band linked...

		self.band = None
		self.chance = None 
		


	
	def weatherinblock(self):
		'''
		for each block of time this method
		retunrs the weather band that is most 
		likely to occur
		'''	
#		return ()