from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    print(long_description)

setup(
    name='myproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'myproject=myfirstproject.cli:cli',
        ],
    },
    author='suman',
    author_email='yl@logicode.in',
    description='Your CLI Tool Description',
    long_description=long_description,  # Include the contents of README.md
    long_description_content_type='text/markdown',
    url='https://github.com/MakwanaSuman/MYPROJECT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    # install_requires=['click',
    #                     "bson >= 0.5.10", 
    #                   "requests_toolbelt = 1.0.0",
    #                   "urllib3 = 2.1.0",],
                    
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.9.6",
)
