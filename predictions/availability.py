#!/Users/hparsons/anaconda/bin/python
'''
This wil contain all classes that pertain
to source/project availability for the 
prediction models
'''

class availability(object):
	print ('loaded class: availability')
	'''
	what does this class do/what does
	the object this class makes contain?
	'''
	def __init__(self):
		'''
		defining for each date, block of 
		time, and weather band, the project(s)
		that can be observed at the telescope
		'''
#note self.date = None has been defined in schedule