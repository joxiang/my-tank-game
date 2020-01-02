from tank import *
class Bullet(Tank):
	def move(self, dir, angle):
		self.dir = dir
		self.angle = angle
		self.imgc = pygame.image.load(self.img).convert_alpha()
		self.imgd = pygame.transform.rotate(self.imgc,self.angle)

		if self.dir == up:
			self.y-=self.step
		elif self.dir == down:
			self.y+=self.step
		elif self.dir == left:
			self.x-=self.step
		elif self.dir == right:
			self.x+=self.step

	def drawImgd(self):
		if self.alive == True:
			self.alive = self.inarea()
			self.win.blit(self.imgd,(int(self.x - self.imgc.get_size()[0]/2),(int(self.y+3 - self.imgc.get_size()[1]/2))))
