from opcodeDecode import *
import objects
import zscii
import random
import sys


################################
# Two-operand opcodes
################################
class Opcode_Je():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('Je',self.argVals,cond,target)

		v1 = self.argVals[0].load()

		matching = False
		for v in self.argVals[1:]:
			v2 = v.load()
			if (v1==v2):
				matching = True
				break

		if matching == cond:
			machine.jump(target)

		pass
	pass

class Opcode_Jl():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('Jl',self.argVals,cond,target)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		if (v1<v2) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_Jg():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('Jg',self.argVals,cond,target)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		if (v1>v2) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_DecChk():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('DecChk', self.argVals,cond,target)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		ret = parseVariable(machine, v1)
		val = ret.load()
		val -= 1
		ret.store(val)

		if (val < v2) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_IncChk():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('IncChk', self.argVals, cond, target)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		ret = parseVariable(machine, v1)
		val = ret.load()
		val += 1
		ret.store(val)

		if (val > v2) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_Jin():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		objectA = machine.getObject(v1)
		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('Jin',objectA,v2,cond)
		if (objectA.parentId == v2) == cond:
			machine.jump(target)
	pass

class Opcode_Test():
	def call(self, machine):
		cond, target = decodeJump(machine)

		bitmap = self.argVals[0].load()
		flags = self.argVals[1].load()

		if ((bitmap & flags) == flags) == cond:
			machine.jump(target)
		pass
	pass

class Opcode_Or():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('Or', v1, v2, ret)

		value = v1 | v2
		ret.store(value)

		pass
	pass

class Opcode_And():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('And', v1, v2, ret)

		value = v1 & v2
		ret.store(value)

		pass
	pass

class Opcode_TestAttr():
	def call(self, machine):
		cond, target = decodeJump(machine)
		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('TestAttr {0} {1}'.format(self.argVals[0], self.argVals[1]))
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		object = machine.getObject(v1)
		attr = object.hasAttr(v2)
		machine.printDebug('object.attr {0}.{1}'.format(object, attr))

		if attr == cond:
			machine.jump(target)

		pass
	pass

class Opcode_SetAttr():
	def call(self, machine):
		objectId = self.argVals[0].load()
		attribute = self.argVals[1].load()

		object = self.machine.getObject(objectId)
		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('SetAttr', object, attribute)

		object.setAttr(attribute)
		pass
	pass

class Opcode_ClearAttr():
	def call(self, machine):
		objectId = self.argVals[0].load()
		attribute = self.argVals[1].load()

		object = self.machine.getObject(objectId)
		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('ClearAttr', object, attribute)

		object.clearAttr(attribute)
		pass
	pass

class Opcode_Store():
	def call(self, machine):
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		var = parseVariable(machine, v1)

		machine.printDebug('Store',var, v2)
		var.store(v2)
		pass
	pass

class Opcode_InsertObj():
	def call(self, machine):
		objectId = self.argVals[0].load()
		destinationId = self.argVals[1].load()

		object = machine.getObject(objectId)
		destination = machine.getObject(destinationId)

		machine.printDebug('===================================================================================')
		machine.printDebug('InsertObj', object, 'into', destination)
		#machine.printScreen("InsertObj {0} {1}".format(objectId, destinationId))
		destination.insertObject(object)

		pass
	pass

class Opcode_LoadW():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = machine.readWord(arrAddr+index*2)

		machine.printDebug('LoadW', self.argVals, value, ret)

		ret.store(value)
		pass
	pass

class Opcode_LoadB():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = machine.readByte(arrAddr+index)

		machine.printDebug('LoadB', self.argVals, value, ret)

		ret.store(value&0xff)
		pass
	pass

class Opcode_GetProp():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		property = self.argVals[1].load()

		object = machine.getObject(objectId)
		propVal = object.getProp(property)
		machine.printDebug('GetProp', object, property, propVal)

		ret.store(propVal)
		pass
	pass

class Opcode_GetPropAddr():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		property = self.argVals[1].load()

		object = machine.getObject(objectId)

		addr = object.getPropAddr(property)

		machine.printDebug('GetPropAddr', object, property, addr)

		ret.store(addr)
		pass
	pass

class Opcode_GetNextProp():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		property = self.argVals[1].load()

		object = machine.getObject(objectId)
		machine.printDebug('GetNextProp', object, property, ret)

		nextProp = object.getNextProp(property)
		ret.store(nextProp)
		pass
	pass

class Opcode_Add():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('Add', v1, v2, ret)

		value = v1 + v2
		ret.store(value)

	pass

class Opcode_Sub():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('Sub', v1, v2, ret)

		value = v1 - v2
		ret.store(value)
	pass

class Opcode_Mul():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('Mul', v1, v2, ret)

		value = v1 * v2
		ret.store(value)
	pass

class Opcode_Div():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('Div', v1, v2, ret)

		value = int(v1 / v2)
		ret.store(value)
	pass

class Opcode_Mod():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		machine.printDebug('Mod', self.argVals, ret)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		value = v1 % v2

		if v1 < 0:
			if v2 < 0: # -13 % -5 = -2
				value = value
			else: # -13 % 5 = -2
				value = value - v2
		else:
			if v2 < 0: # 13 % -5 = 3
				value = value -v2
			else: # 13 % 5 = -2
				value = value

		ret.store(value)
	pass

class Opcode_Call2S():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('Call', self.argVals[0], self.argVals[1:], machine.pc, ret)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, ret)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_Call2N():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('Call', self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_SetColor():
	def call(self, machine):
		pass
	pass

class Opcode_Throw():
	def call(self, machine):
		pass
	pass

################################
# One-operand opcodes
################################

class Opcode_Jz():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		machine.printDebug('Jz',self.argVals,cond)

		if (v1==0) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_GetSibling():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		cond, target = decodeJump(machine)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('GetSibling', object, object.siblingId, ret)
		ret.store(object.siblingId)

		if (object.siblingId!=0) == cond:
			machine.jump(target)

		pass
	pass

class Opcode_GetChild():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		cond, target = decodeJump(machine)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('GetChild', object, object.childId, ret)
		ret.store(object.childId)

		if (object.childId!=0) == cond:
			machine.jump(target)
		pass
	pass

class Opcode_GetParent():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		machine.printDebug('---------------------------------------------------------------------------------------------------------------------')
		machine.printDebug('GetParent', object, object.parentId, ret)
		ret.store(object.parentId)

		pass
	pass

class Opcode_GetPropLen():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		propertyAddress = self.argVals[0].load()

		if propertyAddress == 0:
			machine.printDebug('GetPropLen 0', ret)
			ret.store(0)
		else:
			prop = objects.Property(machine, propertyAddress)
			machine.printDebug('GetPropLen', prop, prop.size, ret)

			ret.store(prop.size)
		pass
	pass

class Opcode_Inc():
	def call(self, machine):
		ret = parseVariable(machine, self.argVals[0].load())
		var = ret.load()
		machine.printDebug('Inc', ret)
		var += 1
		ret.store(var)
		pass
	pass

class Opcode_Dec():
	def call(self, machine):
		ret = parseVariable(machine, self.argVals[0].load())
		var = ret.load()
		machine.printDebug('Dec', ret)
		var -= 1
		ret.store(var)
		pass
	pass

class Opcode_PrintAddr():
	def call(self, machine):
		address = self.argVals[0].load()
		length, string = zscii.decodeString(machine, address)
		machine.printDebug('PrintPaddr', self.argVals, address, string)
		machine.printScreen(string)
		pass
	pass

class Opcode_Call1S():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('Call1S', self.argVals[0], self.argVals[1:], machine.pc, ret)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, ret)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_RemoveObj():
	def call(self, machine):
		v1 = self.argVals[0].load()
		object = machine.getObject(v1)
		parent = machine.getObject(object.parentId)

		machine.printDebug('===================================================================================')
		machine.printDebug('RemoveObj: object #{0}.{1}'.format(v1, object.propHeaderStr))
		#machine.printScreen("RemoveObj {0} {1}".format(v1, parent))
		object.removeObject()
		pass
	pass

class Opcode_PrintObj():
	def call(self, machine):
		v1 = self.argVals[0].load()
		object = machine.getObject(v1)
		#object.
		
		machine.printDebug('PrintObj: object #{0}.{1}'.format(v1, object.propHeaderStr))
		machine.printScreen(object.propHeaderStr)
		pass
	pass

class Opcode_Ret():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('Ret', self.argVals[0], machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		machine.printDebug('new pc:', hex(machine.currentScope.returnAddress))
		machine.printDebug('###############################')
		
		machine.ret(self.argVals[0])
		pass
	pass

class Opcode_Jump():
	def call(self, machine):
		target = self.argVals[0].load() - 2
		machine.printDebug('jump target value:', hex(target))
		target = (machine.pc + target) % 0x10000
		machine.printDebug('jump target:', hex(target))

		machine.jump(target)
		pass
	pass

class Opcode_PrintPaddr():
	def call(self, machine):
		pAddress = self.argVals[0].load()
		address = machine.unpackAddressPrint(pAddress)

		bytes, string = zscii.decodeString(machine, address)
		machine.printDebug('PrintPaddr', self.argVals, address, string)
		machine.printScreen(string)

		pass
	pass

class Opcode_Load():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = parseVariable(machine, self.argVals[0].load())

		ret.store(v1.load())
		pass
	pass

class Opcode_Not():
	def call(self, machine):
		if machine.header.version > 4:
			machine.printDebug('###############################')
			machine.printDebug('oldstack',id(machine.currentScope.stack))
			machine.printDebug('Call', self.argVals[0], [], machine.pc, None)
			machine.printDebug('###############################')
			machine.call(self.argVals[0], [], machine.pc, None)
			machine.printDebug('newstack',id(machine.currentScope.stack))

		else:
			variable = machine.readBytePC()
			ret = parseVariable(machine, variable)

			v1 = self.argVals[0].load()
			machine.printDebug('Not', v1, ret)

			value = ~v1&0xffff
			ret.store(value)
		pass
	pass

################################
# Zero-operand opcodes
################################

class Opcode_RTrue():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('RTrue', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		machine.printDebug('new pc:', hex(machine.currentScope.returnAddress))
		machine.printDebug('###############################')
		
		machine.ret(ConstValue(1, 1))
		pass
	pass

class Opcode_RFalse():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('RTrue', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		machine.printDebug('new pc:', hex(machine.currentScope.returnAddress))
		machine.printDebug('###############################')
		
		machine.ret(ConstValue(0, 1))
		pass
	pass

class Opcode_Print():
	def call(self, machine):
		bytes, string = zscii.decodeString(machine, machine.pc)
		machine.printScreen(string)
		machine.pc += bytes

		machine.printDebug('Print', string)
		pass
	pass

class Opcode_PrintRet():
	def call(self, machine):
		bytes, string = zscii.decodeString(machine, machine.pc)
		machine.printScreen(string)
		machine.printScreen("\n")
		machine.pc += bytes

		machine.printDebug('PrintRet', string)
		machine.ret(ConstValue(1, 1))
		pass
	pass

class Opcode_Nop():
	def call(self, machine):
		pass
	pass

class Opcode_Save():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_Restore():
	def call(self, machine):
		pass
	pass

class Opcode_Restart():
	def call(self, machine):
		pass
	pass

class Opcode_RetPopped():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('RetPopped', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		machine.printDebug('new pc:', hex(machine.currentScope.returnAddress))
		machine.printDebug('###############################')
		value = machine.currentScope.stack.pop()
		machine.ret(ConstValue(value, 1))
		pass
	pass

class Opcode_Pop():
	def call(self, machine):
		machine.printDebug('Pop')
		machine.currentScope.stack.pop()
		pass
	pass

class Opcode_Quit():
	def call(self, machine):
		sys.exit(0)
		pass
	pass

class Opcode_NewLine():
	def call(self, machine):
		machine.printScreen("\n")
		machine.printDebug('NewLine')
		pass
	pass

class Opcode_ShowStatus():
	def call(self, machine):
		pass
	pass

class Opcode_Verify():
	def call(self, machine):
		cond, target = decodeJump(machine)
		if True == cond:
			machine.jump(target)
		pass
	pass

class Opcode_Piracy():
	def call(self, machine):
		cond, target = decodeJump(machine)
		if True == cond:
			machine.jump(target)
		pass
	pass

################################
# Variable-operand opcodes
################################

class Opcode_Call():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)

		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('Call', self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass

class Opcode_StoreW():
	def call(self, machine):
		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = self.argVals[2].load()

		machine.printDebug('StoreW', arrAddr, index, value)
		machine.writeWord(arrAddr+index*2, value)

class Opcode_StoreB():
	def call(self, machine):
		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = self.argVals[2].load()

		machine.printDebug('StoreW', arrAddr, index, value)
		machine.writeByte(arrAddr+index, value)

class Opcode_PutProp():
	def call(self, machine):
		objectId = self.argVals[0].load()
		property = self.argVals[1].load()
		value = self.argVals[2].load()
		object = machine.getObject(objectId)
		#object.
		
		machine.printDebug('PutProp:', object, self.argVals)
		object.setProp(property, value)
		pass
	pass

class Opcode_SRead():
	def call(self, machine):
		if machine.header.version > 4:
			variable = machine.readBytePC()
			ret = parseVariable(machine, variable)
			ret.store(13)

		if machine.header.version < 4:
			machine.updateStatus()

		text = self.argVals[0].load()
		parse = self.argVals[1].load()

		machine.readCommand(text, parse)
		pass
	pass

class Opcode_PrintChar():
	def call(self, machine):
		v1 = self.argVals[0].load()
		
		if v1 == 0:
			t = '???'
		else:
			t = str(chr(v1))

		machine.printDebug('PrinChar', t)
		machine.printScreen(t)

		pass
	pass

class Opcode_PrintNum():
	def call(self, machine):
		v1 = self.argVals[0].load()
		t = str(v1)
		machine.printScreen(t)

		machine.printDebug('PrintNum', t)
		pass
	pass

class Opcode_Random():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		range = self.argVals[0].load()

		value = 0
		if range < 0:
			random.seed(-range)
		elif range == 0:
			random.seed()
		else:
			value = random.randint(1,range)

		ret.store(value)
		pass
	pass

class Opcode_Push():
	def call(self, machine):
		v1 = self.argVals[0].load()

		machine.printDebug('Push', self.argVals[0])
		machine.currentScope.stack.append(v1)
		pass
	pass

class Opcode_Pull():
	def call(self, machine):
		v1 = self.argVals[0].load()
		ret = parseVariable(machine, v1)
		val = machine.currentScope.stack.pop()

		machine.printDebug('Pull', ret, val)
		ret.store(val)
		pass
	pass

class Opcode_SplitWindow():
	def call(self, machine):
		pass
	pass

class Opcode_SetWindow():
	def call(self, machine):
		pass
	pass

class Opcode_CallVS2():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)

		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('CallVS2', self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_EraseWindow():
	def call(self, machine):
		pass
	pass

class Opcode_EraseLine():
	def call(self, machine):
		pass
	pass

class Opcode_SetCursor():
	def call(self, machine):
		pass
	pass

class Opcode_GetCursor():
	def call(self, machine):
		pass
	pass

class Opcode_SetTextStyle():
	def call(self, machine):
		pass
	pass

class Opcode_BufferMode():
	def call(self, machine):
		pass
	pass

class Opcode_OutputStream():
	def call(self, machine):
		pass
	pass

class Opcode_InputStream():
	def call(self, machine):
		pass
	pass

class Opcode_SoundEffect():
	def call(self, machine):
		pass
	pass

class Opcode_ReadChar():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_ScanTable():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Not_V5():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		machine.printDebug('Not', v1, ret)

		value = ~v1&0xffff
		ret.store(value)
		pass
	pass

class Opcode_CallVN():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('CallVN', self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_CallVN2():
	def call(self, machine):
		machine.printDebug('###############################')
		machine.printDebug('oldstack',id(machine.currentScope.stack))
		machine.printDebug('CallVN2', self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, None)
		machine.printDebug('newstack',id(machine.currentScope.stack))
		pass
	pass

class Opcode_Tokenise():
	def call(self, machine):
		pass
	pass

class Opcode_EncodeText():
	def call(self, machine):
		pass
	pass

class Opcode_CopyTable():
	def call(self, machine):
		pass
	pass

class Opcode_PrintTable():
	def call(self, machine):
		pass
	pass

class Opcode_CheckArgCount():
	def call(self, machine):
		cond, target = decodeJump(machine)

		machine.printDebug('CheckArgCount', self.argVals, machine.currentScope.numLocals)

		v1 = self.argVals[0].load()
		if (v1 <= machine.currentScope.numLocals) == cond:
			machine.jump(target)


		pass
	pass

################################
# Extended opcodes
################################

class Opcode_Save():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Restore():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_LogShift():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = makeUnsigned(self.argVals[0].load())
		v2 = self.argVals[1].load()
		machine.printDebug('LogShift', self.argVals, ret)

		if v2 < 0:
			value = v1 >> -v2
		else:
			value = v1 << v2

		value = makeSigned(value)
		if value == 170:
			machine.printDebug('')
		ret.store(value)
		pass
	pass

class Opcode_ArtShift():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		machine.printDebug('ArtShift', self.argVals, ret)

		if v2 < 0:
			value = v1 >> -v2
		else:
			value = v1 << v2

		value = makeSigned(value)
		if value == 170:
			machine.printDebug('')
		ret.store(value)
		pass
	pass

class Opcode_SetFont():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_DrawPicture():
	def call(self, machine):
		pass
	pass

class Opcode_PictureData():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_ErasePicture():
	def call(self, machine):
		pass
	pass

class Opcode_SetMargins():
	def call(self, machine):
		pass
	pass

class Opcode_SaveUndo():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_RestoreUndo():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_PrintUnicode():
	def call(self, machine):
		pass
	pass

class Opcode_CheckUnicode():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_SetTrueColor():
	def call(self, machine):
		pass
	pass

class Opcode_MoveWindow():
	def call(self, machine):
		pass
	pass

class Opcode_WindowSize():
	def call(self, machine):
		pass
	pass

class Opcode_WindowStyle():
	def call(self, machine):
		pass
	pass

class Opcode_GetWindowProp():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_ScrollWindow():
	def call(self, machine):
		pass
	pass

class Opcode_PopStack():
	def call(self, machine):
		pass
	pass

class Opcode_ReadMouse():
	def call(self, machine):
		pass
	pass

class Opcode_MouseWindow():
	def call(self, machine):
		pass
	pass

class Opcode_PushStack():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_PutWindowProp():
	def call(self, machine):
		pass
	pass

class Opcode_PrintForm():
	def call(self, machine):
		pass
	pass

class Opcode_MakeMenu():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_PictureTable():
	def call(self, machine):
		pass
	pass

class Opcode_BufferScreen():
	def call(self, machine):
		pass
	pass
