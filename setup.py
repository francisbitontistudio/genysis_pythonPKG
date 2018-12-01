from setuptools import setup


setup(name='genysis',
      version='0.0.1',
      url='https://github.com/francisbitontistudio/genysis_pythonPKG.git',
      author='F. Bitonti',
      author_email='Francis@studiobitonti.com',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: CAD',
          'Programming Language :: Python :: 2'
      ],
      packages=['genysis'],
      install_requires=[
          'json>=18.2',
          'ast>=32.2'
      ]
      # entry_points={
      #     'console_scripts': [
      #         'encrypt=crytto.main:run'
      #     ]
      # }
)
