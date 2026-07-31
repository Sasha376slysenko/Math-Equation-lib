cdef set SYMBOL_IF = {
	'*', '/', '+', '-', '(', ')', '=',
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
}

cdef extern from "levels_eq.h":
	cdef struct EQ_4:
		unsigned int digit[10]
		char equation[10][1000]
	cdef struct EQ_5:
		unsigned int digit[10]
		char equation[10][1000]
	cdef struct EQ_6:
		unsigned int digit[10]
		char equation[10][1000]
	cdef struct EQ_7:
		unsigned int digit[10]
		char equation[10][1000]
	cdef struct EQ_8:
		unsigned int digit[10]
		char equation[10][1000]

	cdef void initeq_4()
	cdef void initeq_5()
	cdef void initeq_6()
	cdef void initeq_7()
	cdef void initeq_8()

	cdef EQ_4 eq_4
	cdef EQ_5 eq_5
	cdef EQ_6 eq_6
	cdef EQ_7 eq_7
	cdef EQ_8 eq_8


def init():
	initeq_4()
	initeq_5()
	initeq_6()
	initeq_7()
	initeq_8()


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


def get_digit_4(unsigned int index):
	return eq_4.digit[index]


cpdef get_equations_4(unsigned int index):
	cdef str eqs = bytes(eq_4.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_5(unsigned int index):
	return eq_5.digit[index]


cpdef get_equations_5(unsigned int index):
	cdef str eqs = bytes(eq_5.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_6(unsigned int index):
	return eq_6.digit[index]


cpdef get_equations_6(unsigned int index):
	cdef str eqs = bytes(eq_6.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_7(unsigned int index):
	return eq_7.digit[index]


cpdef get_equations_7(unsigned int index):
	cdef str eqs = bytes(eq_7.equation[index]).decode('utf-8')
	return list_eq(eqs)


def get_digit_8(unsigned int index):
	return eq_8.digit[index]


cpdef get_equations_8(unsigned int index):
	cdef str eqs = bytes(eq_8.equation[index]).decode('utf-8')
	return list_eq(eqs)
