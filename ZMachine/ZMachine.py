from struct import unpack, pack
from enum import Enum

# http://inform-fiction.org/zmachine/standards/z1point0/sect11.html


class VarType(Enum):
    LongConstant = 0
    ShortConstant = 1
    Variable = 2

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
        self.v1 = ConstValue(machine.readBytePC())
        self.v2 = ConstValue(machine.readBytePC())

class Opcode_SC_V(Opcode):
    def decode(self, machine):
        self.v1 = ConstValue(machine.readBytePC())
        variable = machine.readBytePC()
        self.v2 = parseVariable(machine, variable)

        pass

class Opcode_V_SC(Opcode):
    def decode(self, machine):
        variable = machine.readBytePC()
        self.v1 = parseVariable(machine, variable)
        self.v2 = ConstValue(machine.readBytePC())

        pass

class Opcode_V_V(Opcode):
    def decode(self, machine):
        variable = machine.readBytePC()
        self.v1 = parseVariable(machine, variable)

        variable = machine.readBytePC()
        self.v2 = parseVariable(machine, variable)

        pass

class Opcode_LC(Opcode):
    def decode(self, machine):
        self.v1 = ConstValue(machine.readWordPC())

class Opcode_SC(Opcode):
    def decode(self, machine):
        self.v1 = ConstValue(machine.readBytePC())

class Opcode_V(Opcode):
    def decode(self, machine):
        variable = machine.readBytePC()
        self.v1 = parseVariable(machine, variable)

        pass

class Opcode_N(Opcode):
    def decode(self, machine):
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

def opAdd(machine, v1, v2, ret):
    sum = v1.load()+v2.load()
    ret.store(sum)

    pass

class Opcode_Add_V_SC(Opcode_V_SC):
    def call(self, machine):
        variable = machine.readBytePC()
        ret = parseVariable(machine, variable)

        opAdd(machine, self.v1, self.v2, ret)
        pass

class Opcode_Add_V_V(Opcode_V_V):
    def call(self, machine):
        variable = machine.readBytePC()
        ret = parseVariable(machine, variable)

        opAdd(machine, self.v1, self.v2, ret)
        pass

class Opcode_Call(Opcode_VAR):
    def call(self, machine):
        variable = machine.readBytePC()
        self.ret = parseVariable(machine, variable)
        machine.call(self.argVals[0], self.argVals[1:])
        pass

class Opcode_StoreW(Opcode_VAR):
    def call(self, machine):
        self.argVals[0].storeOffset(self.argVals[2].load(), self.argVals[1].load())
        pass

class Opcode_StoreB(Opcode_VAR):
    def call(self, machine):
        self.argVals[0].storeOffsetB(self.argVals[2].load(), self.argVals[1].load())
        pass



opCodes = [0] * 256

opCodes[84] = Opcode_Add_V_SC
opCodes[116] = Opcode_Add_V_V
opCodes[224] = Opcode_Call
opCodes[225] = Opcode_StoreW
opCodes[226] = Opcode_StoreB

class RoutineScope:
    def __init__(self, machine, parent, address, locals):
        self.parent = parent

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
        for i in range(len(locals)):
            self.locals[i] = locals[i].load()

        self.stack = []
        self.startAddress = address

def parseVariable(machine, value):
    if value==0:
        return StackValue(machine.currentScope.stack)
    elif value < 16:
        return LocalValue(machine.currentScope.locals, value-1)
    else:
        return GlobalValue(machine, value-16)

class ConstValue:
    def __init__(self, value):
        self.value = value

    def load(self):
        return self.value

    def store(self, value):
        explodeThis()

class StackValue:
    def __init__(self, stack):
        self.stack = stack

    def load(self):
        return self.stack.pop()

    def store(self, value):
        self.stack.append(value)

class LocalValue:
    def __init__(self, locals, offset):
        self.locals = locals
        self.offset = offset

    def load(self):
        return self.locals[self.offset]

    def store(self, value):
        self.locals[self.offset] = value

class GlobalValue:
    def __init__(self, machine, offset):
        self.machine = machine
        self.offset = offset

    def load(self):
        return self.loadOffset(0)

    def store(self, value):
        return self.storeOffset(value, 0)

    def loadOffset(self, offset):
        return self.machine.readWord(self.machine.header.globals + self.offset*2 + offset)

    def storeOffset(self, value, offset):
        return self.machine.writeWord(self.machine.header.globals + self.offset*2 + offset, value)

    def loadOffsetB(self, offset):
        return self.machine.readByte(self.machine.header.globals + self.offset*2 + offset)

    def storeOffsetB(self, value, offset):
        return self.machine.writeByte(self.machine.header.globals + self.offset*2 + offset, value)

class Header:
    def __init__(self, machine):
        self.version =              machine.readByte(0x00)
        self.flags1 =               machine.readWord(0x01)
        self.highMem =              machine.readWord(0x04)
        self.initPC =               machine.readWord(0x06)
        self.dict =                 machine.readWord(0x08)
        self.objectTable =          machine.readWord(0x0A)
        self.globals =              machine.readWord(0x0C)
        self.staticMem =            machine.readWord(0x0E)
        self.flags2 =               machine.readWord(0x10)
        self.serialCode = machine.data[0x12:0x18].decode("utf-8")
        self.a =                    machine.readWord(0x12)
        self.b =                    machine.readWord(0x14)
        self.c =                    machine.readWord(0x16)
        self.abbrev =               machine.readWord(0x18)
        self.length =               machine.readWord(0x1A)
        self.checksum =             machine.readWord(0x1C)
        self.interpreterNumber =    machine.readByte(0x1E)
        self.interpreterVersion =   machine.readByte(0x1F)
        self.scHeight =             machine.readByte(0x20)
        self.scWidth =              machine.readByte(0x21)
        self.scWidthUnits =         machine.readWord(0x22)
        self.scHeightUnits =        machine.readWord(0x24)

        if self.version == 6:
            self.fontHeight =           machine.readByte(0x26)
            self.fontWidth =            machine.readByte(0x27)
        else:
            self.fontWidth =            machine.readByte(0x26)
            self.fontHeight =           machine.readByte(0x27)

        self.routines =             machine.readWord(0x28)
        self.staticStrings =        machine.readWord(0x2A)
        self.bgColor =              machine.readByte(0x2C)
        self.fgColor =              machine.readByte(0x2D)
        self.termCharTable =        machine.readWord(0x2E)
        self.pixelWidthStream3 =    machine.readWord(0x30)
        self.revNumber =            machine.readWord(0x32)
        self.alphabetTable =        machine.readWord(0x34)
        self.headerExtensionTable = machine.readWord(0x36)
        self.userName = machine.data[0x38:0x3C].decode("utf-8")
        self.n =                    machine.readWord(0x38)
        self.o =                    machine.readByte(0x3A)
        self.compiler = machine.data[0x3C:0x40].decode("utf-8")
        self.p =                    machine.readByte(0x3C)
        self.q =                    machine.readByte(0x3E)
        self.interpreterVersion = machine.readByte(0)

        pass

class ZMachine:
    def __init__(self, basePath, fileName):
        self.readFile(basePath, fileName)

        self.header = Header(self)

        self.setup()
        self.run()

    def readFile(self, basePath, fileName):
        self.data = [0]
        with open(basePath + fileName, 'rb') as file:
            self.data = bytearray(file.read())
        pass

    def setup(self):
        self.pc = self.header.initPC
        self.currentScope = RoutineScope(self, None, None, [])
        pass

    def run(self):
        while True:
            self.decodeOp()
        pass

    def readByte(self, address):
        ret, = unpack('>B', self.data[address:address+1])
        return ret

    def readWord(self, address):
        ret, = unpack('>H', self.data[address:address+2])
        return ret

    def writeByte(self, address, value):
        val = pack('>B', value)
        self.data[address] = val[0]

    def writeWord(self, address, value):
        val = pack('>H', value)
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
        if self.header.version <= 3:
            return address * 8

    def call(self, address, param):
        address = self.unpackAddressRoutine(address.load())
        print("calling", address, hex(address), 'params:', param)
        self.currentScope = RoutineScope(self, self.currentScope, address, param)
        self.pc = self.currentScope.startAddress

    def decodeOp(self):
        print("")
        opCode = self.readBytePC()
        print('opCode:', opCode, hex(opCode))

        opc = opCodes[opCode](self)
        print('opCode', opc)
        opc.decode(self)
        opc.call(self)

        pass

def main():
    basePath = '../'
    fileName = 'Enchanter.z3'

    zm = ZMachine(basePath, fileName)


    pass


if __name__ == '__main__':
    main()