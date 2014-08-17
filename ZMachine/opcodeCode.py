from opcodeDecode import *
import zscii


################################
# Two-operand opcodes
################################
class Opcode_Je():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		print('Je',v1,v2,cond)

		if (v1==v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_Jl():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		print('Jl',v1,v2,cond)

		if (v1<v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_Jg():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		print('Jg',v1,v2,cond)

		if (v1>v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_DecChk():
	def call(self, machine):
		cond, target = decodeJump(machine)
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		print('DecChk', v1, v2)
		ret = parseVariable(machine, v1)
		val = ret.load()
		val -= 1
		ret.store(val)

		if (val < v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_IncChk():
	def call(self, machine):
		cond, target = decodeJump(machine)
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		ret = parseVariable(machine, v1)
		print('IncChk', self.argVals, ret)
		val = ret.load()
		val += 1
		ret.store(val)

		if (val > v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_Jin():
	def call(self, machine):
		cond, target = decodeJump(machine)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()

		objectA = machine.getObject(v1)
		print('---------------------------------------------------------------------------------------------------------------------')
		print('Jin',objectA,v2,cond)
		if (objectA.parentId == v2) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target
	pass

class Opcode_Test():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_Or():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Or', v1, v2, ret)

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
		print('And', v1, v2, ret)

		value = v1 & v2
		ret.store(value)

		pass
	pass

class Opcode_TestAttr():
	def call(self, machine):
		cond, target = decodeJump(machine)
		print('---------------------------------------------------------------------------------------------------------------------')
		print('TestAttr {0} {1}'.format(self.argVals[0], self.argVals[1]))
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		object = machine.getObject(v1)
		attr = object.hasAttr(v2)
		print('object.attr {0}.{1}'.format(object, attr))

		if attr == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_SetAttr():
	def call(self, machine):
		objectId = self.argVals[0].load()
		attribute = self.argVals[1].load()

		object = self.machine.getObject(objectId)
		print('---------------------------------------------------------------------------------------------------------------------')
		print('SetAttr', object, attribute)

		object.setAttr(attribute)
		pass
	pass

class Opcode_ClearAttr():
	def call(self, machine):
		pass
	pass

class Opcode_Store():
	def call(self, machine):
		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		var = parseVariable(machine, v1)

		print('Store',var, v2)
		var.store(v2)
		pass
	pass

class Opcode_InsertObj():
	def call(self, machine):
		objectId = self.argVals[0].load()
		destinationId = self.argVals[1].load()

		object = machine.getObject(objectId)
		destination = machine.getObject(destinationId)

		print('---------------------------------------------------------------------------------------------------------------------')
		print('insertObj', object, 'into', destination)
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

		print('LoadW', arrAddr, index, value, ret)

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

		print('LoadB', arrAddr, index, value, ret)

		ret.storeB(value)
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
		print('GetProp', object, property, propVal)

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

		pass
	pass

class Opcode_GetNextProp():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		property = self.argVals[1].load()

		object = machine.getObject(objectId)
		pass
	pass

class Opcode_Add():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Add', v1, v2, ret)

		value = v1 + v2
		ret.store(value)

	pass

class Opcode_Sub():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Sub', v1, v2, ret)

		value = v1 - v2
		ret.store(value)
	pass

class Opcode_Mul():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Mul', v1, v2, ret)

		value = v1 * v2
		ret.store(value)
	pass

class Opcode_Div():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Div', v1, v2, ret)

		value = v1 / v2
		ret.store(value)
	pass

class Opcode_Mod():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		v1 = self.argVals[0].load()
		v2 = self.argVals[1].load()
		print('Mod', v1, v2, ret)

		value = v1 % v2
		ret.store(value)
	pass

class Opcode_Call2S():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Call2N():
	def call(self, machine):
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
		print('Jz',self.argVals,cond)

		if (v1==0) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_GetSibling():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		cond, target = decodeJump(machine)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		print('---------------------------------------------------------------------------------------------------------------------')
		print('GetSibling', object, object.parentId, ret)
		ret.store(object.siblingId)

		if (object.siblingId==0) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target

		pass
	pass

class Opcode_GetChild():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		cond, target = decodeJump(machine)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		print('---------------------------------------------------------------------------------------------------------------------')
		print('GetChild', object, object.parentId, ret)
		ret.store(object.childId)

		if (object.childId==0) == cond:
			if target == 0:
				print('RFalse!')
				machine.ret(ConstValue(0))
				return

			print('jumping!')
			machine.pc = target
		pass
	pass

class Opcode_GetParent():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)

		objectId = self.argVals[0].load()
		object = machine.getObject(objectId)

		print('---------------------------------------------------------------------------------------------------------------------')
		print('GetParent', object, object.parentId, ret)
		ret.store(object.parentId)

		pass
	pass

class Opcode_GetPropLen():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Inc():
	def call(self, machine):
		pass
	pass

class Opcode_Dec():
	def call(self, machine):
		pass
	pass

class Opcode_PrintAddr():
	def call(self, machine):
		pass
	pass

class Opcode_Call1S():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_RemoveObj():
	def call(self, machine):
		pass
	pass

class Opcode_PrintObj():
	def call(self, machine):
		v1 = self.argVals[0].load()
		object = machine.getObject(v1)
		#object.
		
		print('PrintObj: object #{0}.{1}'.format(v1, object.propHeaderStr))
		machine.screen.print(object.propHeaderStr)
		pass
	pass

class Opcode_Ret():
	def call(self, machine):
		print('###############################')
		print('Ret', self.argVals[0], machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		print('new pc:', hex(machine.currentScope.returnAddress))
		print('###############################')
		
		machine.ret(self.argVals[0])
		pass
	pass

class Opcode_Jump():
	def call(self, machine):
		target = self.argVals[0].load() - 2
		print('jump target value:', hex(target))
		target = (machine.pc + target) % 0x10000
		print('jump target:', hex(target))

		machine.pc = target
		pass
	pass

class Opcode_PrintPaddr():
	def call(self, machine):
		pAddress = self.argVals[0].load()
		address = machine.unpackAddressPrint(pAddress)

		bytes, string = zscii.decodeString(machine, address)
		print('PrintPaddr', self.argVals, address, string)
		machine.screen.print(string)

		pass
	pass

class Opcode_Load():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Not():
	def call(self, machine):
		variable = machine.readBytePC()
		ret = parseVariable(machine, variable)
		pass
	pass

################################
# Zero-operand opcodes
################################

class Opcode_RTrue():
	def call(self, machine):
		print('###############################')
		print('RTrue', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		print('new pc:', hex(machine.currentScope.returnAddress))
		print('###############################')
		
		machine.ret(ConstValue(1))
		pass
	pass

class Opcode_RFalse():
	def call(self, machine):
		print('###############################')
		print('RTrue', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		print('new pc:', hex(machine.currentScope.returnAddress))
		print('###############################')
		
		machine.ret(ConstValue(0))
		pass
	pass

class Opcode_Print():
	def call(self, machine):
		bytes, string = zscii.decodeString(machine, machine.pc)
		machine.screen.print(string)
		machine.pc += bytes

		print('Print', string)
		pass
	pass

class Opcode_PrintRet():
	def call(self, machine):
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
		print('###############################')
		print('RetPopped', machine.currentScope.returnValue, id(machine.currentScope.returnValue))
		print('new pc:', hex(machine.currentScope.returnAddress))
		print('###############################')
		value = machine.currentScope.stack.pop()
		machine.ret(ConstValue(value))
		pass
	pass

class Opcode_Pop():
	def call(self, machine):
		pass
	pass

class Opcode_Quit():
	def call(self, machine):
		pass
	pass

class Opcode_NewLine():
	def call(self, machine):
		machine.screen.print("\n")
		print('NewLine')
		pass
	pass

class Opcode_ShowStatus():
	def call(self, machine):
		pass
	pass

class Opcode_Verify():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

class Opcode_Extended():
	def call(self, machine):
		pass
	pass

class Opcode_Piracy():
	def call(self, machine):
		cond, target = decodeJump(machine)
		pass
	pass

################################
# Variable-operand opcodes
################################

class Opcode_Call():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)

		print('###############################')
		print('oldstack',id(machine.currentScope.stack))
		print('Call', self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		print('###############################')
		machine.call(self.argVals[0], self.argVals[1:], machine.pc, self.ret)
		print('newstack',id(machine.currentScope.stack))
		pass

class Opcode_StoreW():
	def call(self, machine):
		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = self.argVals[2].load()

		print('StoreW', arrAddr, index, value)
		machine.writeWord(arrAddr+index*2, value)

class Opcode_StoreB():
	def call(self, machine):
		arrAddr = self.argVals[0].load()
		index = self.argVals[1].load()
		value = self.argVals[2].load()

		print('StoreW', arrAddr, index, value)
		machine.writeByte(arrAddr+index, value)

class Opcode_PutProp():
	def call(self, machine):
		objectId = self.argVals[0].load()
		property = self.argVals[1].load()
		value = self.argVals[2].load()
		object = machine.getObject(objectId)
		#object.
		
		print('PutProp:', object, self.argVals)
		object.setProp(property, value)
		pass
	pass

class Opcode_SRead():
	def call(self, machine):
		pass
	pass

class Opcode_PrintChar():
	def call(self, machine):
		v1 = self.argVals[0].load()
		
		if v1 == 0:
			t = '???'
		else:
			t = str(chr(v1))

		print('PrinChar', t)
		machine.screen.print(t)

		pass
	pass

class Opcode_PrintNum():
	def call(self, machine):
		v1 = self.argVals[0].load()
		t = str(v1)
		machine.screen.print(t)

		print('PrintNum', t)
		pass
	pass

class Opcode_Random():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_Push():
	def call(self, machine):
		v1 = self.argVals[0].load()

		print('Push', self.argVals[0])
		machine.currentScope.stack.append(v1)
		pass
	pass

class Opcode_Pull():
	def call(self, machine):
		v1 = self.argVals[0].load()
		ret = parseVariable(machine, v1)
		val = machine.currentScope.stack.pop()

		print('Pull', ret, val)
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

class Opcode_Not():
	def call(self, machine):
		variable = machine.readBytePC()
		self.ret = parseVariable(machine, variable)
		pass
	pass

class Opcode_CallVN():
	def call(self, machine):
		pass
	pass

class Opcode_CallVN2():
	def call(self, machine):
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
		pass
	pass

################################
# Extended opcodes
################################

class Opcode_Save():
	def call(self, machine):
		pass
	pass

class Opcode_Restore():
	def call(self, machine):
		pass
	pass

class Opcode_LogShift():
	def call(self, machine):
		pass
	pass

class Opcode_ArtShift():
	def call(self, machine):
		pass
	pass

class Opcode_SetFont():
	def call(self, machine):
		pass
	pass

class Opcode_DrawPicture():
	def call(self, machine):
		pass
	pass

class Opcode_PictureData():
	def call(self, machine):
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
		pass
	pass

class Opcode_RestoreUndo():
	def call(self, machine):
		pass
	pass

class Opcode_PrintUnicode():
	def call(self, machine):
		pass
	pass

class Opcode_CheckUnicode():
	def call(self, machine):
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
