from colorama import init, Fore, Back, Style
init()
class Game():
	def __init__(self):
		self.sizeW = 20
		self.sizeH = 20
		self.gameRunfl = True
		self.player = [self.sizeW//2, self.sizeH//2]
		self.prevplayer = [self.sizeW//2, self.sizeH//2]
		self.map = [["_" for x in range(self.sizeW)] for y in range(self.sizeH)]
		self.map[self.player[0]][self.player[1]] = "+"
		self.comm = ""
		self.updateAndPrintMap()
		self.update()

	def regenerateMap(self):	self.map = [["_" for x in range(self.sizeW)] for y in range(self.sizeH)]
	def updateAndPrintMap(self):
		self.map[self.player[0]][self.player[1]] = Fore.RED + "+" + Style.RESET_ALL
		print(self.player[0], self.player[1])
		self.map[self.prevplayer[0]][self.prevplayer[1]] = "_"
		print(self.prevplayer[0], self.prevplayer[1])
		for y in self.map:
			r = ""
			for x in y:
				r += x + " "
			print(r)
	def commandUpdate(self): self.comm = input()
	
	def update(self):
		while(self.gameRunfl):
			match self.comm:
				case "d": 
					self.prevplayer = [self.player[0], self.player[1]]
					self.player[1]+=1 
					self.updateAndPrintMap() 
					self.commandUpdate()
				case "a": 
					self.prevplayer = [self.player[0], self.player[1]]
					self.player[1]-=1
					self.updateAndPrintMap() 
					self.commandUpdate()
				case "w": 
					self.prevplayer = [self.player[0], self.player[1]]
					self.player[0]-=1 
					self.updateAndPrintMap() 
					self.commandUpdate()
				case "s": 
					self.prevplayer = [self.player[0], self.player[1]]
					self.player[0]+=1 
					self.updateAndPrintMap() 
					self.commandUpdate()
				case "end": self.gameRunfl = False
				case default: self.commandUpdate()

init()
Game()
