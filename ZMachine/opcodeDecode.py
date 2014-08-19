from enum import Enum
#from opcodeList import opCodesExt

class VarType(Enum):
	LongConstant = 0
	ShortConstant = 1
	Variable = 2

def parseVariable(machine, value):
	value = makeUnsigned(value, 1)
	if value==0:
		return StackValue(machine.currentScope.stack)
	elif value < 16:
		return LocalValue(machine.currentScope.locals, value-1)
	else:
		return GlobalValue(machine, value-16)

def decodeJump(machine):
	startAddress = machine.pc
	v1 = machine.readBytePC()
	cond = False
	if v1 >> 7 == 1:
		cond = True

	target = v1 & 0x3F
	if (v1 >> 6) & 1 == 0:
		target = target << 8
		v2 = machine.readBytePC()
		target |= v2
	
	if target > 0x2000: # negative jump
		target -= 0x4000

	if target > 1 or target < 0:
		startAddress = machine.pc-2
		target += startAddress
	return cond, target

def makeSigned(value, bytes = 2):
	value = makeUnsigned(value, bytes)
	shift = bytes * 8 - 1
	if (value >> shift) == 1:
		mask = 1 << (bytes * 8)
		value = value - mask

	return value

def makeUnsigned(value, bytes = 2):
	mask = (1 << (bytes * 8)) -1

	return value & mask

class ConstValue:
	def __init__(self, value, bytes):
		self.value = makeSigned(value, bytes)

	def load(self):
		return self.value

	def store(self, value):
		explodeThis()

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return 'ConstValue: #{0}'.format(hex(self.value))

class StackValue:
	def __init__(self, stack):
		self.stack = stack
		#print('StackValue.__init__', self.stack, id(stack), id(self.stack))

	def load(self):
		#print('StackValue.load', self.stack, id(self.stack))
		if len(self.stack) < 1:
			#print('LOAD FROM EMPTY STACK!')
			return 0

		return self.stack.pop()

	def store(self, value):
		#print('StackValue.store:', self.stack, hex(value), 'id:', id(self.stack))
		self.stack.append(makeSigned(value, 2))
		#print('StackValue.store:', self.stack)
		pass

	def storeB(self, value):
		return self.store(makeSigned(value, 1))

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		if len(self.stack) < 1:
			return 'StackValue: SP(empty), id:{0}'.format(id(self.stack))
		return 'StackValue: SP({0}), id:{1}'.format(hex(self.stack[-1]), id(self.stack))

class LocalValue:
	def __init__(self, locals, offset):
		self.locals = locals
		self.offset = offset

	def load(self):
		try:
			return self.locals[self.offset]
		except:
			#print("")
			return 0;

	def store(self, value, bytes = 2):
		self.locals[self.offset] = makeSigned(value, bytes)

	def storeB(self, value):
		self.store(value, 1)

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		try:
			return 'LocalValue: L{0}({1})'.format(hex(self.offset), hex(self.locals[self.offset]))
		except:
			#print("")
			pass

class GlobalValue:
	def __init__(self, machine, offset):
		self.machine = machine
		self.offset = offset

	def load(self):
		return makeSigned(self.machine.readWord(self.machine.header.globals + self.offset*2))

	def store(self, value):
		return self.machine.writeWord(self.machine.header.globals + self.offset*2, makeUnsigned(value))

	def storeB(self, value):
		return self.machine.writeWord(self.machine.header.globals + self.offset*2, makeUnsigned(value, 1))

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return 'GlobalValue: G{0}({1})'.format(hex(self.offset), hex(self.load()))

def decodeArgTypes(argType):
	bitstring = bin(argType)[2:].rjust(8, '0')
	args = []
	for i in [0,2,4,6]:
		subTypeString = bitstring[i:i+2]
		subType = None
		if subTypeString == '00':
			subType = VarType.LongConstant
		elif subTypeString == '01':
			subType = VarType.ShortConstant
		elif subTypeString == '10':
			subType = VarType.Variable

		if subType != None:
			args.append(subType)

	#print(bitstring, args)
	return args

class Opcode():
	def __init__(self, machine):
		self.machine = machine
		pass

class Opcode_SC_SC(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readBytePC(), 1)
		v2 = ConstValue(machine.readBytePC(), 1)
		self.argVals = [v1,v2]

class Opcode_SC_V(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readBytePC(), 1)
		variable = machine.readBytePC()
		v2 = parseVariable(machine, variable)

		self.argVals = [v1,v2]

		pass

class Opcode_V_SC(Opcode):
	def decode(self, machine):
		variable = machine.readBytePC()
		v1 = parseVariable(machine, variable)
		v2 = ConstValue(machine.readBytePC(), 1)

		self.argVals = [v1,v2]

		pass

class Opcode_V_V(Opcode):
	def decode(self, machine):
		variable = machine.readBytePC()
		v1 = parseVariable(machine, variable)

		variable = machine.readBytePC()
		v2 = parseVariable(machine, variable)

		self.argVals = [v1,v2]

		pass

class Opcode_LC(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readWordPC(), 2)
		self.argVals = [v1]


class Opcode_SC(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readBytePC(), 1)
		self.argVals = [v1]


class Opcode_V(Opcode):
	def decode(self, machine):
		variable = machine.readBytePC()
		v1 = parseVariable(machine, variable)
		self.argVals = [v1]


		pass

class Opcode_N(Opcode):
	def decode(self, machine):
		pass


class Opcode_2OP_VAR(Opcode):
	def decode(self, machine):
		v1 = machine.readBytePC()
		v2 = machine.readBytePC()
		v3 = machine.readBytePC()
		v4 = machine.readBytePC()

		pass

class Opcode_VAR(Opcode):
	def decode(self, machine):
		argType1 = machine.readBytePC()
		args = decodeArgTypes(argType1)

		self.argVals = []
		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.argVals.append(ConstValue(var, 2))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var, 1))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.argVals.append(parseVariable(machine, var))

		pass

class Opcode_VAR2(Opcode):
	def decode(self, machine):
		argVals = []
		argType1 = machine.readBytePC()
		argType2 = machine.readBytePC()

		args = decodeArgTypes(argType1)

		self.argVals = []
		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.argVals.append(ConstValue(var, 2))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var, 1))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.argVals.append(parseVariable(machine, var))

		args = decodeArgTypes(argType2)

		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.argVals.append(ConstValue(var, 2))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var, 1))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.argVals.append(parseVariable(machine, var))

		pass



class Opcode_Extended(Opcode):
	def decode(self, machine):
		opCode = machine.readBytePC()
		
		self.op = self.opCodesExt[opCode]()

		argType1 = machine.readBytePC()
		args = decodeArgTypes(argType1)

		self.op.machine = machine
		self.op.argVals = []

		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.op.argVals.append(ConstValue(var, 2))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.op.argVals.append(ConstValue(var, 1))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.op.argVals.append(parseVariable(machine, var))


		pass
	def call(self, machine):
		self.op.call(machine)
		pass
