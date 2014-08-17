from opcodeCode import *
from opcodeDecode import *

opCodes = [0] * 256

class Opcode_Je_SC_SC(Opcode_SC_SC, Opcode_Je):
	pass
# hex 54
opCodes[0x01] = Opcode_Je_SC_SC

class Opcode_Jl_SC_SC(Opcode_SC_SC, Opcode_Jl):
	pass
# hex 54
opCodes[0x02] = Opcode_Jl_SC_SC

class Opcode_Jg_SC_SC(Opcode_SC_SC, Opcode_Jg):
	pass
# hex 54
opCodes[0x03] = Opcode_Jg_SC_SC

class Opcode_DecChk_SC_SC(Opcode_SC_SC, Opcode_DecChk):
	pass
# hex 54
opCodes[0x04] = Opcode_DecChk_SC_SC

class Opcode_IncChk_SC_SC(Opcode_SC_SC, Opcode_IncChk):
	pass
# hex 54
opCodes[0x05] = Opcode_IncChk_SC_SC

class Opcode_Jin_SC_SC(Opcode_SC_SC, Opcode_Jin):
	pass
# hex 54
opCodes[0x06] = Opcode_Jin_SC_SC

class Opcode_Test_SC_SC(Opcode_SC_SC, Opcode_Test):
	pass
# hex 54
opCodes[0x07] = Opcode_Test_SC_SC

class Opcode_Or_SC_SC(Opcode_SC_SC, Opcode_Or):
	pass
# hex 54
opCodes[0x08] = Opcode_Or_SC_SC

class Opcode_And_SC_SC(Opcode_SC_SC, Opcode_And):
	pass
# hex 54
opCodes[0x09] = Opcode_And_SC_SC

class Opcode_TestAttr_SC_SC(Opcode_SC_SC, Opcode_TestAttr):
	pass
# hex 54
opCodes[0x0A] = Opcode_TestAttr_SC_SC

class Opcode_SetAttr_SC_SC(Opcode_SC_SC, Opcode_SetAttr):
	pass
# hex 54
opCodes[0x0B] = Opcode_SetAttr_SC_SC

class Opcode_ClearAttr_SC_SC(Opcode_SC_SC, Opcode_ClearAttr):
	pass
# hex 54
opCodes[0x0C] = Opcode_ClearAttr_SC_SC

class Opcode_Store_SC_SC(Opcode_SC_SC, Opcode_Store):
	pass
# hex 54
opCodes[0x0D] = Opcode_Store_SC_SC

class Opcode_InsertObj_SC_SC(Opcode_SC_SC, Opcode_InsertObj):
	pass
# hex 54
opCodes[0x0E] = Opcode_InsertObj_SC_SC

class Opcode_LoadW_SC_SC(Opcode_SC_SC, Opcode_LoadW):
	pass
# hex 54
opCodes[0x0F] = Opcode_LoadW_SC_SC

class Opcode_LoadB_SC_SC(Opcode_SC_SC, Opcode_LoadB):
	pass
# hex 54
opCodes[0x10] = Opcode_LoadB_SC_SC

class Opcode_GetProp_SC_SC(Opcode_SC_SC, Opcode_GetProp):
	pass
# hex 54
opCodes[0x11] = Opcode_GetProp_SC_SC

class Opcode_GetPropAddr_SC_SC(Opcode_SC_SC, Opcode_GetPropAddr):
	pass
# hex 54
opCodes[0x12] = Opcode_GetPropAddr_SC_SC

class Opcode_GetNextProp_SC_SC(Opcode_SC_SC, Opcode_GetNextProp):
	pass
# hex 54
opCodes[0x13] = Opcode_GetNextProp_SC_SC

class Opcode_Add_SC_SC(Opcode_SC_SC, Opcode_Add):
	pass
# hex 54
opCodes[0x14] = Opcode_Add_SC_SC

class Opcode_Sub_SC_SC(Opcode_SC_SC, Opcode_Sub):
	pass
# hex 54
opCodes[0x15] = Opcode_Sub_SC_SC

class Opcode_Mul_SC_SC(Opcode_SC_SC, Opcode_Mul):
	pass
# hex 54
opCodes[0x16] = Opcode_Mul_SC_SC

class Opcode_Div_SC_SC(Opcode_SC_SC, Opcode_Div):
	pass
# hex 54
opCodes[0x17] = Opcode_Div_SC_SC

class Opcode_Mod_SC_SC(Opcode_SC_SC, Opcode_Mod):
	pass
# hex 54
opCodes[0x18] = Opcode_Mod_SC_SC

class Opcode_Call2S_SC_SC(Opcode_SC_SC, Opcode_Call2S):
	pass
# hex 54
opCodes[0x19] = Opcode_Call2S_SC_SC

class Opcode_Call2N_SC_SC(Opcode_SC_SC, Opcode_Call2N):
	pass
# hex 54
opCodes[0x1A] = Opcode_Call2N_SC_SC

class Opcode_SetColor_SC_SC(Opcode_SC_SC, Opcode_SetColor):
	pass
# hex 54
opCodes[0x1B] = Opcode_SetColor_SC_SC

class Opcode_Throw_SC_SC(Opcode_SC_SC, Opcode_Throw):
	pass
# hex 54
opCodes[0x1C] = Opcode_Throw_SC_SC





class Opcode_Je_SC_V(Opcode_SC_V, Opcode_Je):
	pass
# hex 54
opCodes[0x21] = Opcode_Je_SC_V

class Opcode_Jl_SC_V(Opcode_SC_V, Opcode_Jl):
	pass
# hex 54
opCodes[0x22] = Opcode_Jl_SC_V

class Opcode_Jg_SC_V(Opcode_SC_V, Opcode_Jg):
	pass
# hex 54
opCodes[0x23] = Opcode_Jg_SC_V

class Opcode_DecChk_SC_V(Opcode_SC_V, Opcode_DecChk):
	pass
# hex 54
opCodes[0x24] = Opcode_DecChk_SC_V

class Opcode_IncChk_SC_V(Opcode_SC_V, Opcode_IncChk):
	pass
# hex 54
opCodes[0x25] = Opcode_IncChk_SC_V

class Opcode_Jin_SC_V(Opcode_SC_V, Opcode_Jin):
	pass
# hex 54
opCodes[0x26] = Opcode_Jin_SC_V

class Opcode_Test_SC_V(Opcode_SC_V, Opcode_Test):
	pass
# hex 54
opCodes[0x27] = Opcode_Test_SC_V

class Opcode_Or_SC_V(Opcode_SC_V, Opcode_Or):
	pass
# hex 54
opCodes[0x28] = Opcode_Or_SC_V

class Opcode_And_SC_V(Opcode_SC_V, Opcode_And):
	pass
# hex 54
opCodes[0x29] = Opcode_And_SC_V

class Opcode_TestAttr_SC_V(Opcode_SC_V, Opcode_TestAttr):
	pass
# hex 54
opCodes[0x2A] = Opcode_TestAttr_SC_V

class Opcode_SetAttr_SC_V(Opcode_SC_V, Opcode_SetAttr):
	pass
# hex 54
opCodes[0x2B] = Opcode_SetAttr_SC_V

class Opcode_ClearAttr_SC_V(Opcode_SC_V, Opcode_ClearAttr):
	pass
# hex 54
opCodes[0x2C] = Opcode_ClearAttr_SC_V

class Opcode_Store_SC_V(Opcode_SC_V, Opcode_Store):
	pass
# hex 54
opCodes[0x2D] = Opcode_Store_SC_V

class Opcode_InsertObj_SC_V(Opcode_SC_V, Opcode_InsertObj):
	pass
# hex 54
opCodes[0x2E] = Opcode_InsertObj_SC_V

class Opcode_LoadW_SC_V(Opcode_SC_V, Opcode_LoadW):
	pass
# hex 54
opCodes[0x2F] = Opcode_LoadW_SC_V

class Opcode_LoadB_SC_V(Opcode_SC_V, Opcode_LoadB):
	pass
# hex 54
opCodes[0x30] = Opcode_LoadB_SC_V

class Opcode_GetProp_SC_V(Opcode_SC_V, Opcode_GetProp):
	pass
# hex 54
opCodes[0x31] = Opcode_GetProp_SC_V

class Opcode_GetPropAddr_SC_V(Opcode_SC_V, Opcode_GetPropAddr):
	pass
# hex 54
opCodes[0x32] = Opcode_GetPropAddr_SC_V

class Opcode_GetNextProp_SC_V(Opcode_SC_V, Opcode_GetNextProp):
	pass
# hex 54
opCodes[0x33] = Opcode_GetNextProp_SC_V

class Opcode_Add_SC_V(Opcode_SC_V, Opcode_Add):
	pass
# hex 54
opCodes[0x34] = Opcode_Add_SC_V

class Opcode_Sub_SC_V(Opcode_SC_V, Opcode_Sub):
	pass
# hex 54
opCodes[0x35] = Opcode_Sub_SC_V

class Opcode_Mul_SC_V(Opcode_SC_V, Opcode_Mul):
	pass
# hex 54
opCodes[0x36] = Opcode_Mul_SC_V

class Opcode_Div_SC_V(Opcode_SC_V, Opcode_Div):
	pass
# hex 54
opCodes[0x37] = Opcode_Div_SC_V

class Opcode_Mod_SC_V(Opcode_SC_V, Opcode_Mod):
	pass
# hex 54
opCodes[0x38] = Opcode_Mod_SC_V

class Opcode_Call2S_SC_V(Opcode_SC_V, Opcode_Call2S):
	pass
# hex 54
opCodes[0x39] = Opcode_Call2S_SC_V

class Opcode_Call2N_SC_V(Opcode_SC_V, Opcode_Call2N):
	pass
# hex 54
opCodes[0x3A] = Opcode_Call2N_SC_V

class Opcode_SetColor_SC_V(Opcode_SC_V, Opcode_SetColor):
	pass
# hex 54
opCodes[0x3B] = Opcode_SetColor_SC_V

class Opcode_Throw_SC_V(Opcode_SC_V, Opcode_Throw):
	pass
# hex 54
opCodes[0x3C] = Opcode_Throw_SC_V





class Opcode_Je_V_SC(Opcode_V_SC, Opcode_Je):
	pass
# hex 54
opCodes[0x41] = Opcode_Je_V_SC

class Opcode_Jl_V_SC(Opcode_V_SC, Opcode_Jl):
	pass
# hex 54
opCodes[0x42] = Opcode_Jl_V_SC

class Opcode_Jg_V_SC(Opcode_V_SC, Opcode_Jg):
	pass
# hex 54
opCodes[0x43] = Opcode_Jg_V_SC

class Opcode_DecChk_V_SC(Opcode_V_SC, Opcode_DecChk):
	pass
# hex 54
opCodes[0x44] = Opcode_DecChk_V_SC

class Opcode_IncChk_V_SC(Opcode_V_SC, Opcode_IncChk):
	pass
# hex 54
opCodes[0x45] = Opcode_IncChk_V_SC

class Opcode_Jin_V_SC(Opcode_V_SC, Opcode_Jin):
	pass
# hex 54
opCodes[0x46] = Opcode_Jin_V_SC

class Opcode_Test_V_SC(Opcode_V_SC, Opcode_Test):
	pass
# hex 54
opCodes[0x47] = Opcode_Test_V_SC

class Opcode_Or_V_SC(Opcode_V_SC, Opcode_Or):
	pass
# hex 54
opCodes[0x48] = Opcode_Or_V_SC

class Opcode_And_V_SC(Opcode_V_SC, Opcode_And):
	pass
# hex 54
opCodes[0x49] = Opcode_And_V_SC

class Opcode_TestAttr_V_SC(Opcode_V_SC, Opcode_TestAttr):
	pass
# hex 54
opCodes[0x4A] = Opcode_TestAttr_V_SC

class Opcode_SetAttr_V_SC(Opcode_V_SC, Opcode_SetAttr):
	pass
# hex 54
opCodes[0x4B] = Opcode_SetAttr_V_SC

class Opcode_ClearAttr_V_SC(Opcode_V_SC, Opcode_ClearAttr):
	pass
# hex 54
opCodes[0x4C] = Opcode_ClearAttr_V_SC

class Opcode_Store_V_SC(Opcode_V_SC, Opcode_Store):
	pass
# hex 54
opCodes[0x4D] = Opcode_Store_V_SC

class Opcode_InsertObj_V_SC(Opcode_V_SC, Opcode_InsertObj):
	pass
# hex 54
opCodes[0x4E] = Opcode_InsertObj_V_SC

class Opcode_LoadW_V_SC(Opcode_V_SC, Opcode_LoadW):
	pass
# hex 54
opCodes[0x4F] = Opcode_LoadW_V_SC

class Opcode_LoadB_V_SC(Opcode_V_SC, Opcode_LoadB):
	pass
# hex 54
opCodes[0x50] = Opcode_LoadB_V_SC

class Opcode_GetProp_V_SC(Opcode_V_SC, Opcode_GetProp):
	pass
# hex 54
opCodes[0x51] = Opcode_GetProp_V_SC

class Opcode_GetPropAddr_V_SC(Opcode_V_SC, Opcode_GetPropAddr):
	pass
# hex 54
opCodes[0x52] = Opcode_GetPropAddr_V_SC

class Opcode_GetNextProp_V_SC(Opcode_V_SC, Opcode_GetNextProp):
	pass
# hex 54
opCodes[0x53] = Opcode_GetNextProp_V_SC

class Opcode_Add_V_SC(Opcode_V_SC, Opcode_Add):
	pass
# hex 54
opCodes[0x54] = Opcode_Add_V_SC

class Opcode_Sub_V_SC(Opcode_V_SC, Opcode_Sub):
	pass
# hex 54
opCodes[0x55] = Opcode_Sub_V_SC

class Opcode_Mul_V_SC(Opcode_V_SC, Opcode_Mul):
	pass
# hex 54
opCodes[0x56] = Opcode_Mul_V_SC

class Opcode_Div_V_SC(Opcode_V_SC, Opcode_Div):
	pass
# hex 54
opCodes[0x57] = Opcode_Div_V_SC

class Opcode_Mod_V_SC(Opcode_V_SC, Opcode_Mod):
	pass
# hex 54
opCodes[0x58] = Opcode_Mod_V_SC

class Opcode_Call2S_V_SC(Opcode_V_SC, Opcode_Call2S):
	pass
# hex 54
opCodes[0x59] = Opcode_Call2S_V_SC

class Opcode_Call2N_V_SC(Opcode_V_SC, Opcode_Call2N):
	pass
# hex 54
opCodes[0x5A] = Opcode_Call2N_V_SC

class Opcode_SetColor_V_SC(Opcode_V_SC, Opcode_SetColor):
	pass
# hex 54
opCodes[0x5B] = Opcode_SetColor_V_SC

class Opcode_Throw_V_SC(Opcode_V_SC, Opcode_Throw):
	pass
# hex 54
opCodes[0x5C] = Opcode_Throw_V_SC





class Opcode_Je_V_V(Opcode_V_V, Opcode_Je):
	pass
# hex 54
opCodes[0x61] = Opcode_Je_V_V

class Opcode_Jl_V_V(Opcode_V_V, Opcode_Jl):
	pass
# hex 54
opCodes[0x62] = Opcode_Jl_V_V

class Opcode_Jg_V_V(Opcode_V_V, Opcode_Jg):
	pass
# hex 54
opCodes[0x63] = Opcode_Jg_V_V

class Opcode_DecChk_V_V(Opcode_V_V, Opcode_DecChk):
	pass
# hex 54
opCodes[0x64] = Opcode_DecChk_V_V

class Opcode_IncChk_V_V(Opcode_V_V, Opcode_IncChk):
	pass
# hex 54
opCodes[0x65] = Opcode_IncChk_V_V

class Opcode_Jin_V_V(Opcode_V_V, Opcode_Jin):
	pass
# hex 54
opCodes[0x66] = Opcode_Jin_V_V

class Opcode_Test_V_V(Opcode_V_V, Opcode_Test):
	pass
# hex 54
opCodes[0x67] = Opcode_Test_V_V

class Opcode_Or_V_V(Opcode_V_V, Opcode_Or):
	pass
# hex 54
opCodes[0x68] = Opcode_Or_V_V

class Opcode_And_V_V(Opcode_V_V, Opcode_And):
	pass
# hex 54
opCodes[0x69] = Opcode_And_V_V

class Opcode_TestAttr_V_V(Opcode_V_V, Opcode_TestAttr):
	pass
# hex 54
opCodes[0x6A] = Opcode_TestAttr_V_V

class Opcode_SetAttr_V_V(Opcode_V_V, Opcode_SetAttr):
	pass
# hex 54
opCodes[0x6B] = Opcode_SetAttr_V_V

class Opcode_ClearAttr_V_V(Opcode_V_V, Opcode_ClearAttr):
	pass
# hex 54
opCodes[0x6C] = Opcode_ClearAttr_V_V

class Opcode_Store_V_V(Opcode_V_V, Opcode_Store):
	pass
# hex 54
opCodes[0x6D] = Opcode_Store_V_V

class Opcode_InsertObj_V_V(Opcode_V_V, Opcode_InsertObj):
	pass
# hex 54
opCodes[0x6E] = Opcode_InsertObj_V_V

class Opcode_LoadW_V_V(Opcode_V_V, Opcode_LoadW):
	pass
# hex 54
opCodes[0x6F] = Opcode_LoadW_V_V

class Opcode_LoadB_V_V(Opcode_V_V, Opcode_LoadB):
	pass
# hex 54
opCodes[0x70] = Opcode_LoadB_V_V

class Opcode_GetProp_V_V(Opcode_V_V, Opcode_GetProp):
	pass
# hex 54
opCodes[0x71] = Opcode_GetProp_V_V

class Opcode_GetPropAddr_V_V(Opcode_V_V, Opcode_GetPropAddr):
	pass
# hex 54
opCodes[0x72] = Opcode_GetPropAddr_V_V

class Opcode_GetNextProp_V_V(Opcode_V_V, Opcode_GetNextProp):
	pass
# hex 54
opCodes[0x73] = Opcode_GetNextProp_V_V

class Opcode_Add_V_V(Opcode_V_V, Opcode_Add):
	pass
# hex 54
opCodes[0x74] = Opcode_Add_V_V

class Opcode_Sub_V_V(Opcode_V_V, Opcode_Sub):
	pass
# hex 54
opCodes[0x75] = Opcode_Sub_V_V

class Opcode_Mul_V_V(Opcode_V_V, Opcode_Mul):
	pass
# hex 54
opCodes[0x76] = Opcode_Mul_V_V

class Opcode_Div_V_V(Opcode_V_V, Opcode_Div):
	pass
# hex 54
opCodes[0x77] = Opcode_Div_V_V

class Opcode_Mod_V_V(Opcode_V_V, Opcode_Mod):
	pass
# hex 54
opCodes[0x78] = Opcode_Mod_V_V

class Opcode_Call2S_V_V(Opcode_V_V, Opcode_Call2S):
	pass
# hex 54
opCodes[0x79] = Opcode_Call2S_V_V

class Opcode_Call2N_V_V(Opcode_V_V, Opcode_Call2N):
	pass
# hex 54
opCodes[0x7A] = Opcode_Call2N_V_V

class Opcode_SetColor_V_V(Opcode_V_V, Opcode_SetColor):
	pass
# hex 54
opCodes[0x7B] = Opcode_SetColor_V_V

class Opcode_Throw_V_V(Opcode_V_V, Opcode_Throw):
	pass
# hex 54
opCodes[0x7C] = Opcode_Throw_V_V






class Opcode_Jz_LC(Opcode_LC, Opcode_Jz):
	pass
# hex 54
opCodes[0x80] = Opcode_Jz_LC

class Opcode_GetSibling_LC(Opcode_LC, Opcode_GetSibling):
	pass
# hex 54
opCodes[0x81] = Opcode_GetSibling_LC

class Opcode_GetChild_LC(Opcode_LC, Opcode_GetChild):
	pass
# hex 54
opCodes[0x82] = Opcode_GetChild_LC

class Opcode_GetParent_LC(Opcode_LC, Opcode_GetParent):
	pass
# hex 54
opCodes[0x83] = Opcode_GetParent_LC

class Opcode_GetPropLen_LC(Opcode_LC, Opcode_GetPropLen):
	pass
# hex 54
opCodes[0x84] = Opcode_GetPropLen_LC

class Opcode_Inc_LC(Opcode_LC, Opcode_Inc):
	pass
# hex 54
opCodes[0x85] = Opcode_Inc_LC

class Opcode_Dec_LC(Opcode_LC, Opcode_Dec):
	pass
# hex 54
opCodes[0x86] = Opcode_Dec_LC

class Opcode_PrintAddr_LC(Opcode_LC, Opcode_PrintAddr):
	pass
# hex 54
opCodes[0x87] = Opcode_PrintAddr_LC

class Opcode_Call1S_LC(Opcode_LC, Opcode_Call1S):
	pass
# hex 54
opCodes[0x88] = Opcode_Call1S_LC

class Opcode_RemoveObj_LC(Opcode_LC, Opcode_RemoveObj):
	pass
# hex 54
opCodes[0x89] = Opcode_RemoveObj_LC

class Opcode_PrintObj_LC(Opcode_LC, Opcode_PrintObj):
	pass
# hex 54
opCodes[0x8A] = Opcode_PrintObj_LC

class Opcode_Ret_LC(Opcode_LC, Opcode_Ret):
	pass
# hex 54
opCodes[0x8B] = Opcode_Ret_LC

class Opcode_Jump_LC(Opcode_LC, Opcode_Jump):
	pass
# hex 54
opCodes[0x8C] = Opcode_Jump_LC

class Opcode_PrintPaddr_LC(Opcode_LC, Opcode_PrintPaddr):
	pass
# hex 54
opCodes[0x8D] = Opcode_PrintPaddr_LC

class Opcode_Load_LC(Opcode_LC, Opcode_Load):
	pass
# hex 54
opCodes[0x8E] = Opcode_Load_LC

class Opcode_Not_LC(Opcode_LC, Opcode_Not):
	pass
# hex 54
opCodes[0x8F] = Opcode_Not_LC






class Opcode_Jz_SC(Opcode_SC, Opcode_Jz):
	pass
# hex 54
opCodes[0x90] = Opcode_Jz_SC

class Opcode_GetSibling_SC(Opcode_SC, Opcode_GetSibling):
	pass
# hex 54
opCodes[0x91] = Opcode_GetSibling_SC

class Opcode_GetChild_SC(Opcode_SC, Opcode_GetChild):
	pass
# hex 54
opCodes[0x92] = Opcode_GetChild_SC

class Opcode_GetParent_SC(Opcode_SC, Opcode_GetParent):
	pass
# hex 54
opCodes[0x93] = Opcode_GetParent_SC

class Opcode_GetPropLen_SC(Opcode_SC, Opcode_GetPropLen):
	pass
# hex 54
opCodes[0x94] = Opcode_GetPropLen_SC

class Opcode_Inc_SC(Opcode_SC, Opcode_Inc):
	pass
# hex 54
opCodes[0x95] = Opcode_Inc_SC

class Opcode_Dec_SC(Opcode_SC, Opcode_Dec):
	pass
# hex 54
opCodes[0x96] = Opcode_Dec_SC

class Opcode_PrintAddr_SC(Opcode_SC, Opcode_PrintAddr):
	pass
# hex 54
opCodes[0x97] = Opcode_PrintAddr_SC

class Opcode_Call1S_SC(Opcode_SC, Opcode_Call1S):
	pass
# hex 54
opCodes[0x98] = Opcode_Call1S_SC

class Opcode_RemoveObj_SC(Opcode_SC, Opcode_RemoveObj):
	pass
# hex 54
opCodes[0x99] = Opcode_RemoveObj_SC

class Opcode_PrintObj_SC(Opcode_SC, Opcode_PrintObj):
	pass
# hex 54
opCodes[0x9A] = Opcode_PrintObj_SC

class Opcode_Ret_SC(Opcode_SC, Opcode_Ret):
	pass
# hex 54
opCodes[0x9B] = Opcode_Ret_SC

class Opcode_Jump_SC(Opcode_SC, Opcode_Jump):
	pass
# hex 54
opCodes[0x9C] = Opcode_Jump_SC

class Opcode_PrintPaddr_SC(Opcode_SC, Opcode_PrintPaddr):
	pass
# hex 54
opCodes[0x9D] = Opcode_PrintPaddr_SC

class Opcode_Load_SC(Opcode_SC, Opcode_Load):
	pass
# hex 54
opCodes[0x9E] = Opcode_Load_SC

class Opcode_Not_SC(Opcode_SC, Opcode_Not):
	pass
# hex 54
opCodes[0x9F] = Opcode_Not_SC





class Opcode_Jz_V(Opcode_V, Opcode_Jz):
	pass
# hex 54
opCodes[0xA0] = Opcode_Jz_V

class Opcode_GetSibling_V(Opcode_V, Opcode_GetSibling):
	pass
# hex 54
opCodes[0xA1] = Opcode_GetSibling_V

class Opcode_GetChild_V(Opcode_V, Opcode_GetChild):
	pass
# hex 54
opCodes[0xA2] = Opcode_GetChild_V

class Opcode_GetParent_V(Opcode_V, Opcode_GetParent):
	pass
# hex 54
opCodes[0xA3] = Opcode_GetParent_V

class Opcode_GetPropLen_V(Opcode_V, Opcode_GetPropLen):
	pass
# hex 54
opCodes[0xA4] = Opcode_GetPropLen_V

class Opcode_Inc_V(Opcode_V, Opcode_Inc):
	pass
# hex 54
opCodes[0xA5] = Opcode_Inc_V

class Opcode_Dec_V(Opcode_V, Opcode_Dec):
	pass
# hex 54
opCodes[0xA6] = Opcode_Dec_V

class Opcode_PrintAddr_V(Opcode_V, Opcode_PrintAddr):
	pass
# hex 54
opCodes[0xA7] = Opcode_PrintAddr_V

class Opcode_Call1S_V(Opcode_V, Opcode_Call1S):
	pass
# hex 54
opCodes[0xA8] = Opcode_Call1S_V

class Opcode_RemoveObj_V(Opcode_V, Opcode_RemoveObj):
	pass
# hex 54
opCodes[0xA9] = Opcode_RemoveObj_V

class Opcode_PrintObj_V(Opcode_V, Opcode_PrintObj):
	pass
# hex 54
opCodes[0xAA] = Opcode_PrintObj_V

class Opcode_Ret_V(Opcode_V, Opcode_Ret):
	pass
# hex 54
opCodes[0xAB] = Opcode_Ret_V

class Opcode_Jump_V(Opcode_V, Opcode_Jump):
	pass
# hex 54
opCodes[0xAC] = Opcode_Jump_V

class Opcode_PrintPaddr_V(Opcode_V, Opcode_PrintPaddr):
	pass
# hex 54
opCodes[0xAD] = Opcode_PrintPaddr_V

class Opcode_Load_V(Opcode_V, Opcode_Load):
	pass
# hex 54
opCodes[0xAE] = Opcode_Load_V

class Opcode_Not_V(Opcode_V, Opcode_Not):
	pass
# hex 54
opCodes[0xAF] = Opcode_Not_V








class Opcode_RTrue_N(Opcode_N, Opcode_RTrue):
	pass
# hex 54
opCodes[0xB0] = Opcode_RTrue_N

class Opcode_RFalse_N(Opcode_N, Opcode_RFalse):
	pass
# hex 54
opCodes[0xB1] = Opcode_RFalse_N

class Opcode_Print_N(Opcode_N, Opcode_Print):
	pass
# hex 54
opCodes[0xB2] = Opcode_Print_N

class Opcode_PrintRet_N(Opcode_N, Opcode_PrintRet):
	pass
# hex 54
opCodes[0xB3] = Opcode_PrintRet_N

class Opcode_Nop_N(Opcode_N, Opcode_Nop):
	pass
# hex 54
opCodes[0xB4] = Opcode_Nop_N

class Opcode_Save_N(Opcode_N, Opcode_Save):
	pass
# hex 54
opCodes[0xB5] = Opcode_Save_N

class Opcode_Restore_N(Opcode_N, Opcode_Restore):
	pass
# hex 54
opCodes[0xB6] = Opcode_Restore_N

class Opcode_Restart_N(Opcode_N, Opcode_Restart):
	pass
# hex 54
opCodes[0xB7] = Opcode_Restart_N

class Opcode_RetPopped_N(Opcode_N, Opcode_RetPopped):
	pass
# hex 54
opCodes[0xB8] = Opcode_RetPopped_N

class Opcode_Pop_N(Opcode_N, Opcode_Pop):
	pass
# hex 54
opCodes[0xB9] = Opcode_Pop_N

class Opcode_Quit_N(Opcode_N, Opcode_Quit):
	pass
# hex 54
opCodes[0xBA] = Opcode_Quit_N

class Opcode_NewLine_N(Opcode_N, Opcode_NewLine):
	pass
# hex 54
opCodes[0xBB] = Opcode_NewLine_N

class Opcode_ShowStatus_N(Opcode_N, Opcode_ShowStatus):
	pass
# hex 54
opCodes[0xBC] = Opcode_ShowStatus_N

class Opcode_Verify_N(Opcode_N, Opcode_Verify):
	pass
# hex 54
opCodes[0xBD] = Opcode_Verify_N

class Opcode_Extended_N(Opcode_N, Opcode_Extended):
	pass
# hex 54
opCodes[0xBE] = Opcode_Extended_N

class Opcode_Piracy_N(Opcode_N, Opcode_Piracy):
	pass
# hex 54
opCodes[0xBF] = Opcode_Piracy_N







class Opcode_Je_VAR(Opcode_VAR, Opcode_Je):
	pass
# hex 54
opCodes[0xC1] = Opcode_Je_VAR

class Opcode_Jl_VAR(Opcode_VAR, Opcode_Jl):
	pass
# hex 54
opCodes[0xC2] = Opcode_Jl_VAR

class Opcode_Jg_VAR(Opcode_VAR, Opcode_Jg):
	pass
# hex 54
opCodes[0xC3] = Opcode_Jg_VAR

class Opcode_DecChk_VAR(Opcode_VAR, Opcode_DecChk):
	pass
# hex 54
opCodes[0xC4] = Opcode_DecChk_VAR

class Opcode_IncChk_VAR(Opcode_VAR, Opcode_IncChk):
	pass
# hex 54
opCodes[0xC5] = Opcode_IncChk_VAR

class Opcode_Jin_VAR(Opcode_VAR, Opcode_Jin):
	pass
# hex 54
opCodes[0xC6] = Opcode_Jin_VAR

class Opcode_Test_VAR(Opcode_VAR, Opcode_Test):
	pass
# hex 54
opCodes[0xC7] = Opcode_Test_VAR

class Opcode_Or_VAR(Opcode_VAR, Opcode_Or):
	pass
# hex 54
opCodes[0xC8] = Opcode_Or_VAR

class Opcode_And_VAR(Opcode_VAR, Opcode_And):
	pass
# hex 54
opCodes[0xC9] = Opcode_And_VAR

class Opcode_TestAttr_VAR(Opcode_VAR, Opcode_TestAttr):
	pass
# hex 54
opCodes[0xCA] = Opcode_TestAttr_VAR

class Opcode_SetAttr_VAR(Opcode_VAR, Opcode_SetAttr):
	pass
# hex 54
opCodes[0xCB] = Opcode_SetAttr_VAR

class Opcode_ClearAttr_VAR(Opcode_VAR, Opcode_ClearAttr):
	pass
# hex 54
opCodes[0xCC] = Opcode_ClearAttr_VAR

class Opcode_Store_VAR(Opcode_VAR, Opcode_Store):
	pass
# hex 54
opCodes[0xCD] = Opcode_Store_VAR

class Opcode_InsertObj_VAR(Opcode_VAR, Opcode_InsertObj):
	pass
# hex 54
opCodes[0xCE] = Opcode_InsertObj_VAR

class Opcode_LoadW_VAR(Opcode_VAR, Opcode_LoadW):
	pass
# hex 54
opCodes[0xCF] = Opcode_LoadW_VAR

class Opcode_LoadB_VAR(Opcode_VAR, Opcode_LoadB):
	pass
# hex 54
opCodes[0xD0] = Opcode_LoadB_VAR

class Opcode_GetProp_VAR(Opcode_VAR, Opcode_GetProp):
	pass
# hex 54
opCodes[0xD1] = Opcode_GetProp_VAR

class Opcode_GetPropAddr_VAR(Opcode_VAR, Opcode_GetPropAddr):
	pass
# hex 54
opCodes[0xD2] = Opcode_GetPropAddr_VAR

class Opcode_GetNextProp_VAR(Opcode_VAR, Opcode_GetNextProp):
	pass
# hex 54
opCodes[0xD3] = Opcode_GetNextProp_VAR

class Opcode_Add_VAR(Opcode_VAR, Opcode_Add):
	pass
# hex 54
opCodes[0xD4] = Opcode_Add_VAR

class Opcode_Sub_VAR(Opcode_VAR, Opcode_Sub):
	pass
# hex 54
opCodes[0xD5] = Opcode_Sub_VAR

class Opcode_Mul_VAR(Opcode_VAR, Opcode_Mul):
	pass
# hex 54
opCodes[0xD6] = Opcode_Mul_VAR

class Opcode_Div_VAR(Opcode_VAR, Opcode_Div):
	pass
# hex 54
opCodes[0xD7] = Opcode_Div_VAR

class Opcode_Mod_VAR(Opcode_VAR, Opcode_Mod):
	pass
# hex 54
opCodes[0xD8] = Opcode_Mod_VAR

class Opcode_Call2S_VAR(Opcode_VAR, Opcode_Call2S):
	pass
# hex 54
opCodes[0xD9] = Opcode_Call2S_VAR

class Opcode_Call2N_VAR(Opcode_VAR, Opcode_Call2N):
	pass
# hex 54
opCodes[0xDA] = Opcode_Call2N_VAR

class Opcode_SetColor_VAR(Opcode_VAR, Opcode_SetColor):
	pass
# hex 54
opCodes[0xDB] = Opcode_SetColor_VAR

class Opcode_Throw_VAR(Opcode_VAR, Opcode_Throw):
	pass
# hex 54
opCodes[0xDC] = Opcode_Throw_VAR




class Opcode_Call_VAR(Opcode_VAR, Opcode_Call):
	pass
opCodes[0xE0] = Opcode_Call_VAR

class Opcode_StoreW_VAR(Opcode_VAR, Opcode_StoreW):
	pass
opCodes[0xE1] = Opcode_StoreW_VAR

class Opcode_StoreB_VAR(Opcode_VAR, Opcode_StoreB):
	pass
opCodes[0xE2] = Opcode_StoreB_VAR

class Opcode_PutProp_VAR(Opcode_VAR, Opcode_PutProp):
	pass
opCodes[0xE3] = Opcode_PutProp_VAR

class Opcode_SRead_VAR(Opcode_VAR, Opcode_SRead):
	pass
opCodes[0xE4] = Opcode_SRead_VAR

class Opcode_PrintChar_VAR(Opcode_VAR, Opcode_PrintChar):
	pass
opCodes[0xE5] = Opcode_PrintChar_VAR

class Opcode_PrintNum_VAR(Opcode_VAR, Opcode_PrintNum):
	pass
opCodes[0xE6] = Opcode_PrintNum_VAR

class Opcode_Random_VAR(Opcode_VAR, Opcode_Random):
	pass
opCodes[0xE7] = Opcode_Random_VAR

class Opcode_Push_VAR(Opcode_VAR, Opcode_Push):
	pass
opCodes[0xE8] = Opcode_Push_VAR

class Opcode_Pull_VAR(Opcode_VAR, Opcode_Pull):
	pass
opCodes[0xE9] = Opcode_Pull_VAR

class Opcode_SplitWindow_VAR(Opcode_VAR, Opcode_SplitWindow):
	pass
opCodes[0xEA] = Opcode_SplitWindow_VAR

class Opcode_SetWindow_VAR(Opcode_VAR, Opcode_SetWindow):
	pass
opCodes[0xEB] = Opcode_SetWindow_VAR

class Opcode_CallVS2_VAR2(Opcode_VAR2, Opcode_CallVS2):
	pass
opCodes[0xEC] = Opcode_CallVS2_VAR2

class Opcode_EraseWindow_VAR(Opcode_VAR, Opcode_EraseWindow):
	pass
opCodes[0xED] = Opcode_EraseWindow_VAR

class Opcode_EraseLine_VAR(Opcode_VAR, Opcode_EraseLine):
	pass
opCodes[0xEE] = Opcode_EraseLine_VAR

class Opcode_SetCursor_VAR(Opcode_VAR, Opcode_SetCursor):
	pass
opCodes[0xEF] = Opcode_SetCursor_VAR

class Opcode_GetCursor_VAR(Opcode_VAR, Opcode_GetCursor):
	pass
opCodes[0xF0] = Opcode_GetCursor_VAR

class Opcode_SetTextStyle_VAR(Opcode_VAR, Opcode_SetTextStyle):
	pass
opCodes[0xF1] = Opcode_SetTextStyle_VAR

class Opcode_BufferMode_VAR(Opcode_VAR, Opcode_BufferMode):
	pass
opCodes[0xF2] = Opcode_BufferMode_VAR

class Opcode_OutputStream_VAR(Opcode_VAR, Opcode_OutputStream):
	pass
opCodes[0xF3] = Opcode_OutputStream_VAR

class Opcode_InputStream_VAR(Opcode_VAR, Opcode_InputStream):
	pass
opCodes[0xF4] = Opcode_InputStream_VAR

class Opcode_SoundEffect_VAR(Opcode_VAR, Opcode_SoundEffect):
	pass
opCodes[0xF5] = Opcode_SoundEffect_VAR

class Opcode_ReadChar_VAR(Opcode_VAR, Opcode_ReadChar):
	pass
opCodes[0xF6] = Opcode_ReadChar_VAR

class Opcode_ScanTable_VAR(Opcode_VAR, Opcode_ScanTable):
	pass
opCodes[0xF7] = Opcode_ScanTable_VAR

class Opcode_Not_VAR(Opcode_VAR, Opcode_Not):
	pass
opCodes[0xF8] = Opcode_Not_VAR

class Opcode_CallVN_VAR(Opcode_VAR, Opcode_CallVN):
	pass
opCodes[0xF9] = Opcode_CallVN_VAR

class Opcode_CallVN2_VAR2(Opcode_VAR2, Opcode_CallVN2):
	pass
opCodes[0xFA] = Opcode_CallVN2_VAR2

class Opcode_Tokenise_VAR(Opcode_VAR, Opcode_Tokenise):
	pass
opCodes[0xFB] = Opcode_Tokenise_VAR

class Opcode_EncodeText_VAR(Opcode_VAR, Opcode_EncodeText):
	pass
opCodes[0xFC] = Opcode_EncodeText_VAR

class Opcode_CopyTable_VAR(Opcode_VAR, Opcode_CopyTable):
	pass
opCodes[0xFD] = Opcode_CopyTable_VAR

class Opcode_PrintTable_VAR(Opcode_VAR, Opcode_PrintTable):
	pass
opCodes[0xFE] = Opcode_PrintTable_VAR

class Opcode_CheckArgCount_VAR(Opcode_VAR, Opcode_CheckArgCount):
	pass
opCodes[0xFF] = Opcode_CheckArgCount_VAR


