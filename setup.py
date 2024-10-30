from setuptools import setup, find_packages

setup(
    name='helper_functions',
    version='0.1',
    description='utility function',
    author='Atharv Panditrao',
    author_email='atharvpan@g.ucla.edu',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
