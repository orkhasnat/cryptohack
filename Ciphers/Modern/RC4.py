#!/usr/bin/python

class RC4:
	def __init__(self, key = None):
		self.state = range(256) # initialization of the permutation table
		self.x = self.y = 0 # the indexes x and y, instead of i and j

		if key is not None:
			self.key = key
			self.init(key)

	# Key schedule
	def init(self, key):
		for i in range(256):
			self.x = (ord(key[i % len(key)]) + self.state[i] + self.x) & 0xFF
			self.state[i], self.state[self.x] = self.state[self.x], self.state[i]
		self.x = 0

	# Decrypt binary input data
	def binaryDecrypt(self, data):
		output = [None]*len(data)
		for i in xrange(len(data)):
			self.x = (self.x + 1) & 0xFF
			self.y = (self.state[self.x] + self.y) & 0xFF
			self.state[self.x], self.state[self.y] = self.state[self.y], self.state[self.x]
			output[i] = (data[i] ^ self.state[(self.state[self.x] + self.state[self.y]) & 0xFF])
		return bytearray(output)
		
