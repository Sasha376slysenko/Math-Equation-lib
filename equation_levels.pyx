cdef set SYMBOL_IF = {
	'*', '/', '+', '-', '(', ')', '=',
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}

cdef extern from "levels.h":
	cdef struct EqAddSubBracket:
		unsigned short digit[100]
		char equation[100][1000]

	cdef struct EqMulDivBracket:
		unsigned short digit[100]
		char equation[100][1000]

	cdef struct EqAddSubMulDivBracket:
		unsigned short digit[100]
		char equation[100][1000]

	cdef void initAddSubBracket()
	cdef void initMulDivBracket()
	cdef void initAddSubMulDivBracket()

	cdef EqAddSubBracket AddSubBracket
	cdef EqMulDivBracket MulDivBracket
	cdef EqAddSubMulDivBracket AddSubMulDivBracket


def init():
	initAddSubBracket()
	initMulDivBracket()
	initAddSubMulDivBracket()


def list_eq(str eqs_i):
	cdef str ch = ''
	cdef str temp_str = ''
	cdef list result_eq = []

	for ch in eqs_i:
		if ch in SYMBOL_IF:
			temp_str += ch
		elif ch == ',':
			result_eq.append(temp_str)
		else:
			temp_str = ''
	return result_eq


def get_digit_add_sub_br(unsigned int index):
	return AddSubBracket.digit[index]


cpdef get_eq_add_sub_br(unsigned int index):
	cdef str eqs = bytes(AddSubBracket.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_mul_div_br(unsigned int index):
	return MulDivBracket.digit[index]


cpdef get_eq_mul_div_br(unsigned int index):
	cdef str eqs = bytes(MulDivBracket.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_add_sub_mul_div_br(unsigned int index):
	return AddSubMulDivBracket.digit[index]


cpdef get_eq_add_sub_mul_div_br(unsigned int index):
	cdef str eqs = bytes(AddSubMulDivBracket.equation[index]).decode('utf-8')
	return list_eq(eqs)