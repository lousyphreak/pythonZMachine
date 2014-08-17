import pygame
import sys


class Screen:
	class Cursor:
		x = 0
		y = 0
		width = 80
		height = 25

		def __init__(self, width, height):
			self.width = width
			self.height = height

		def advance(self):
			self.x +=1
			if self.x >= self.width:
				self.x = 0
				self.y += 1

			if self.y >= self.height:
				self.y = self.height-1
				return True
			return False

		def newline(self):
			self.x = 0
			self.y += 1
			if self.y >= self.height:
				self.y = self.height-1
				return True
			return False

	def __init__(self,machine):
		self.machine = machine


	def init(self):
		ret = pygame.init()

		self.charsPerLine = 80
		self.numLines = 35
		self.fontHeight = 16
		self.fontWidth = 10

		self.cursor = self.Cursor(self.charsPerLine, self.numLines)

		emptyLine = ''
		for c in range(self.charsPerLine):
			emptyLine += ' '
		self.emptyLine=bytearray(emptyLine.encode())

		self.text = []
		for line in range(self.numLines):
			self.text.append(self.emptyLine[:])

		self.bg = 0, 0, 0
		self.fg = 255, 255, 255

		self.screenRes = (self.charsPerLine*self.fontWidth, self.numLines*self.fontHeight)

		self.screen = pygame.display.set_mode(self.screenRes)
		self.myfont = pygame.font.SysFont("monospace", self.fontHeight)

		self.update()

	def print(self, text):
		for c in text:
			self.printChar(c)

		self.update()
		pass

	def printChar(self, c):
		if c == '\n':
			newLine = self.cursor.newline()
		else:
			c = c.encode()
			line = self.text[self.cursor.y]
			line[self.cursor.x] = c[0]

			newLine = self.cursor.advance()

		if newLine:
			for i in range(1, self.numLines):
				self.text[i-1] = self.text[i]

			self.text[self.numLines-1] = self.emptyLine[:]
		
		pass


	def update(self):
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				sys.exit()

		self.screen.fill(self.bg)

		for l in range(self.numLines):
			ll = self.text[l]
			label = self.myfont.render(ll.decode("utf-8"), 1, self.fg)
			self.screen.blit(label, (0, l*self.fontHeight))

		pygame.display.flip()
		pass

