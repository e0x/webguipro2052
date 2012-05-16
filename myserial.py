EIGHTBITS=None
STOPBITS_ONE=None
PARITY_NONE=None

class Serial:
	def __init__(self,port=None,baudrate=None,parity=None,stopbits=None,bytesize=None):
                pass

	def open(self):
		pass
	
	def close(self):
		pass

	def read(size=1):
		return 'a' * size

	def write(self,data):
		return len(data)
        
	def isOpen(self):
		pass

	def inWaiting(self):
		i = 10
		while i < 1:
			i -= 1
			return i
	


