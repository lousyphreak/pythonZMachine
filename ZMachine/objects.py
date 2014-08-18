import zscii


def init(machine):
	ot = ObjectTable(machine)
	pass

def getDefaultPropertyValue(machine, propID):
	startAddress = machine.header.objectTable
	propValue = machine.readWord(startAddress + (propID-1) * 2)
	return propValue

class Property:
	def __init__(self, machine, addr):
		self.machine = machine
		self.addr = addr
		self.addrValue = addr + 1
		self.totalLength = 1
		self.value = None

		self.size =  machine.readByte(addr)
		if self.size == 0:
			return

		decoded = False
		if machine.header.version < 4:
			if self.size & 0x80:
				size2 = machine.readByte(addr + 1)
				self.propId = self.size & 0x1f
				self.size = size2 & 0x1f
				self.addrValue = addr + 2
				self.totalLength = 2
				decoded = True

		if not decoded:
			self.propId = self.size & 0x1F
			self.size = (self.size>>5) +1

		self.totalLength += self.size


	def getValue(self):
		ad = self.addr + 1
		if self.value == None:
			pval = []
			for i in range(self.size):
				pval.append(self.machine.readByte(ad+i))

			self.value = pval

		if len(self.value) == 1:
			return self.value[0]

		return (self.value[0] << 8) | self.value[1]

	def setValue(self, value):
		if self.size == 1:
			self.machine.writeByte(self.addr + 1, value&0xff)
		
		elif self.size == 2:
			self.machine.writeByte(self.addr + 1, (value>>8)&0xff)
			self.machine.writeByte(self.addr + 2, value&0xff)

		else:
			explodeThis()

		self.value = None
		newVal = self.getValue()
		pass

class Object:
	def __init__(self,machine, offset, id):
		self.offset = offset
		self.machine = machine
		self.id = id
		if machine.header.version < 4:
			self.attr = (machine.readByte(offset) << 24) | (machine.readByte(offset+1) << 16) | (machine.readByte(offset+2) << 8) | (machine.readByte(offset+3))
			#self.attr = [machine.readByte(offset),machine.readByte(offset+1),machine.readByte(offset+2),machine.readByte(offset+3)]
			self.parentId = machine.readByte(offset+4)
			self.siblingId = machine.readByte(offset+5)
			self.childId = machine.readByte(offset+6)
			prop = machine.readWord(offset+7)

			propHeaderLength = machine.readByte(prop+0)
			l, self.propHeaderStr = zscii.decodeString(machine, prop + 1)

			ad = prop + 1 + l
		else:
			self.attr = (machine.readByte(offset) << 40) | (machine.readByte(offset+1) << 32) | (machine.readByte(offset+2) << 24) | (machine.readByte(offset+3) << 16) | (machine.readByte(offset+4) << 8) | (machine.readByte(offset+5))
			#self.attr = [machine.readByte(offset),machine.readByte(offset+1),machine.readByte(offset+2),machine.readByte(offset+3),machine.readByte(offset+4),machine.readByte(offset+5)]
			self.parentId = machine.readWord(offset+6)
			self.siblingId = machine.readWord(offset+8)
			self.childId = machine.readWord(offset+10)
			prop = machine.readWord(offset+12)

			propHeaderLength = machine.readByte(prop+0)
			l, self.propHeaderStr = zscii.decodeString(machine, prop + 1)

			ad = prop + 1 + l
		self.properties = {}
		while True:
			prop = Property(machine, ad)
			if prop.size == 0:
				break

			self.properties[prop.propId] = prop
			ad += prop.totalLength
			continue

		pass

	def hasAttr(self, attr):
		if self.machine.header.version < 4:
			bit = 31 - attr
		else:
			bit = 47 - attr

		return ((self.attr >> bit) & 1) == 1

	def clearAttr(self, attr):
		self.setAttrOnOff(attr, False)
		pass

	def setAttr(self, attr):
		self.setAttrOnOff(attr, True)
		pass

	def setAttrOnOff(self, attr, on):
		if self.machine.header.version < 4:
			bit = 31 - attr
		else:
			bit = 47 - attr

		oldAttr = self.attr
		a1 = self.hasAttr(attr)

		if on:
			setBit = 1 << bit
			self.attr |= setBit
		else:
			clearBit = ~(1 << bit)
			self.attr &= clearBit

		if self.machine.header.version < 4:
			count = 4
		else:
			count = 6

		for i in range(count):
			invI = count-1-i
			self.machine.writeByte(self.offset+i, ((self.attr)>>(invI*8)) & 0xff)

		self.attr = (self.machine.readByte(self.offset) << 24) | (self.machine.readByte(self.offset+1) << 16) | (self.machine.readByte(self.offset+2) << 8) | (self.machine.readByte(self.offset+3))
		a2 = self.hasAttr(attr)
		pass

	def getProp(self, propID):
		if propID in self.properties:
			return self.properties[propID].getValue()

		return getDefaultPropertyValue(self.machine, propID)

	def getPropAddr(self, propID):
		if propID in self.properties:
			return self.properties[propID].addr

		return 0

	def setProp(self, propID, value):
		self.properties[propID].setValue(value)
		pass

	def insertObject(self, other):
		oldChildId = self.childId
		other.setSibling(oldChildId)
		self.setChild(other.id)
		other.setParent(self.id)

		pass

	def setParent(self, parent):
		self.parentId = parent
		self.machine.writeByte(self.offset+4, self.parentId)
		pass

	def setSibling(self, sibling):
		self.siblingId = sibling
		self.machine.writeByte(self.offset+5, self.siblingId)
		pass

	def setChild(self, child):
		self.childId = child
		self.machine.writeByte(self.offset+6, self.childId)
		pass

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return 'Object: #{0} {1}'.format(self.id, self.propHeaderStr)


class ObjectTable:
	def __init__(self, machine):
		self.startAddress = machine.header.objectTable
		self.numProperties = 31
		if machine.header.version > 3:
			self.numProperties = 63

		self.objectTableStart = self.startAddress + self.numProperties * 2

		o = Object(machine, self.objectTableStart)
		pass
	pass