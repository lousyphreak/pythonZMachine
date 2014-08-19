from struct import unpack, pack
from opcodeList import opCodes
import objects
import textParser
from screen import Screen
from opcodeDecode import ConstValue

# http://inform-fiction.org/zmachine/standards/z1point0/sect11.html



class RoutineScope:
	def __init__(self, machine, parent, address, locals, returnAddress, returnValue):
		self.parent = parent
		self.returnAddress = returnAddress
		self.returnValue = returnValue
		# main scope has no address --> no locals
		if address is not None:
			self.localsCount=machine.readByte(address)
			self.locals = [0]*self.localsCount
			address+=1
			if machine.header.version < 5:
				for i in range(self.localsCount):
					self.locals[i] = machine.readWord(address)
					address+=2
		
		# initialize locals with call parameters
		self.numLocals = len(locals)
		for i in range(len(locals)):
			self.locals[i] = locals[i].load()

		self.stack = []
		self.startAddress = address

		machine.printDebug('new Scope: stack:{0}', id(self.stack))


class Header:
	def __init__(self, machine):
		self.version =			  machine.readByte(0x00)
		self.flags1 =			   machine.readWord(0x01)
		self.highMem =			  machine.readWord(0x04)
		self.initPC =			   machine.readWord(0x06)
		self.dict =				 machine.readWord(0x08)
		self.objectTable =		  machine.readWord(0x0A)
		self.globals =			  machine.readWord(0x0C)
		self.staticMem =			machine.readWord(0x0E)
		self.flags2 =			   machine.readWord(0x10)
		self.serialCode = machine.data[0x12:0x18].decode("utf-8")
		self.a =					machine.readWord(0x12)
		self.b =					machine.readWord(0x14)
		self.c =					machine.readWord(0x16)
		self.abbrev =			   machine.readWord(0x18)
		self.length =			   machine.readWord(0x1A)
		self.checksum =			 machine.readWord(0x1C)
		self.interpreterNumber =	machine.readByte(0x1E)
		self.interpreterVersion =   machine.readByte(0x1F)
		self.scHeight =			 machine.readByte(0x20)
		self.scWidth =			  machine.readByte(0x21)
		self.scWidthUnits =		 machine.readWord(0x22)
		self.scHeightUnits =		machine.readWord(0x24)

		if self.version == 6:
			self.fontHeight =		   machine.readByte(0x26)
			self.fontWidth =			machine.readByte(0x27)
		else:
			self.fontWidth =			machine.readByte(0x26)
			self.fontHeight =		   machine.readByte(0x27)

		self.routines =			 machine.readWord(0x28)
		self.staticStrings =		machine.readWord(0x2A)
		self.bgColor =			  machine.readByte(0x2C)
		self.fgColor =			  machine.readByte(0x2D)
		self.termCharTable =		machine.readWord(0x2E)
		self.pixelWidthStream3 =	machine.readWord(0x30)
		self.revNumber =			machine.readWord(0x32)
		self.alphabetTable =		machine.readWord(0x34)
		self.headerExtensionTable = machine.readWord(0x36)
		self.userName = machine.data[0x38:0x3C].decode("utf-8")
		self.n =					machine.readWord(0x38)
		self.o =					machine.readByte(0x3A)
		self.compiler = machine.data[0x3C:0x40].decode("utf-8")
		self.p =					machine.readByte(0x3C)
		self.q =					machine.readByte(0x3E)
		self.interpreterVersion = machine.readByte(0)

		pass

class ZMachine:
	def __init__(self, basePath, fileName):
		self.readFile(basePath, fileName)

		self.header = Header(self)

		self.screen = Screen(self)

		self.setup()
		self.run()

	def readFile(self, basePath, fileName):
		self.data = [0]
		with open(basePath + fileName, 'rb') as file:
			self.data = bytearray(file.read())
		pass

	def setup(self):
		self.pc = self.header.initPC
		self.currentScope = RoutineScope(self, None, None, [], -1, -1)
		textParser.init(self)
		self.screen.init()
		pass

	def run(self):
		val = 0
		while True:
			self.printDebug("")
			opCode = self.readBytePC()
			self.printDebug('address:', hex(self.pc-1),'opCode:', opCode, hex(opCode))

			opc = opCodes[opCode](self)
			self.printDebug('opCode', opc)
			opc.decode(self)
			opc.call(self)

			val += 1
			val %= 20
			if val == 0:
				self.screen.update()
				#print(val)
		pass

	def readByte(self, address):
		ret, = unpack('>B', self.data[address:address+1])
		return ret

	def readWord(self, address):
		ret, = unpack('>H', self.data[address:address+2])
		return ret

	def writeByte(self, address, value):
		val = pack('>B', value & 0xff)
		self.data[address] = val[0]

	def writeWord(self, address, value):
		val = pack('>H', value & 0xffff)
		self.data[address+0] = val[0]
		self.data[address+1] = val[1]

	def readByteGlobals(self, offset):
		return self.readByte(self.header.globals+offset)

	def readWordGlobals(self, offset):
		return self.readWord(self.header.globals+offset)

	def writeByteGlobals(self, offset, value):
		self.writeByte(self.header.globals+offset, value)

	def writeWordGlobals(self, offset, value):
		self.writeWord(self.header.globals+offset, value)

	def readBytePC(self):
		value = self.readByte(self.pc)
		self.pc += 1
		return value

	def readWordPC(self):
		value = self.readWord(self.pc)
		self.pc += 2
		return value

	def unpackAddressRoutine(self, address):
		if self.header.version <= 3:
			return address * 2
		if self.header.version <= 5:
			return address * 4
		if self.header.version <= 7:
			return address * 4 + self.header.routines * 8
		if self.header.version <= 8:
			return address * 8

	def unpackAddressPrint(self, address):
		if self.header.version <= 3:
			return address * 2
		if self.header.version <= 5:
			return address * 4
		if self.header.version <= 7:
			# verify!
			return address * 4 + self.header.staticStrings * 8
		if self.header.version <= 8:
			return address * 8

	def call(self, address, param, returnAddress, returnValue):
		targetAddress = address.load()

		if targetAddress == 0:
			self.printDebug('ABORT CALL --> DEST == 0')
			if returnValue != None:
				returnValue.store(0)
			return
		address = self.unpackAddressRoutine(targetAddress)
		self.printDebug("calling", address, hex(address), 'params:', param, 'old stack:', id(self.currentScope.stack))
		self.currentScope = RoutineScope(self, self.currentScope, address, param, returnAddress, returnValue)
		self.printDebug('new stack:', id(self.currentScope.stack))
		self.pc = self.currentScope.startAddress

	def ret(self, value):
		oldScope = self.currentScope
		newScope = self.currentScope.parent
		self.currentScope = newScope

		self.printDebug('oldstack:', id(oldScope.stack),'new stack:', id(newScope.stack))

		self.pc = oldScope.returnAddress

		retValue = value.load()
		if oldScope.returnValue is not None:
			oldScope.returnValue.store(retValue)

	def jump(self, target):
		if target == 0:
			self.printDebug('RFalse!')
			self.ret(ConstValue(0, 1))
			return
		elif target == 1:
			self.printDebug('RTrue!')
			self.ret(ConstValue(1, 1))
			return

		self.printDebug('jumping!')
		self.pc = target
		pass

	def getPropertiesLength(self):
		if self.header.version < 4:
			return 31 * 2
		return 63 * 2

	def getObjectLength(self):
		if self.header.version < 4:
			return 9
		return 14

	def getObject(self, objectNum):
		objectsStartAddress = self.header.objectTable + self.getPropertiesLength()
		objectAddress = objectsStartAddress + self.getObjectLength() * (objectNum-1)
		
		return objects.Object(self, objectAddress, objectNum)

	def updateStatus(self):
		pass

	def readCommand(self, textTarget, parseBuffer):
		# reading
		maxLen = self.readByte(textTarget)
		if self.header.version < 5:
			maxLen -= 1

		text, timedAbort = self.screen.readText(maxLen)

		offset = 0
		if self.header.version > 4:
			offset = self.readByte(textTarget + 1) + 1

		for i in range(len(text)):
			c = text[i]
			self.writeByte(textTarget+offset+i, ord(c))

		if self.header.version > 4:
			self.writeByte(textTarget+1, len(text))

		# parsing
		if parseBuffer == 0:
			return timedAbort
		maxWords = self.readByte(parseBuffer)

		decodedWords = textParser.parse(self, text)

		self.writeByte(parseBuffer+1, len(decodedWords))

		for i in range(len(decodedWords)):
			dWord = decodedWords[i]
			self.writeWord(parseBuffer+i*4+2, dWord.address)
			self.writeByte(parseBuffer+i*4+4, dWord.numChars)
			self.writeByte(parseBuffer+i*4+5, dWord.textPos)

		return timedAbort

	def printScreen(self, text):
		self.screen.print(text)
		pass

	def printDebug(self, text, *args):
		pass

def main():
	ff = 13

	if ff == 0:
		basePath = '../'
		fileName = 'Enchanter.z3'
	elif ff < 10:
		basePath = 'F:/zork/'

		if ff == 1:
			fileName = 'zork.z3'
		if ff == 2:
			fileName = 'hhgg.z3'
	elif ff < 200:
		basePath = './'

		if ff == 11:
			fileName = 'Ruins.z8'

		if ff == 13:
			fileName = 'czech.z3'
		if ff == 14:
			fileName = 'czech.z4'
		if ff == 15:
			fileName = 'czech.z5'
		if ff == 16:
			fileName = 'czech.z6'
		if ff == 17:
			fileName = 'czech.z7'
		if ff == 18:
			fileName = 'czech.z8'

		if ff == 25:
			fileName = 'praxix.z5'

	zm = ZMachine(basePath, fileName)


	pass


if __name__ == '__main__':
	main()