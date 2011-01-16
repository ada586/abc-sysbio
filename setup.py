
from distutils.core import setup

setup(name='abc-sysbio',
      version='2.01',
      description='Approximate Bayesian Computation for systems biology',

      author='Chris Barnes, Juliane Liepe, Erika Cule',

      author_email='christopher.barnes@imperial.ac.uk,juliane.liepe08@imperial.ac.uk',

      url='http://abc-sysbio.sourceforge.net/',

      packages=['abccuda','abcsysbio'],

      scripts=['scripts/run-abc-sysbio', 
               'scripts/abc-sysbio-sbml-sum'],

      package_data={ 'abccuda': ['MersenneTwister.dat','MersenneTwister.cu','cuLsoda_all.cu'] },
      
      requires=['libSBML', 
                'matplotlib',
                'Numpy',
                'Scipy']
                )
