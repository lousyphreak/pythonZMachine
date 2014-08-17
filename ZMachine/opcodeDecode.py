from enum import Enum


class VarType(Enum):
	LongConstant = 0
	ShortConstant = 1
	Variable = 2

def parseVariable(machine, value):
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
		target << 6
		v2 = machine.readBytePC()
		target |= v2
	
	if target > 1:
		startAddress = machine.pc-2
		t14 = target >> 14
		t13 = target >> 13
		t12 = target >> 12
		t11 = target >> 11
		if target > 5000:
			target = 65536 - target
		target += startAddress
	return cond, target

class ConstValue:
	def __init__(self, value):
		self.value = value

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
		print('StackValue.__init__', self.stack, id(stack), id(self.stack))

	def load(self):
		print('StackValue.load', self.stack, id(self.stack))
		return self.stack.pop()

	def store(self, value):
		print('StackValue.store:', self.stack, hex(value), 'id:', id(self.stack))
		self.stack.append(value)
		print('StackValue.store:', self.stack)
		pass

	def storeB(self, value):
		return self.store(value)

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
		return self.locals[self.offset]

	def store(self, value):
		self.locals[self.offset] = value

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return 'LocalValue: L{0}({1})'.format(hex(self.offset), hex(self.locals[self.offset]))

class GlobalValue:
	def __init__(self, machine, offset):
		self.machine = machine
		self.offset = offset

	def load(self):
		return self.machine.readWord(self.machine.header.globals + self.offset*2)

	def store(self, value):
		return self.machine.writeWord(self.machine.header.globals + self.offset*2, value)

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
		v1 = ConstValue(machine.readBytePC())
		v2 = ConstValue(machine.readBytePC())
		self.argVals = [v1,v2]

class Opcode_SC_V(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readBytePC())
		variable = machine.readBytePC()
		v2 = parseVariable(machine, variable)

		self.argVals = [v1,v2]

		pass

class Opcode_V_SC(Opcode):
	def decode(self, machine):
		variable = machine.readBytePC()
		v1 = parseVariable(machine, variable)
		v2 = ConstValue(machine.readBytePC())

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
		v1 = ConstValue(machine.readWordPC())
		self.argVals = [v1]


class Opcode_SC(Opcode):
	def decode(self, machine):
		v1 = ConstValue(machine.readBytePC())
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
				self.argVals.append(ConstValue(var))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var))
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

		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.argVals.append(ConstValue(var))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.argVals.append(parseVariable(machine, variable))

		args = decodeArgTypes(argType2)

		for arg in args:
			if arg is VarType.LongConstant:
				var = machine.readWordPC()
				self.argVals.append(ConstValue(var))
			if arg is VarType.ShortConstant:
				var = machine.readBytePC()
				self.argVals.append(ConstValue(var))
			if arg is VarType.Variable:
				var = machine.readBytePC()
				self.argVals.append(parseVariable(machine, variable))

		pass

