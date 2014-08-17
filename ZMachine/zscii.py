
charTable0 = 'abcdefghijklmnopqrstuvwxyz'
charTable1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
charTable2 = " \n0123456789.,!?_#'\"/\\-:()"
charTable = [charTable0, charTable1, charTable2]

def decode10Bit(machine, tenBit):
	if tenBit == 8: # delete ? 
		return "??delete??"
	elif tenBit == 9: # tab (V6)
		return "\t"
	elif tenBit == 11: # sentence space (V6)
		return "  "
	elif tenBit == 13: # newline
		return "\n"
	elif tenBit == 27: # escape
		return "??escape??"
	elif tenBit >= 32 and tenBit <= 126: #  standard ASCII
		return str(chr(tenBit))
	pass

def decodeString(machine, startOffset):
	finished = False
	address = startOffset
	retString = ''

	chars = []
	while not finished:
		w = machine.readWord(address)
		upperBit = w >> 15
		if upperBit != 0:
			finished = True

		a = (w >> 10) & 0x1f
		b = (w >> 5) & 0x1f
		c = (w >> 0) & 0x1f
		chars.append(a)
		chars.append(b)
		chars.append(c)

		address+=2

	currentMap = 0
	currentTemp = None
	synonym = None
	tenBit = None

	for c in chars:
		if synonym is not None:
			offset = (synonym * 32 + c) * 2
			synAddress = machine.readWord(machine.header.abbrev + offset)*2
			unused, synstr = decodeString(machine, synAddress)
			retString+=synstr
			synonym = None
			continue

		if tenBit == 0:
			tenBitChar = c << 5
			tenBit = 1
			continue
		if tenBit == 1:
			tenBitChar |= c
			retString += decode10Bit(machine, tenBitChar)
			tenBit = None
			continue

		if machine.header.version < 3:
			if c == 0:
				retString+=" "
				continue
			if c == 1:
				if machine.header.version == 2:
					synonym = 0
				else:
					retString+="\n"
				continue
			if c == 2:
				if currentTemp is not None:
					currentTemp = (currentTemp+1)%3
				currentTemp = (currentMap+1)%3
				continue
			if c == 3:
				if currentTemp is not None:
					currentTemp = (currentTemp-1)%3
				currentTemp = (currentMap-1)%3
				continue
			if c == 4:
				currentMap = (currentMap+1)%3
				continue
			if c == 5:
				currentMap = (currentMap-1)%3
				continue
		else:
			if c == 0:
				retString+=" "
				continue
			if c == 1:
				synonym = 0
				continue
			if c == 2:
				synonym = 1
				continue
			if c == 3:
				synonym = 2
				continue
			if c == 4:
				if currentTemp is not None:
					currentTemp = (currentTemp+1)%3
				currentTemp = (currentMap+1)%3
				continue
			if c == 5:
				if currentTemp is not None:
					currentTemp = (currentTemp-1)%3
				currentTemp = (currentMap-1)%3
				continue

		map = currentMap
		if currentTemp is not None:
			map = currentTemp
			currentTemp = None

		if map == 2 and c == 6:
			tenBit = 0
			continue

		retString += charTable[map][c-6]
		#print(charTable[map][c-6], end="")
		#print(charTable[map][c-6])

	
	return address - startOffset, retString
