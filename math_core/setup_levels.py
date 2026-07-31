from setuptools import setup, Extension
from Cython.Build import cythonize

extension = [
	Extension(
		'equation_levels',
		sources=[
			'src_c/equation_levels.pyx',
			'src_c/eq_4.c',
			'src_c/eq_5.c',
			'src_c/eq_6.c',
			'src_c/eq_7.c',
			'src_c/eq_8.c'
		],
		include_dirs=['.']
	)
]

setup(name='equation_levels', ext_modules=cythonize(extension, language_level='3'))