from setuptools import setup, find_namespace_packages

with open('README.rst') as file:
    README = file.read()

setup(
  name = 'kubernetify',         # How you named your package folder (MyLib)
  packages=find_namespace_packages(),   # Chose the same as "name"
  version = '1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'takes a string and kubernetifies it',   # Give a short description about your library
  author = 'Greg Ford',                   # Type in your name
  author_email = 'gregford117@live.com',      # Type in your E-Mail
  url = 'https://github.com/gregford117/kubernetify',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/gregford117/kubernetify/archive/v_1.tar.gz',    # I explain this later on
  keywords = ['KUBERNETES', 'KUBERNETIFY'],   # Keywords that define your package best
  test_suite='nose.collector',
  tests_require=['nose'],
  install_requires=[],
  scripts = ['bin/kubernetify'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
