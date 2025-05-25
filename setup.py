from setuptools import setup, find_packages

setup(
    name='mylib',
    version='0.1.0',
    packages=find_packages(),
    description='Prosta biblioteka z funkcjami do danych, tekstu i matematyki',
    author='Mikołaj M.',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
