#!/bin/env python

import random

class Vector(object):
	def __init__(self):
		self.x=0
		self.y=0
		self.factor=1
		self.maxspeed=20

	def set(self):
		if self.chance():
			a = 1 if self.chance() else -1
			self.x = self.x + a * self.factor

		if self.chance():
			b = 1 if self.chance() else -1
			self.y = self.y + b * self.factor

		if self.x > self.maxspeed:
			self.x = self.maxspeed
		elif self.x <= -self.maxspeed:
			self.x = -self.maxspeed

		if self.y > self.maxspeed:
			self.y = self.maxspeed
		elif self.y <= -self.maxspeed:
			self.y = -self.maxspeed


	def chance(self):
		return random.randint(0,100) > 50
		
