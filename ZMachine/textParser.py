import zscii

class DecodedWord:
	address = 0
	numChars = 0
	textPos = 0

	def __init__(self, address, numChars, textPos):
		self.address = address
		self.numChars = numChars
		self.textPos = textPos

class DictionaryWord:
	word = ''
	address = 0

	def __init__(self, address, word):
		self.address = address
		self.word = word

class TextWord:
	word = ''
	offset = 0

	def __init__(self, word, offset):
		self.word = word
		self.offset = offset

def split(text, separators):
	currentWord = ''
	currentWordStart = 0
	words = []

	for i in range(len(text)):
		char = text[i]
		if ord(char) in separators:
			words.append(TextWord(currentWord, currentWordStart))
			words.append(TextWord(str(char), i))
			currentWord = ''
			currentWordStart = i + 1
			continue
		elif char == ' ':
			words.append(TextWord(currentWord, currentWordStart))
			currentWord = ''
			currentWordStart = i + 1
			continue
		else:
			currentWord += char

	if len(currentWord) > 0:
		words.append(TextWord(currentWord, currentWordStart))

	return words

def parse(machine, text):
	offset = machine.header.dict

	numSeparators = machine.readByte(offset)
	offset += 1
	separators = []
	for i in range(numSeparators):
		separators.append(machine.readByte(offset))
		offset += 1

	entryLength = machine.readByte(offset)
	offset += 1
	numEntries = machine.readWord(offset)
	offset += 2

	entries = []
	for i in range(numEntries):
		length, str = zscii.decodeString(machine, offset)
		entries.append(DictionaryWord(offset, str))
		offset += entryLength

	words = split(text, separators)

	parsedWords = []
	for word in words:
		foundEntry = None
		for entry in entries:
			if entry.word == word.word:
				foundEntry = entry
				break
		if foundEntry is not None:
			parsedWords.append(DecodedWord(entry.address, len(word.word), word.offset))
		else:
			parsedWords.append(DecodedWord(0, len(word.word), word.offset))

	return parsedWords

def init(machine):
	offset = machine.header.dict

	numSeparators = machine.readByte(offset)
	offset += 1
	separators = []
	for i in range(numSeparators):
		separators.append(machine.readByte(offset))
		offset += 1

	entryLength = machine.readByte(offset)
	offset += 1
	numEntries = machine.readWord(offset)
	offset += 2

	entries = []
	for i in range(numEntries):
		len, str = zscii.decodeString(machine, offset)
		offset += entryLength
		entries.append(str)
	pass