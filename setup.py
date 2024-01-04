from setuptools import setup, find_packages

setup(
    name='mycli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mycli=mycli.cli:cli',
        ],
    },
    author='suman',
    author_email='yl@logicode.in',
    description='Your CLI Tool Description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mycli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
