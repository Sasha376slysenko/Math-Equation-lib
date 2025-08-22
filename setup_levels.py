from setuptools import setup, Extension
from Cython.Build import cythonize

extension = [
	Extension(
		'equation_levels',
		sources=[
			'equation_levels.pyx',
			'eq_add_sub_br.c',
			'eq_mul_div_br.c',
			'eq_add_sub_mul_div_br.c'
		],
		include_dirs=['.']
	)
]

setup(name='equation_levels', ext_modules=cythonize(extension, language_level='3'))