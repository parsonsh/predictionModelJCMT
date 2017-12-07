#!/Users/hparsons/anaconda/bin/python
'''
This wil contain all classes that pertain
to schedule for the prediction models
'''

class schdeule(object):
	print ('loaded class: schedule')
	'''
	what does this class do/what does
	the object this class makes contain?
	'''
	def __init__(self):
		'''
		defining for each date the project
		that has priority at the telescope
		'''
		self.date = None
		self.pp = None # priority project

	def priorities(self):
		'''
		given the schedule returns the 
		program priorities 
		'''
		