from setuptools import setup, find_packages

setup(
    name="demo_app",
    version='0.1',
    author="Tarren Peterson",
    author_email="tarrenjp@gmail.com",
    description=("Just a simple demo PyQt App"),
    license="GPL",
    packages=find_packages(),
    install_requires=[
        'PyQt5>=5.7',
    ],
    entry_points={
        'gui_scripts': [
            'demo_app = demo_app.__main__:main'
        ],
    }

)