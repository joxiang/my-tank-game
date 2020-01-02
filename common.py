import sys, random, math, pygame
from pygame.locals import *
from const import *

class Common(object):
	def __init__(self, url, x, y):
		self.img = url
		self.x = x
		self.y = y
		self.health = 0
		self.alive = False
		self.imgc = pygame.image.load(self.img).convert_alpha()
		self.win = pygame.display.set_mode((sw,sh))
		self.width = self.imgc.get_size()[0]
		self.height = self.imgc.get_size()[1]
	def drawImg(self):
		if self.alive == True:
			self.win.blit(self.imgc,(int(self.x - self.imgc.get_size()[0]/2),(int(self.y - self.imgc.get_size()[1]/2))))

	def drawImgd(self):
		if self.alive == True:
			self.testB()
			self.win.blit(self.imgd,(int(self.x - self.imgc.get_size()[0]/2),(int(self.y - self.imgc.get_size()[1]/2))))

	def testB(self):
		self.width = self.imgc.get_size()[0]
		self.height = self.imgc.get_size()[1]
		if self.x < self.width/2:
			self.x = self.width/2
		if self.x > sw - self.width/2:
			self.x = sw - self.width/2
		if self.y < self.height/2:
			self.y = self.height/2
		if self.y > sh - self.height/2:
			self.y = sh - self.height/2
	def inarea(self):
		if self.width/2< self.x < sw - self.width/2 and self.height/2 < self.y < sh - self.height/2:
			return True
		else:
			return False