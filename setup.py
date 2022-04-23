from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = "Visualize the Compton Data Space (CDS)"
with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()

setup(name='cds-visualization',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",      
      classifiers=['License :: MIT License', 'Programming Language :: Python :: 3.9.10'],       
      author="Jacqueline Beechert",
      author_email="jbeechert56@gmail.com",   
      python_requires=">=3",
      license="MIT",
      package_dir = {'':'code'},
      install_requires = ['pytest', 'numpy']
)
