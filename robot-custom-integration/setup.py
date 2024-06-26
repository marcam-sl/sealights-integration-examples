from setuptools import setup, find_packages

setup(
    name='sl-python-robot',
    version='1.0.0',
    install_requires=["requests==2.28.2", "robotframework", "robotframework-requests", "opentelemetry-distro", "robotframework-pabot", "robotframework-seleniumlibrary", "pyjwt"],
    packages=find_packages(),
    url='https://github.com/Sealights/sealights-integration-examples/tree/main/robot-custom-integration',
    license='',
    author='Bartosz Kaczkowski',
    author_email='bartosz.kaczkowski@sealights.io',
    description='Sealights Testing Optimization for Robot Framework'
)
