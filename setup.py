from setuptools import setup

setup(
    name='fielddirect-client-py',
    version='0.1.0',
    description='Client for Field Direct API',
    url='https://github.com/sotaog/fielddirectclient',
    author='Zachary Fox',
    author_email='zach@sotaog.com',
    license='MIT',
    packages=['fielddirectclient'],
    install_requires=['pyodata@git+https://github.com/sotaog/python-pyodata.git@experimental_v3', 'requests']
)
