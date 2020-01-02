import sys, random, math, pygame
from pygame.locals import *

class Common(object):
	def __init__(self, url, x, y, health, alive):
		self.__img = url
		self.__x = x
		self.__y = y
		self.__health = health
		self.alive = alive
	#The following are for read my hidden成员变量
	def getx(self):
		return self.__x
	def setx(self, x): 
		self.__x = x
	x = property(getx, setx)

	def gety(self):
		return self.__y
	def sety(self, y): 
		self.__y = y
	y = property(gety, sety)

	def gethealth(self):
		return self.__health
	def sethealth(self, health): 
		self.__health = health
	health = property(gethealth, sethealth)

	def getimg(self):
		return pygame.image.load(self.__img).convert_alpha()
	def setimg(self, url):
		self.__img = url
	img = property(getimg, setimg)

	def drawImg(self, win):
		self.win = win
		win.blit(self.img,(int(self.x - self.img.get_size()[0]/2),(int(self.y - self.img.get_size()[1]/2))))