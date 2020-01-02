from common import *
from const import *

class Tank(Common):
	def __init__(self, url, x, y):
		super().__init__(url, x, y)
		self.step = 0.23456789
		self.dir = up
		self.angle = 0.0
		self.imgd = pygame.transform.rotate(self.imgc, self.angle)
		self.n = 0

	def move(self, dir, angle):
		self.angle = angle
		self.imgc = pygame.image.load(self.img).convert_alpha()
		self.imgd = pygame.transform.rotate(self.imgc, self.angle)
		# print(self.step)
		self.dir = dir

		self.img = "tank-"+str(self.n+1)+".png"
		if self.dir == up:
			self.y-=self.step
		elif self.dir == down:
			self.y+=self.step
		elif self.dir == left:
			self.x-=self.step
		elif self.dir == right:
			self.x+=self.step
	def drawImgd(self, worldTime):
		if worldTime % 10 == 0:
			self.n+=1
			self.n%=3
		if self.alive == True:
			self.testB()
			self.win.blit(self.imgd,(int(self.x - self.imgc.get_size()[0]/2),(int(self.y - self.imgc.get_size()[1]/2))))

